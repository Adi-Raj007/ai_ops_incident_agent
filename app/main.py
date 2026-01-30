from app.graph.incident_graph import build_incident_graph


def main():
    graph = build_incident_graph()

    print("AI Ops Incident Agent Started")
    user_input = input("Describe the system issue: ")

    initial_state = {
        "user_input": user_input
    }

    final_state = graph.invoke(initial_state)

    print("\nFINAL RESULT:")
    print(final_state["result"])


if __name__ == "__main__":
    main()
