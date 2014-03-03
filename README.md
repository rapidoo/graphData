une fois que tu as installé Neo4j (2.0.1) - je n'avais travaillé que sur la 1.8 mais la 2.0 déchire grave (sans être rétrocompatible) - 
que tu l'as lancé 
> path_to_neo4j/bin/neo4j start

et que tu as installé py2neo (voir http://book.py2neo.org/en/latest/install/) :
> easy_install py2neo


Tu peux récupérer les 2 fichiers joints et les mettre dans data (en se basant sur l'archive que tu m'as envoyé):

Tu peux lancer le fichier:
> python linkscripts.py

qui va alimenter la base neo4j.

Il va mettre le nom des scripts sur les noeuds (grâces aux inputs et outputs trouvés dans les fichiers json sous recipes)

Il fait des relations node - output > node grâce à ses mêmes fichiers et mets sur les liens le fichier json qui fait le lien entre input et output.

Puis si tu lances par exemple:

> python analyse_impact.py BlocLR_Code_RSI_AFF_raw


ou l'argument est le nom du script (sans l'extension)


Ensuite ça doit te donner quelque chose comme ceci:

- RSI_AFFICHAGE via compute_RSI_AFFICHAGE

- RSI_AFFICHAGE_CLIC_raw via compute_RSI_AFFICHAGE_CLIC_raw
