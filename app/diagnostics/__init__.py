from app.tools.system_tools import check_cpu, check_memory, check_disk


def generate_hypotheses(initial_type: str):
    """
    Decide which hypotheses to evaluate and in what order.
    """

    if initial_type == "cpu":
        return ["cpu", "memory", "disk"]

    if initial_type == "disk":
        return ["disk"]

    if initial_type == "service":
        return ["service"]

    # vague / unknown issues
    return ["cpu", "memory", "disk"]


def evaluate_hypotheses(hypotheses: list):
    """
    Evaluate each hypothesis using system evidence.
    Stop when a critical/warning issue is found.
    """

    evidence = []
    root_cause = None

    for h in hypotheses:
        if h == "cpu":
            result = check_cpu()
        elif h == "memory":
            result = check_memory()
        elif h == "disk":
            result = check_disk()
        else:
            continue

        evidence.append(result)

        if result["status"] in ("critical", "warning"):
            root_cause = result
            break

    return root_cause, evidence
