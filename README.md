# AI Ops Incident Response Agent  
**LangGraph · LangChain · System Diagnostics · Explainable AI**

---

## 📌 Project Overview

This project is an **AI-powered Incident Response Agent** built with a **System Engineer–first mindset**.

It is NOT a chatbot.

The system understands natural-language incident descriptions, forms **multiple diagnostic hypotheses**, validates them using **real system metrics (CPU, RAM, Disk)**, explains its reasoning with evidence, assigns **incident severity**, and orchestrates the workflow using **LangGraph**.

The focus is on **correctness, safety, explainability, and production-style architecture**.

---

## 🎯 Problem Statement

System engineers often receive vague and ambiguous incident reports such as:

- “My system is lagging”
- “Everything feels slow”
- “Server is behaving weird”
- “Performance dropped suddenly”

These descriptions cannot be trusted directly.

This project automates **first-level incident triage** by:
1. Understanding user intent (LLM-assisted)
2. Generating multiple diagnostic hypotheses
3. Collecting real system evidence
4. Eliminating incorrect causes
5. Explaining the final decision
6. Assigning severity for prioritization

---

## 🧠 Core Design Principles

- **Hybrid Intelligence** – Rule-based logic + LLM (LLM never has final authority)
- **Multi-Hypothesis Reasoning** – Never assume a single root cause
- **Evidence-Driven Decisions** – Use real system metrics only
- **Explainability** – Every decision is justified with evidence
- **Safety First** – Escalate when confidence is low
- **Deterministic Workflow** – Controlled using LangGraph

---

## 🏗️ High-Level Architecture

User Input (Natural Language)  
↓  
Rule + LLM Classification (LangChain)  
↓  
Hypothesis Generation  
↓  
System Diagnostics (CPU / RAM / Disk)  
↓  
Evidence Collection  
↓  
Root Cause Selection  
↓  
Severity Scoring  
↓  
Final Explainable Output  

---

## 📁 Project Structure

ai_ops_incident_agent  
├── app  
│   ├── agents  
│   │   └── classifier_agent.py  
│   ├── tools  
│   │   └── system_tools.py  
│   ├── diagnostics  
│   │   └── hypothesis_engine.py  
│   ├── evidence  
│   │   └── evidence_builder.py  
│   ├── severity  
│   │   └── severity_engine.py  
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
- LangChain (LLM orchestration)
- LangGraph (workflow orchestration)
- ChatGroq (LLaMA-3)
- Pydantic (schema validation)
- psutil (real system metrics)
- python-dotenv (configuration management)

---

## 🧩 Diagnostics Covered (Current Stage)

| Component | Purpose |
|---------|--------|
| CPU | Detect CPU saturation |
| Memory (RAM) | Detect memory pressure |
| Disk | Detect storage bottlenecks |
| Unknown | Safe escalation |

---

## 🔍 Multi-Hypothesis Diagnostic Engine (Rare Feature)

Instead of assuming a single root cause, the agent evaluates **multiple hypotheses sequentially**, similar to how real system engineers troubleshoot.

Example flow:

User input:  
`"System is lagging"`

Hypotheses evaluated:
- CPU → normal
- Memory → critical
- Disk → skipped

Final Root Cause: **Memory pressure**

---

## 🧪 Evidence-Based Explainability

Every output includes:
- Metrics checked
- Which causes were ruled out
- Why the final cause was selected

Example:

Evidence:
- CPU usage: 12% (normal)
- Memory usage: 89% (critical)

Reasoning:
- CPU was ruled out due to normal usage.
- Memory usage is critical, indicating a likely bottleneck.

This makes the system **auditable and trustworthy**.

---

## 🚦 Severity Scoring (Production-Oriented)

Severity is assigned **after evidence collection**, not from user text.

| Condition | Severity |
|--------|---------|
| Any critical metric | CRITICAL |
| Multiple warnings | HIGH |
| Single warning | MEDIUM |
| All metrics normal | LOW |
| No clear root cause | MEDIUM (safe escalation) |

This mirrors real incident management systems.

---

