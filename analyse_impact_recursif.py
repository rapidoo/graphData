import sys
from py2neo import neo4j

graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")
datasets = graph_db.get_or_create_index(neo4j.Node, "Dataset")
recipes = graph_db.get_or_create_index(neo4j.Relationship, "Recipes")

def analyse_impacts():
	if len(sys.argv) > 1 :
		
		foundDatasets = datasets.get("dataset", sys.argv[1])
	
		startNode = foundDatasets[0]

		if (len(foundDatasets) == 1) & (foundDatasets[0] is not None) :
			analyse_impact(startNode)
 		else:
			print("script non trouve")

def analyse_impact(node):

	rels = list(graph_db.match(start_node=node, rel_type="recipe"))

	for rel in rels:
		print(rel.end_node.get_properties()['dataset'] + " via " + rel['recipe'])	
		analyse_impact(rel.end_node)

analyse_impacts()
