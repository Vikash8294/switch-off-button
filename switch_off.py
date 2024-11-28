import tkinter as tk
import os
import sys
import platform

def shutdown():
    """Shuts down the system."""
    system_platform = platform.system().lower()
    if system_platform == "windows":
        os.system("shutdown /s /f /t 0")
    elif system_platform == "linux" or system_platform == "darwin":
        os.system("sudo shutdown now")
    else:
        print("Unsupported OS!")

def restart():
    """Restarts the system."""
    system_platform = platform.system().lower()
    if system_platform == "windows":
        os.system("shutdown /r /f /t 0")
    elif system_platform == "linux" or system_platform == "darwin":
        os.system("sudo reboot")
    else:
        print("Unsupported OS!")

def create_app():
    """Create a simple GUI with shutdown and restart buttons."""
    root = tk.Tk()
    root.title("System Control")

    shutdown_button = tk.Button(root, text="Shutdown", command=shutdown, width=20, height=2)
    shutdown_button.pack(pady=10)

    restart_button = tk.Button(root, text="Restart", command=restart, width=20, height=2)
    restart_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_app()
