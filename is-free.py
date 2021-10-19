import requests
import json
#Opens and reads the token from the file called "token"
fi = open("token", "r")


# Makes a get request to the endpoint below
url = "https://mobile.laundryrestart.com/jhclaundry/api/catalog/machines/1"
payload={}
headers = {
  'Authorization': fi.read(),
  'location': '6'
}
response = requests.request("GET", url, headers=headers, data=payload)

#Deals with the response
data = response.json()
query = json.dumps(data)
a = json.loads(query)

# For loop to show the status of the machines
for s in range(6):
   print("machine {} is {}.".format(a[s]["name"], a[s]["isAvailable"]))

fi.close()