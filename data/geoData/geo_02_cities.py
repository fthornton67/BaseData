from py2neo import neo4j
import sys
import io           
import csv
# set up authentication parameters

neo4j.authenticate("sfmgraphdb.cloudapp.net:7474", "fthornton67", "Onward_2014")                                     
graph_db = neo4j.GraphDatabaseService('http://sfmgraphdb.cloudapp.net:7474/db/data/')
                   
#with open('USCities.csv','r') as csvfile:
#	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
#	for row in reader:
#		with open("state_" + row[2]+".csv", "a") as stateFile:
#			stateFile.write("{0},{1},{2},{3},{4}\n".format(row[0],row[1],row[2],row[3],row[4]))

query = neo4j.CypherQuery(graph_db, "match (n:state) RETURN n")

for record in query.stream():
		print (record[0]['state_name'] + "  " + record[0]['state_abbrv'])
		batch = neo4j.WriteBatch(graph_db)  # batch is linked to graph database
		with open('state/state_'+record[0]['state_abbrv']+'.csv','r') as csvfile:
			reader = csv.reader(csvfile, delimiter=',', quotechar='"')
			for row in reader:
				batch.get_or_create_indexed_node("City", "city_num", row[0], { "city_name": row[1],
				"city_no": row[0], "state": row[2] ,"latitude":row[3],"longitude":row[4]
			})
			nodes = batch.submit()  # will return `Node` objects for the nodes created
			print(record[0]['state_abbrv']) 
			queryString = "match (n) where has(n.state) set n:city:geo".format(record[0]['state_abbrv'])
			result = neo4j.CypherQuery(graph_db, queryString).execute()  
			print(len(nodes))