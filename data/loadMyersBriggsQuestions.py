#!/usr/bin/env python

from pymongo import MongoClient
                         
fRead = open('myersBriggsQuestions.txt','r')   

client = MongoClient('mongodb://localhost:27017/')
db = client['mean-dev'] 
#db.create_collection('mb_questions')
collection = db['mb_questions']

for line in fRead:     
	if len(line.strip()) > 0:  
		question = { 'question': line }
		collection.insert(question)  
		
		
		