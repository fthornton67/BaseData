from py2neo import neo4j
import sys
import io
import csv

# set up authentication parameters
neo4j.authenticate("sfmgraphdb.cloudapp.net:7474", "fthornton67", "Onward_2014")
graph_db = neo4j.GraphDatabaseService('http://sfmgraphdb.cloudapp.net:7474/db/data/')

batch = neo4j.WriteBatch(graph_db)  # batch is linked to graph database

with open('States.csv','r') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in spamreader:
		# get_or_create_indexes_node is one of many batch methods available
		batch.get_or_create_indexed_node("state", "state_name", row[1], { "state_name": row[0],"state_abbrv":row[1],"state_capital":row[2],"most_populated":row[3],"population":row[4],"square_miles":row[5],"time_zone1":row[6],"time_zone2":row[7],"dst":row[8]})

nodes = batch.submit()  # will return `Node` objects for the nodes created

for node in nodes:
	node.add_labels('state')