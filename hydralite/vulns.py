import requests

def scan_vulnerabilities():
    print("\n🔍 Popla Vulnerability Scanner")
    url = input("Enter full URL (e.g., http://example.com): ").strip()

    if not url.startswith("http"):
        print("❌ Invalid URL. Please include http:// or https://")
        return

    try:
        print(f"\n🧠 Starting vulnerability scan on: {url}")
        response = requests.get(url, timeout=5)
        headers = response.headers

        known_headers = {
            "X-Content-Type-Options": "📛 Prevents MIME-sniffing attacks",
            "X-Frame-Options": "🛡️ Clickjacking protection",
            "X-XSS-Protection": "🧪 Cross-site scripting filter",
            "Content-Security-Policy": "🔒 Blocks inline scripts/styles",
            "Strict-Transport-Security": "📶 Enforces HTTPS connections",
            "Referrer-Policy": "🌐 Controls Referer header behavior",
            "Permissions-Policy": "📱 Controls camera/mic/geolocation APIs"
        }

        found = []
        missing = []

        for header, description in known_headers.items():
            if header in headers:
                print(f"✅ {header} is present: {headers[header]}")
                found.append(header)
            else:
                print(f"⚠️ {header} is **MISSING** — {description}")
                missing.append(header)

        print("\n📋 Summary:")
        print(f"🔹 Found headers: {len(found)}")
        print(f"🔻 Missing headers: {len(missing)}")

    except requests.exceptions.RequestException as e:
        print(f"\n❌ Error fetching URL: {e}")
