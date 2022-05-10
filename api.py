# RESTful APIS

import requests

import json

response = requests.get("https://api.stackexchange.com/docs/badges#order=desc&sort=rank&filter=default&site=stackoverflow&run=true")
print(response.json())