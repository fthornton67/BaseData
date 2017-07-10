#!/usr/bin/env python

from pymongo import MongoClient 
import sys
import io
import csv               
from geojson import Point
import json
	
client = MongoClient('mongodb://localhost:27017/')
db = client['mean-dev'] 
#db.create_collection('mb_questions')
collection = db['phitr_airports']

for i in collection.find():
	currentPoint = Point((float(i["Longitude"]),  float(i["Latitude"]))) 
	i["loc"] = currentPoint
	collection.save(i)
	