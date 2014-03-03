import sys
from py2neo import neo4j

graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")
outputs = graph_db.get_or_create_index(neo4j.Relationship, "Outputs")
scripts = graph_db.get_or_create_index(neo4j.Node, "Scripts")


def analyse_impact():
	if len(sys.argv) > 1 :
		
		foundScripts = scripts.get("script", sys.argv[1])
	
		startNode = foundScripts[0]

		if (len(foundScripts) == 1) & (foundScripts[0] is not None) :
			rels = list(graph_db.match(start_node=startNode, rel_type="output"))

			for rel in rels:
				print(rel.end_node.get_properties()['script'] + " via " + rel['recipe'])
 		else:
			print("script non trouve")

analyse_impact()
