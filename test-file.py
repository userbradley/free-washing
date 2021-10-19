import urllib.parse
#f = { 'username' : 'mike.jones@breadnet.co.uk', 'password' : 'Indigo!212', 'client_id' : '1_1881648594', 'client_secret' : 'A4f5d4gf59aT4566999999GHJ', 'grant_type' : 'password' }
#urllib.urlencode(f)
#f = { 'eventName' : 'myEvent', 'eventDescription' : 'cool event'}
#urllib.urlencode(f)
#print(urllib.parse.urlencode(f))

f = { 'username' : 'mike.jones@breadnet.co.uk', 'password' : 'Indigo!212', 'client_id' : '1_1881648594', 'client_secret' : 'A4f5d4gf59aT4566999999GHJ', 'grant_type' : 'password'}
a = urllib.parse.urlencode(f)
print(a)