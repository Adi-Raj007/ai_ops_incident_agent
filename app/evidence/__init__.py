def build_evidence_report(root_cause: dict, evidence: list) -> str:
    """
    Build a human-readable explanation from diagnostic evidence.
    """

    if not root_cause:
        return (
            "No clear root cause could be identified.\n\n"
            "Evidence checked:\n"
            + "\n".join(
                f"- {e['metric'].capitalize()} usage: {e['value']}{e['unit']} "
                f"({e['status']})"
                for e in evidence
            )
            + "\n\nConclusion:\nEscalating to system administrator."
        )

    lines = []

    # Root cause
    lines.append(f"Root Cause: {root_cause['metric'].capitalize()} issue\n")

    # Evidence section
    lines.append("Evidence:")
    for e in evidence:
        lines.append(
            f"- {e['metric'].capitalize()} usage: "
            f"{e['value']}{e['unit']} ({e['status']})"
        )

    # Reasoning section
    lines.append("\nReasoning:")
    for e in evidence:
        if e["metric"] != root_cause["metric"]:
            lines.append(
                f"- {e['metric'].capitalize()} was ruled out "
                f"because usage is {e['status']}."
            )

    lines.append(
        f"- {root_cause['metric'].capitalize()} usage is "
        f"{root_cause['status']}, indicating a likely bottleneck."
    )

    return "\n".join(lines)
