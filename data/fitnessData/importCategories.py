#!/usr/bin/env python

from pymongo import MongoClient 
import sys
import io
import csv
	
client = MongoClient('mongodb://localhost:27017/')
db = client['phitrme-dev'] 
#db.create_collection('mb_questions')
collection = db['phitr_categories']
                     
with open('categories.csv','rU') as csvfile:
	categories = csv.reader(csvfile, delimiter='\t', quotechar='"')   
	headers = categories.next()  
	counter = 0
	for c in categories:  
		o = dict()
		o['_id'] = counter;
		for field in headers: 
			print(field +': ' +c[headers.index(field)])     
			o[field] = c[headers.index(field)]
			print o
		collection.insert(o) 
		counter = counter+1
		