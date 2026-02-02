def calculate_severity(root_cause: dict, evidence: list) -> str:
    """
    Determine incident severity based on diagnostic evidence.
    """

    if not evidence:
        return "LOW"

    critical_count = 0
    warning_count = 0

    for e in evidence:
        if e["status"] == "critical":
            critical_count += 1
        elif e["status"] == "warning":
            warning_count += 1

    # Severity rules
    if critical_count >= 1:
        return "CRITICAL"

    if warning_count >= 2:
        return "HIGH"

    if warning_count == 1:
        return "MEDIUM"

    # If no clear root cause but metrics checked
    if not root_cause:
        return "MEDIUM"

    return "LOW"
