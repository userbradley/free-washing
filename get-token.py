import requests
import urllib.parse
import json
username = "<>"
password = "<>"

f = { 'username' : username, 'password' : password, 'client_id' : '1_1881648594', 'client_secret' : 'A4f5d4gf59aT4566999999GHJ', 'grant_type' : 'password'}
urllib.parse.urlencode(f)
safe_string = urllib.parse.urlencode(f)
url = "https://mobile.laundryrestart.com/jhclaundry/oauth/v2/token"
payload = safe_string
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}
response = requests.request("POST", url, headers=headers, data=payload)

data = response.json()
query = json.dumps(data)
a = json.loads(query)
#print(response.text)
print("the access token is:",a["access_token"])

# Write to file to use in other scripts
fi = open("token", "w")
fi.write(a["access_token"])
