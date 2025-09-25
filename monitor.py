import subprocess
import sys

def enable_monitor(interface):
    subprocess.run(["airmon-ng", "start", interface])

def disable_monitor(interface):
    subprocess.run(["airmon-ng", "stop", interface])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python monitor.py --enable/--disable <interface>")
        sys.exit(1)

    action = sys.argv[1]
    iface = sys.argv[2]

    if action == "--enable":
        enable_monitor(iface)
    elif action == "--disable":
        disable_monitor(iface)
    else:
        print("Invalid action. Use --enable or --disable.")
