import sys
import csv

with open('USCities.csv','r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in reader:
		with open("state/state_" + row[2]+".csv", "a") as stateFile:
			stateFile.write("{0},\"{1}\",{2},{3},{4}\n".format(row[0],row[1],row[2],row[3],row[4]))
