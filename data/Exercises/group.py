#!/usr/bin/python
import os
import sys
from bs4 import BeautifulSoup  
from pymongo import MongoClient  
from bson.son import SON

reload(sys)                                              
sys.setdefaultencoding("utf-8")
client = MongoClient('localhost', 27017) 
db = client.fitness                     
collection = db['exercises']    
                        
for d in collection.find({"Action" : 'VIDEO' }):
	print(d)

print(collection.aggregate([
	{ '$group' : { '_id' :"$muscleStressType",'total':{'$sum': "$count"}}}     
	]))