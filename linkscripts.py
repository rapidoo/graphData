import os
import json
from py2neo import neo4j

path = './recipes'
graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")
scripts = graph_db.get_or_create_index(neo4j.Node, "Scripts")
outputs = graph_db.get_or_create_index(neo4j.Relationship, "Outputs")

def storeScriptsIntoNeo4j():
	graph_db.clear()

	for filename in os.listdir(path):
		with open(path + "/" + filename) as data_file: 
			name, extension = os.path.splitext(filename)
			if(extension == ".json"):
				data = json.load(data_file)
				data_file.close()
				for input in data['inputs']:
					inputNode = scripts.get_or_create("script", input, {"script": input})
					for output in data['outputs']:
						outputNode = scripts.get_or_create("script", output, {"script": output})
						outputs.create_if_none("recipe",name, (inputNode,"output",outputNode))
					
storeScriptsIntoNeo4j();
