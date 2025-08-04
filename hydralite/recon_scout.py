import requests
import subprocess
import time

def banner():
    print("="*50)
    print("HydraFlow Recon Phase 🐍 | Popla69 ReconScout")
    print("="*50)

def get_final_url(domain):
    if not domain.startswith("http"):
        https_url = f"https://{domain}"
        http_url = f"http://{domain}"
    else:
        return domain  # already full URL

    try:
        res = requests.get(https_url, timeout=5)
        if res.status_code < 400:
            return https_url
    except:
        pass

    try:
        res = requests.get(http_url, timeout=5)
        if res.status_code < 400:
            return http_url
    except:
        pass

    return None

def get_headers(url):
    try:
        res = requests.get(url, timeout=10)
        print(f"[+] {url} Status: {res.status_code}")
        print("[+] Headers:")
        for k, v in res.headers.items():
            print(f"    {k}: {v}")
    except Exception as e:
        print(f"[-] Failed to fetch headers: {e}")

def tech_stack_with_whatweb(url):
    print("\n[+] Running WhatWeb scan...")
    try:
        subprocess.run(["perl", "/data/data/com.termux/files/usr/bin/whatweb", url])
    except Exception as e:
        print(f"[-] WhatWeb failed: {e}")

def cname_lookup(domain):
    print("\n[+] Checking CNAME records...")
    try:
        result = subprocess.check_output(["nslookup", "-type=CNAME", domain])
        print(result.decode())
    except Exception as e:
        print(f"[-] CNAME lookup failed: {e}")

if __name__ == "__main__":
    banner()
    user_input = input("Enter full URL or domain (e.g., example.com): ").strip()
    final_url = get_final_url(user_input)

    if not final_url:
        print("❌ Could not reach the target site on HTTPS or HTTP.")
        exit()

    print(f"[✓] Resolved target: {final_url}\n")

    get_headers(final_url)
    tech_stack_with_whatweb(final_url)

    domain = final_url.replace("https://", "").replace("http://", "").split("/")[0]
    cname_lookup(domain)

    print("\n[✓] Passive Recon Complete ✅")
