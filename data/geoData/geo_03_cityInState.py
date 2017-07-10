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

query = neo4j.CypherQuery(graph_db, "match (n:`state`) RETURN n")
for state in query.stream():                                
	print(state[0]['state_abbrv'])
	query2 = neo4j.CypherQuery(graph_db,"start  n=node(*) where n.state = '{0}' return n".format(state[0]['state_abbrv']))
	batch = neo4j.WriteBatch(graph_db)  # batch is linked to graph database
	for city in query2.stream():
		batch.create((city[0],"city in",state[0]))
	print("completed:{0}".format(state[0]['state_abbrv']))
	batch.submit()