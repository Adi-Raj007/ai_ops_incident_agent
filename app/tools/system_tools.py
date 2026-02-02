import psutil


def check_cpu():
    """
    Returns CPU usage percentage
    """
    cpu_percent = psutil.cpu_percent(interval=1)

    return {
        "metric": "cpu",
        "value": cpu_percent,
        "unit": "%",
        "status": (
            "critical" if cpu_percent > 85
            else "warning" if cpu_percent > 70
            else "normal"
        )
    }


def check_memory():
    """
    Returns RAM usage details
    """
    mem = psutil.virtual_memory()

    return {
        "metric": "memory",
        "value": mem.percent,
        "unit": "%",
        "available_mb": round(mem.available / (1024 * 1024), 2),
        "status": (
            "critical" if mem.percent > 85
            else "warning" if mem.percent > 70
            else "normal"
        )
    }


def check_disk():
    """
    Returns disk usage percentage
    """
    disk = psutil.disk_usage("/")

    return {
        "metric": "disk",
        "value": disk.percent,
        "unit": "%",
        "free_gb": round(disk.free / (1024 * 1024 * 1024), 2),
        "status": (
            "critical" if disk.percent > 85
            else "warning" if disk.percent > 70
            else "normal"
        )
    }
