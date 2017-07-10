#!/usr/bin/python 

import json,httplib,urllib
connection = httplib.HTTPSConnection('api.parse.com', 443)
params = urllib.urlencode({"where":json.dumps({ "muscleGroups": {"$all":['abs']} })})
connection.connect()
connection.request('GET', '/1/classes/phitr_exercises?%s' % params,'', {
       "X-Parse-Application-Id": "iD9PNLAaagv0kxKYFFGjO8po8YzwCZUVJURprNCf",
       "X-Parse-REST-API-Key": "K851QkMefzmsD8e7O1i59pwn6Am6HlJQr3yCbaOQ"
     })
result = json.loads(connection.getresponse().read())   
jResult = json.loads(result)
print jResult