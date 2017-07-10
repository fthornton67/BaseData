#!/usr/bin/env python
import os
import sys
from bs4 import BeautifulSoup  
from pymongo import MongoClient
            
client = MongoClient('mongodb://localhost:27017/')
db = client['phitrme-dev']                    
collection = db['phitr_exercises']   

print(collection)            

def updateVideo():            
	print("*******************update")
	u =  db['phitr_exercises'].update({'Action' :'VIDEO'},{ '$unset' : {'Action':""}},upsert=True,multi=True)
	print(u)  
	print("******************results")
	print(collection.find({'Action':'VIDEO'}).count())
		
def getMuscleStressType(muscleGroup):
	results = []
	groupType = muscleGroup.find_all('i')[0].next_element.string.split(':')[0].split(' ')[1] 
	return groupType.lower()
	
def getMuscleGroups(muscleGroup):
	results = []
	groupType = muscleGroup[0].next_element.string.split(':')[0].split(' ')[1] 
	groupVal = muscleGroup[0].next_element.string.split(':')[1] 
	#print('groupType') 
	if len(groupVal) != 0:
		#group val was a string
		results.append(groupVal)
	else:
		# get an array of vals from next element
		groupVal = muscleGroup[0].next_element.next_element.next_element.lower().replace('(','').replace(')','').replace('and',',')
		for s in groupVal.split(','):
			s = s.strip()
			results.append(s)
	#print(results)     
	return results
	

reload(sys) 
sys.setdefaultencoding("utf-8")
           
muscleGroups = dict()                   
path ="./exercise"   
def importExercises():
	#db['mean-dev'].drop()
	for root, dirs, files in os.walk(path):
		for name in files:            
			print(name)
			if name.endswith((".html", ".htm")):
				p=os.path.join(root,name)
				with open(p) as f:
					content = f.readlines()
					page = BeautifulSoup(str(content).replace('\\r\\n','').replace('\\t','').replace('\', \'',''))
					#print(page.table.prettify())
					pageSpans = page.table.find_all('span')
					#for s in pageSpans:
					#	print(s.string)
					tableSpans = page.table.find_all('span') 
					exercise = {} 
					
					for tS in tableSpans:   
						if tS['style'] == 'font-size:18px; color:black':
						    exercise['title'] = tS.string 
						
						if tS['style'] == 'font-size:14px; color:#5a5ab5':
							exercise[str(tS.string)] = str(tS.next_sibling.next_sibling.next_sibling.next_sibling.string)
							#if tS['style'] == 'font-size:11px; color:#000000':
							#print("\t\t" + str(tS.string))  
					if len(page.table.find_all('i')) > 0:
						#print(page.table.find_all('i')[0])
						exercise['muscleGroups'] = getMuscleGroups(page.table.find_all('i'))
						exercise['muscleStressType']  = getMuscleStressType(page.table)
							
					exercise['count'] = 1
					exercise['index'] = name
					collection.insert(exercise)
print('Begin Import Exercises')
importExercises()
print('Begin update videos')
updateVideo()