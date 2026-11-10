import json
import requests

url = "https://arctic-shift.photon-reddit.com/api/posts/search"

params = {
    "subreddit": "concordia",
    "limit": 100,
    "sort": "desc"
}

response = requests.get(url, params=params, timeout=30)
response.raise_for_status()

data = response.json()

with open("data/concordia.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print("Downloaded", len(data["data"]), "concordia posts")