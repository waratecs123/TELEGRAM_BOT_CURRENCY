import requests
import json

r = requests.get("https://baconipsum.com/api/?type=meat-and-filler")
r = json.loads(r.content)

print(r)