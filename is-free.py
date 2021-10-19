import requests, json, datetime
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

# For loop to show the status of the machines and time left where it's relevant
for s in range(6):

   if a[s]["statusName"] == "Reserved": #should be Reserved

    tl = str(datetime.timedelta(seconds=a[s]["secLeft"]))
    print("machine {}".format(a[s]["name"]),"is Reserved and has", tl, "remaining")

   elif a[s]["statusName"] == "Available":

    print("machine {} is {}.".format(a[s]["name"], a[s]["statusName"]))

   elif a[s]["statusName"] == "Busy": #should be Busy

    tl = str(datetime.timedelta(seconds=a[s]["secLeft"]))
    print("machine {}".format(a[s]["name"]),"is Busy and has", tl, "remaining")

fi.close()