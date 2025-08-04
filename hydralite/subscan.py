import requests

def subdomain_scanner():
    domain = input("Enter the domain (e.g., example.com): ").strip()
    if not domain:
        print("❌ No domain entered. Exiting.")
        return

    # Sample wordlist – expand as needed
    subdomains = ["www", "mail", "ftp", "blog", "test", "dev", "admin"]

    print(f"\n🔍 Scanning subdomains for: {domain}\n")

    found = False
    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url, timeout=3)
            print(f"✅ Found: {url} [Status: {response.status_code}]")
            found = True
        except requests.ConnectionError:
            pass

    if not found:
        print("❌ No subdomains found or they are not live.")

# Run only when this file is executed directly
if __name__ == "__main__":
    subdomain_scanner()
