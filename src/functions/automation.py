import os
import webbrowser
import psutil
import subprocess

def open_chrome():
    """Opens Google Chrome."""
    webbrowser.open("https://www.google.com")

def open_calculator():
    """Opens the Windows Calculator."""
    os.system("calc")  # Windows-specific

def open_notepad():
    """Opens Notepad."""
    os.system("notepad")  # Windows-specific

def get_cpu_usage():
    """Returns the current CPU usage as a percentage."""
    return psutil.cpu_percent()

def get_ram_usage():
    """Returns the current RAM usage as a percentage."""
    return psutil.virtual_memory().percent

def run_command(command):
    """Runs a PowerShell command and returns the output."""
    try:
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

def create_file(filename):
    """Creates an empty file with the given name."""
    with open(filename, 'w') as f:
        pass
    return f"File {filename} created."

def get_disk_space():
    """Returns the free disk space on the C: drive in GB."""
    disk = psutil.disk_usage('C:\\')
    return disk.free / (1024 ** 3)  # Convert bytes to GB

# Additional functions
def list_running_processes():
    """Lists the top 5 running processes by memory usage."""
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    # Sort by memory usage and get top 5
    top_processes = sorted(processes, key=lambda x: x['memory_percent'], reverse=True)[:5]
    return top_processes

def check_internet_connection():
    """Checks if there is an active internet connection."""
    try:
        # Try to connect to Google's DNS server
        result = subprocess.run(["ping", "-n", "1", "8.8.8.8"], capture_output=True, text=True)
        return "Connected" if result.returncode == 0 else "Disconnected"
    except Exception as e:
        return f"Error checking connection: {str(e)}"