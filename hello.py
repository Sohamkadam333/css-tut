import requests
import json


headers = {'Accept': 'application/json'}

r = requests.get('https://catfact.ninja/fact', headers=headers)

print(r.json()['fact'])
# y = json.loads(r.json())
# print(y)
