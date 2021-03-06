import requests

BASE = "http://127.0.01:5000/"  # LocalHost url that this is running on

response = requests.put(BASE + "video/1", {"likes": 10, "name": "Wayne", "views": 1853205})
print(response.json())

input()

response = requests.get(BASE + "video/1")
print(response.json())