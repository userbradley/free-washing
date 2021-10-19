import json, requests

url = "https://api.github.com/users/userbradley"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()
query = json.dumps(data)
a = json.loads(query)
print(a["name"])
#print(data)

#print(json.load(sys.stdin)['name'])
#print(json.load(query)['name'])