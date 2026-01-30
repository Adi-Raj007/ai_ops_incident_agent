# AI Ops Incident Response Agent (LangGraph + LangChain)

## 📌 Project Overview

This project is an AI-powered Incident Response Agent designed from a System Engineer’s perspective.  
It helps in triaging common system issues by understanding natural language input, classifying the incident, validating decisions safely, and routing execution through a controlled workflow.

This system is NOT a chatbot.  
It is a decision-making agent that combines deterministic rules, LLM-based reasoning, strict schema validation, and a state-machine workflow.

---

## 🎯 Problem Statement

System engineers often receive unclear, human-written incident descriptions such as:

- System feels slow
- Everything is lagging
- Website not responding
- No space left on server

Manually interpreting these messages is time-consuming and error-prone.

This project automates the first level of incident triage by:
1. Understanding the user’s intent
2. Classifying the type of incident
3. Executing the correct diagnostic checks
4. Responding safely and transparently

---

## 🧠 Core Design Principles

- Safety First – LLM outputs are never trusted directly  
- Hybrid Intelligence – Rules + LLM (not LLM-only)  
- Strict Validation – All AI outputs pass through Pydantic schemas  
- Deterministic Workflow – Execution controlled using LangGraph  
- System-Oriented – Uses real system metrics  

---

## 🏗️ High-Level Architecture

User Input  
↓  
Rule-Based Heuristics (Fast & Safe)  
↓  
LangChain + ChatGroq (Ambiguous Cases)  
↓  
Pydantic Schema Validation  
↓  
LangGraph Workflow (State Machine)  
↓  
System Tools (CPU / Disk / Service)  
↓  
Final Response  

---

## 📁 Project Structure

ai_ops_incident_agent  
├── app  
│   ├── agents  
│   │   └── classifier_agent.py  
│   ├── tools  
│   │   └── system_tools.py  
│   ├── schema  
│   │   └── incident_schema.py  
│   ├── graph  
│   │   └── incident_graph.py  
│   └── main.py  
├── requirements.txt  
├── .env  
├── .gitignore  
└── README.md  

---

## ⚙️ Technologies Used

- Python 3.10+  
- LangChain  
- LangGraph  
- ChatGroq (LLaMA-3)  
- Pydantic  
- psutil  
- python-dotenv  

---

## 🧩 Incident Types Supported (Current Stage)

CPU – High CPU usage, system slowness  
Disk – Disk full, storage issues  
Service – Service (e.g., nginx) down  
Unknown – Ambiguous or unsafe to classify  

---

## 🛡️ Safety Mechanisms

- LLM output is validated using strict Pydantic schemas  
- Only predefined incident types are allowed  
- Confidence thresholds are enforced  
- Low-confidence outputs fall back to unknown  
- Unsafe cases are escalated, not guessed  

---

## ▶️ How to Run the Project

1. Activate virtual environment  

source venv/bin/activate  

(Windows: venv\\Scripts\\activate)

2. Add Groq API key  

Create a `.env` file in project root:

GROQ_API_KEY=your_api_key_here  

3. Run the application  

python -m app.main  

---

## 🧪 Example Inputs

CPU usage is very high  
System feels slow since morning  
Disk is almost full  
Everything is broken  

---

## ✅ Example Output

AGENT: Starting incident classification  
AGENT: Using LLM for classification  
GRAPH: Entered CPU node  

FINAL RESULT:  
CPU usage is normal at 1.3%.  

This demonstrates:
- LLM-based understanding  
- Deterministic workflow routing  
- Real system metric verification  
- Safe, non-hallucinatory output  

---

## ❌ Why This Is Not a Chatbot

Chatbots give free-text replies.  
This project follows a structured decision workflow.

Chatbots trust LLM blindly.  
This project validates every LLM output with schema checks.

Chatbots do not use system tools.  
This project runs real diagnostics.

---

## 🚀 Future Enhancements

- Memory / RAM diagnostics  
- Multi-hypothesis evaluation  
- Log analysis agent  
- FastAPI-based API service  
- IAM / Access review extension  
- Dockerized deployment  

---

## 👨‍💻 Author Notes

This project is built incrementally with a strong focus on:
- engineering discipline  
- safety-first AI  
- real system engineering practices  

---

## 📌 Interview Summary

I built a hybrid AI incident response system using LangChain for controlled LLM reasoning, Pydantic for strict validation, and LangGraph for deterministic workflow orchestration, backed by real system metrics.
