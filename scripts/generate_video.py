import requests

API_KEY = "YOUR_HIGGSFIELD_API_KEY"

url = "https://api.higgsfield.ai/v1/video/generate"

payload = {
    "prompt": "Luxury woman walking in Dubai mall",
    "duration": 5
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
