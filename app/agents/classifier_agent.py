from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from app.schema.incident_schema import IncidentClassification

load_dotenv()

# ----------------------------
# Rule-based fallback
# ----------------------------
def rule_based_classification(user_input: str):
    text = user_input.lower()

    if "cpu" in text:
        return "cpu"
    if "disk" in text or "storage" in text:
        return "disk"
    if "service" in text or "nginx" in text:
        return "service"

    return None


# ----------------------------
# LangChain + ChatGroq setup
# ----------------------------
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

parser = PydanticOutputParser(
    pydantic_object=IncidentClassification
)

prompt = ChatPromptTemplate.from_template(
    """
You are a system incident classifier.

Classify the following user-reported system issue into ONE of:
- cpu
- disk
- service
- unknown

Rules:
- Respond ONLY in valid JSON
- No explanation text
- JSON must have exactly two fields:
  - incident_type
  - confidence (number between 0 and 1)

User issue:
"{user_input}"
"""
)


# ----------------------------
# Hybrid classifier (FINAL)
# ----------------------------
def classify_incident(state: dict) -> dict:
    user_input = state.get("user_input", "")

    print("AGENT: Starting incident classification")

    # 1️⃣ Rule-based check
    rule_result = rule_based_classification(user_input)
    if rule_result:
        print(f"AGENT: Rule-based classification -> {rule_result}")
        state["incident_type"] = rule_result
        state["confidence"] = 1.0
        return state

    # 2️⃣ LLM-based classification
    print("AGENT: Using LLM for classification")

    try:
        chain = prompt | llm | parser
        result = chain.invoke({"user_input": user_input})

        # Confidence gate
        if result.confidence < 0.6:
            print("AGENT: Low confidence from LLM, falling back to UNKNOWN")
            state["incident_type"] = "unknown"
            state["confidence"] = result.confidence
        else:
            state["incident_type"] = result.incident_type
            state["confidence"] = result.confidence

    except Exception as e:
        print("AGENT: LLM failed, falling back to UNKNOWN")
        print(f"ERROR: {e}")
        state["incident_type"] = "unknown"
        state["confidence"] = 0.0

    return state
