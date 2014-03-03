import os
import json
from py2neo import neo4j

path = './recipes'
graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")
datasets = graph_db.get_or_create_index(neo4j.Node, "Dataset")
recipes = graph_db.get_or_create_index(neo4j.Relationship, "Recipes")

def storeScriptsIntoNeo4j():
	graph_db.clear()

	for filename in os.listdir(path):
		with open(path + "/" + filename) as data_file: 
			name, extension = os.path.splitext(filename)
			if(extension == ".json"):
				data = json.load(data_file)
				data_file.close()
				for input in data['inputs']:
					inputNode = datasets.get_or_create("dataset", input, {"dataset": input})
					for output in data['outputs']:
						outputNode = datasets.get_or_create("dataset", output, {"dataset": output})
						recipes.create_if_none("recipe",name, (inputNode,"recipe",outputNode))
					
storeScriptsIntoNeo4j();
