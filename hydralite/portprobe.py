import socket
import sys

target = input("Enter target domain or IP: ")
common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 8080]

print(f"\n[🔍] Scanning {target}...\n")

for port in common_ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
        sock.close()
    except socket.gaierror:
        print("Hostname couldn't be resolved.")
        break
    except socket.error:
        print("Connection error.")
        break
