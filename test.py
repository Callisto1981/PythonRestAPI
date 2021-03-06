import requests

BASE = "http://127.0.01:5000/"  # LocalHost url that this is running on

response = requests.put(BASE + "video/1", {"likes": 10})
print(response.json())
