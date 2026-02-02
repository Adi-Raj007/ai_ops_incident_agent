from langgraph.graph import StateGraph, END

from app.agents.classifier_agent import classify_incident
from app.diagnostics.hypothesis_engine import (
    generate_hypotheses,
    evaluate_hypotheses,
)
from app.evidence.evidence_builder import build_evidence_report
from app.severity.severity_engine import calculate_severity


def diagnosis_node(state: dict) -> dict:
    print("GRAPH: Entered DIAGNOSIS node")

    incident_type = state.get("incident_type", "unknown")

    # 1️⃣ Generate hypotheses
    hypotheses = generate_hypotheses(incident_type)

    # 2️⃣ Evaluate hypotheses using system tools
    root_cause, evidence = evaluate_hypotheses(hypotheses)

    # 3️⃣ Build evidence-backed explanation
    report = build_evidence_report(root_cause, evidence)

    # 4️⃣ Calculate severity
    severity = calculate_severity(root_cause, evidence)

    # 5️⃣ Update state
    state["root_cause"] = root_cause["metric"] if root_cause else "unknown"
    state["severity"] = severity
    state["evidence_report"] = report

    return state


def build_incident_graph():
    graph = StateGraph(dict)

    # Nodes
    graph.add_node("classify", classify_incident)
    graph.add_node("diagnose", diagnosis_node)

    # Entry
    graph.set_entry_point("classify")

    # Flow
    graph.add_edge("classify", "diagnose")
    graph.add_edge("diagnose", END)

    return graph.compile()
