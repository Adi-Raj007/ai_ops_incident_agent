import psutil

def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent
def check_disk_usage():
    disk=psutil.disk_usage('/')
    return disk.percent
def check_service_status(service_name: str):
    """
    Mock service status check
    """
    if service_name.lower() == "nginx":
        return "stopped"
    return "running"
