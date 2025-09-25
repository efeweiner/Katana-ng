import subprocess

def list_interfaces():
    result = subprocess.run(["iwconfig"], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    list_interfaces()
