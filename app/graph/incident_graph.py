from langgraph.graph import StateGraph , END


from app.agents.classifier_agent import classify_incident
from app.tools.system_tools import (
check_cpu_usage,
check_disk_usage,
check_service_status,
)


def cpu_node(state:dict)->dict:
    print("GRAPH: Entered CPU node")
    cpu =check_cpu_usage()
    if cpu >80:
        state["result"]=(f"CPU usage is {cpu}%."
                         "Suggested action: check running processes or restart heavy services.")
    else:
        state["result"]=f"CPU usage is normal at {cpu}%."
    return state
def disk_node(state:dict)->dict:
    print("GRAPH: Entered Disk node")
    disk =check_disk_usage()
    if disk >80:
        state["result"]=(f"Disk usage is {disk}%."
                         "Suggested action: clean logs or temporary files.")
    else:
        state["result"]=f"Disk usage is normal at {disk}%."
    return state

def service_node(state:dict)->dict:
    print("GRAPH: Entered Service node")
    status =check_service_status("nginx")
    if status =="stopped":
        state["result"]=("Nginx service is stopped. Suggested action: restart the service.")
    else:
        state["result"]="Service is running normally."
    return state

def unknown_node(state:dict)->dict:
    print("GRAPH: Entered UNKNOWN node")
    state["result"]=("Incident could not be confidently classified."
                     "Escalating to system administrator.")
    return state


def build_incident_graph():
    graph = StateGraph(dict)

    #Nodes
    graph.add_node("classify",classify_incident)
    graph.add_node("cpu",cpu_node)
    graph.add_node("disk",disk_node)
    graph.add_node("service",service_node)
    graph.add_node("unknown",unknown_node)

    #Entry Point
    graph.set_entry_point("classify")

    #conditional routing
    graph.add_conditional_edges(
        "classify",
        lambda state: state["incident_type"],
        {
            "cpu":"cpu",
            "disk":"disk",
            "service":"service",
            "unknown":"unknown",

        },

    )
    graph.add_edge("cpu",END)
    graph.add_edge("disk",END)
    graph.add_edge("service",END)
    graph.add_edge("unknown",END)



    return graph.compile()