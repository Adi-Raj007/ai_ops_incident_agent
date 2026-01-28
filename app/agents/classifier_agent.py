def classify_incident(state:dict)->dict:
    user_input=state.get("user_input","").lower()
    print("Agent:classifying incident")
    if "cpu" in user_input:
        state["incident_type"]="cpu"
    elif "disk" in user_input or "storage" in user_input:
        state["incident_type"]="disk"
    elif "service" in user_input or "nginx" in user_input:
        state["incident_type"]="service"
    else:
        state["incident_type"]="unknown"
    print(f"AGENT: Incident classified as {state['incident_type']}")
    return state
