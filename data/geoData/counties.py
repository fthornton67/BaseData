import fnmatch
import os
import csv    
import sys    
import json
import http.client
import urllib.parse
import xml        
from xml.etree import ElementTree as ET                        


rootPath = '.'
pattern = 'US*.csv'   
                          
def postCurrentItem(jsonLine):
	connection = http.client.HTTPSConnection('api.parse.com', 443)
	connection.connect()         
	connection.request('POST', '/1/classes/sfm_Geo_USCities', json.dumps(json.loads(jsonLine)), {
           "X-Parse-Application-Id": "orOInbx3WpwNjlZE0op7lv7HSeFA4tlsCENATg3U",
           "X-Parse-REST-API-Key": "tqGKF4vtGQHQ3y5f99EVWgrtBlWEd9Em9uzhwc4q",
           "Content-Type": "application/json"
         })                  
	print(connection.getresponse().read())

def createJsonLine(element):
	for coord in element.get('d').split(' '):
		print(coord)
		

import xml.etree.ElementTree as ET
tree = ET.parse('counties.xml')
root = tree.getroot() 
for child in root.findall('{http://www.w3.org/2000/svg}g'):
	for sChild in child:  
		createJsonLine(sChild)
		