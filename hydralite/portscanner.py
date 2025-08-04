import socket
import concurrent.futures

print("┌────────────── HydraFlow PortScanner ─────────────┐")
target = input("Enter IP or domain to scan: ").strip()

# Common ports to scan (feel free to expand)
common_ports = {
    21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 53: 'DNS',
    80: 'HTTP', 110: 'POP3', 143: 'IMAP', 443: 'HTTPS',
    3306: 'MySQL', 8080: 'HTTP-Alt'
}

def scan_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                return f"[OPEN] Port {port} ({common_ports.get(port, 'Unknown')})"
    except:
        return None

print(f"\nScanning {target}...\n")
with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    results = executor.map(scan_port, common_ports.keys())
    for res in results:
        if res:
            print(res)

print("\n└──────────────────── Scan Done ───────────────────┘")
