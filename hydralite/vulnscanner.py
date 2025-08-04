import requests

print("🔎 HydraLite Vulnerability Scanner")

target = input("Enter full URL (e.g., https://example.com): ").strip()

# Very basic test patterns
vuln_paths = [
    "/phpinfo.php", "/test.php", "/admin/", "/login.php",
    "/.env", "/config.php", "/.git", "/wp-login.php"
]

headers = {
    "User-Agent": "HydraLiteScanner/1.0"
}

for path in vuln_paths:
    url = target.rstrip("/") + path
    try:
        res = requests.get(url, headers=headers, timeout=5)
        if res.status_code == 200:
            print(f"[⚠️ FOUND] Potential issue at: {url}")
    except requests.exceptions.RequestException:
        pass

print("✅ Scan complete.")
