#!/usr/bin/python

import json,httplib
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()                 

data = []
with open('exercises.json') as f:
    for line in f:
        data.append(json.loads(line)) 
              
    for ex in data:
		connection.request('POST', '/1/classes/phitr_exercises', json.dumps(ex, separators=(',',':')), {
		"X-Parse-Application-Id": "iD9PNLAaagv0kxKYFFGjO8po8YzwCZUVJURprNCf",
		"X-Parse-REST-API-Key": "K851QkMefzmsD8e7O1i59pwn6Am6HlJQr3yCbaOQ",
		"Content-Type": "application/json"
		})
		results = json.loads(connection.getresponse().read())
		print results