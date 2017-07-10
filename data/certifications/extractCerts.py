#!/usr/bin/env python     
from pymongo import MongoClient 
import sys
import io
import csv               
from geojson import Point
import json          

import xml.etree.ElementTree as ET
tree = ET.parse('certs.html')
root = tree.getroot()      

	
	
client = MongoClient('mongodb://localhost:27017/')
db = client['phitr-dev'] 
collection = db['phitr_certs']

reload(sys)  
sys.setdefaultencoding('utf8')

for label in root.iter('label'):
	o = dict()
	o['title'] = label.text
	collection.insert(o)
collection.save()
	
