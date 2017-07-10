from py2neo import neo4j
from py2neo import cypher
import sys
import io           
import csv
     

# set up authentication parameters
neo4j.authenticate("sfmgraphdb.cloudapp.net:7474", "fthornton67", "Onward_2014")
graph_db = neo4j.GraphDatabaseService('http://sfmgraphdb.cloudapp.net:7474/db/data/')

batch = neo4j.WriteBatch(graph_db)  # batch is linked to graph database
batchUpdate = neo4j.ReadBatch(graph_db)


cycleCount = 500
with open('zip_codes_states.csv','r') as csvfile:            
	
	lineReader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in lineReader:
		# get_or_create_indexes_node is one of many batch methods available
		batch.get_or_create_indexed_node("zip", "zip", row[0], { "zip_code" : row[0], "latitude":row[1], "longitude" : row[2] , "city" : row[3] , "state" : row[4] , "county" : row[5]}) 
		if(len(batch)>= cycleCount):                                               
			nodes = batch.submit()  # will return `Node` objects for the nodes created
			print("batch printed")
			batch.clear()
			