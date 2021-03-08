import requests

BASE = "http://127.0.01:5000/"  # LocalHost url that this is running on
data = [
    {"likes": 18978013, "name": "Conan the Barbarian", "views": 1789007},
    {"likes": 954475, "name": "Waiting...", "views": 86225634},
    {"likes": 165152, "name": "The Game", "views": 14923008746}
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())


input()
response = requests.get(BASE + "video/2")
print(response.json())