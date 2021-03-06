import requests

BASE = "http://127.0.01:5000/" # LocalHost url that this is running on

response = requests.get(BASE + "helloworld")
print(response.json())