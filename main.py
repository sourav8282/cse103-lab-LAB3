import urllib.request
import ssl
import certifi

print("Hello, GitHub!")

url = "https://api.github.com"

context = ssl.create_default_context(cafile=certifi.where())

try:
    response = urllib.request.urlopen(url, context=context)
    print("API Status:", response.status)
    print(response.read().decode())

except Exception as e:
    print("API request failed:", e)
