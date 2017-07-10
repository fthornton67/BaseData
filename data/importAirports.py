#!/usr/bin/env python

from pymongo import MongoClient 
import sys
import io
import csv               
from geojson import Point
import json
	
client = MongoClient('mongodb://localhost:27017/')
db = client['phitrme-dev'] 
#db.create_collection('mb_questions')
collection = db['phitr_airports']
                     
with open('airports_.csv','rU') as csvfile:
	categories = csv.reader(csvfile, delimiter=',', quotechar='"')   
	headers = categories.next()  
	counter = 0
	for c in categories:  
		o = dict()
		o['_id'] = counter;
		for field in headers: 
		   # print(field +': ' +c[headers.index(field)])     
			o[field] = unicode(c[headers.index(field)], errors='replace')
		   # print o
		collection.insert(o) 
		counter = counter+1      
		
		
for i in collection.find():
	currentPoint = Point((float(i["Longitude"]),  float(i["Latitude"]))) 
	i["loc"] = currentPoint
	collection.save(i)
