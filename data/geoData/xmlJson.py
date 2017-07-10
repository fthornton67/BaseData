import fnmatch
import os
import csv    
import sys    
import json
import http.client
import urllib.parse
import xml        
from xml.etree import ElementTree as ET
import threading
import time


rootPath = '.'
pattern = 'US*.csv'   

class postThread (threading.Thread):
	def __init__(self,jsonLine):
		threading.Thread.__init__(self)
		self.jsonLine = jsonLine
	def run(self):
		print ("Starting " + self.name)
		# Get lock to synchronize threads
		threadLock.acquire()
		postCurrentItem(self.jsonLine)
		# Free lock to release next thread
		threadLock.release()
def postCurrentItem(jsonLine):
	connection = http.client.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('POST', '/1/classes/sfm_Geo_USCounties', json.dumps(json.loads(jsonLine)), {
           "X-Parse-Application-Id": "orOInbx3WpwNjlZE0op7lv7HSeFA4tlsCENATg3U",
           "X-Parse-REST-API-Key": "tqGKF4vtGQHQ3y5f99EVWgrtBlWEd9Em9uzhwc4q",
           "Content-Type": "application/json"
         })                  
	print(connection.getresponse().read())
	

def createJsonString(county,state,shape):
	jsonString = "\"county\" : \"{0}\", \"state\" : \"{1}\", \"shapePoints\": {2}".format(county.strip(),state.strip(),json.dumps(shape.split(' ')))
	return "{" + jsonString  +"}"

threadLock = threading.Lock()
threads = []

import xml.etree.ElementTree as ET
tree = ET.parse('counties.xml')
root = tree.getroot()
for child in root.findall('{http://www.w3.org/2000/svg}g'):
	for sChild in child:  
		cThread = postThread(createJsonString(sChild.attrib.get('id').split(',')[0],
		sChild.attrib.get('id').split(',')[1]
		,sChild.attrib.get('d')))
		# Create new threads
		cThread.start()
	    # Add threads to thread list
		threads.append(cThread)