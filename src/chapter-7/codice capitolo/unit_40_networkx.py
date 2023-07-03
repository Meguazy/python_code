from miner import Miner
from nltk import download
from nltk import word_tokenize

import community
import networkx as nx
import pandas as pd
import re

download('punkt')
download('stopwords')

#----COSTRUZIONE E MANIPOLAZIONE DI UNA RETE-----
print("----COSTRUZIONE E MANIPOLAZIONE DI UNA RETE----")

"""Usiamo dei dati tratti da Wikipedia (https://en.wikipedia.org/wiki/List_of_countries_and_territories_by_number_of_land_borders) per costruire una rete di paesi e dei loro confini
Il grafo non e' orientato; non contiene cicli ne spigoli paralleli"""

borders_table = Miner.table_miner("https://en.wikipedia.org/wiki/List_of_countries_and_territories_by_number_of_land_borders", 0)

borders_df = pd.concat(pd.read_html(str(borders_table), index_col=0))
borders_df.index.rename('Country', inplace=True)
borders_df.to_csv("prova.csv")

#Creating the Graph
borders = nx.Graph()

#Adding the countries as nodes
countries_list = list(borders_df.index.values)
borders.add_nodes_from(countries_list)

for item in countries_list:
    near_countries: list = []
    check = True

    for str_split in str(borders_df.loc[str(item)][4]).split(":"):
        if check:
            near_countries.append(str_split)
            check = False
        else:    
            match = re.findall(r'\).* (A-Za-z *)?\s+(.*)$', str_split)
            if match:
                near_countries.append(match[0][1])

    for country in near_countries:
        country_refactor = re.sub(r' $','', re.sub(r'[^A-Za-z ]','',country))

        if country_refactor != 'nan':
            borders.add_edge(item, country_refactor)

#--Esplorazione e analisi di una rete--
print("\nFunzione 'len' che calcola il numero di nodi:")
print(len(borders))

print("\nLista dei nodi tramite la funzione 'nodes()':")
print(borders.nodes())
print("\nLista degli spigoli tramite la funzione 'edges()':")
print(borders.edges())
print("\nAccesso al dizionario dei nodi tramite l'attributo '_node':")
print(borders._node)
print("\nUsare lo slicing per stampare i primi 5 spigoli:")
print(list(borders.edges())[:5])

print("\nUso della funzione 'neighbors' per vedere gli stati confinanti con l'italia")
[print(item) for item in borders.neighbors("Italy")]

print("\nCalcolo il grado del nodo 'Italy' usando la funzione 'degree'")
print(borders.degree("Italy"))

print("\nRircerca del paese con il maggior numero di confini:")
degrees = pd.DataFrame(list(borders.degree()),
                       columns=('country','degree')).set_index('country')
print(degrees.sort_values("degree").tail(6))

"""Utilizzo la funzione clustering() per calcolare il coefficiente di clustering, ovvero il numero di spigoli presenti nel vicinato di un nodo A, in questo caso Italy"""
print("\nCoefficinete di clustering di 'Italy':")
print(nx.clustering(borders, "Italy"))

"""A partire da un grafo, le funzione connected_componests(), weakly_connected_componests() e strongly_connected_componests() restituiscono un generatore di liste dei rispottivi componenti connessi.
Potete usare il generatore in un'espressione di iterazione o convertirlo in una lista, grazie alla funzione list().
Un altro metodo utile e- il metodo 'subgraph(G,n), dove G e' il grafo che vogliamo ricercare mentre n e' la lista di nodi di cui vogliamo il sottografo. Anche per questo metodo esistono le
funzioni connected, weakly e strong."""
print("\nStampo i componenti connessi del grafo:")
print(list(nx.connected_components(borders)))

print("\nStampo la lunghezza degli elementi presenti nel sottografo connesso:")
[print(len(borders.subgraph(x))) for x in nx.connected_components(borders)]

"""Ci sono infine le funzioni di centralita' """
print("\nDegree centrality:")
print(nx.degree_centrality(borders))
print("\nIn degree centrality:")
#print(nx.in_degree_centrality(borders)) Non funziona perche' il grafo non e' orientato
print("\nOut degree centrality:")
#print(nx.out_degree_centrality(borders)) Non funziona perche' il grafo non e' orientato
print("\closeness centrality:")
print(nx.closeness_centrality(borders))
print("\nBetweenness centrality:")
print(nx.betweenness_centrality(borders))
print("\nEigenvalue centrality:")
print(nx.eigenvector_centrality(borders,max_iter=200))

#--GESTIONE DEGLI ATTRIBUTI--
"""Un grafo networkx, con tutti i suoi nodi, spigoli e attributi, e' implementato sotto forma di un dizionario. Un grafo ho un'iterfaccia a dizionarrio verso i suoi nodi.
Un nodo ha un'interfaccia a dizionario verso i suoi attributi. Potete quindi passare i nomi e i valori di attributi come parametri opzionali delle funzioni
add_node(), add_nodes_from(), add_edge() e add_edge_from()"""
#Attributi degli spigoli
borders["Italy"]["Austria"]["weight"] = 456.0
#Attributi dei nodi
borders._node["Italy"]["area"] = 357618
borders.add_node("Meguazyland", area=131)
"""Quando si usa il parametro data=True sulle funzioni nodes e edges, viene restituita una lista dei nodi o degli spigoli con gli attributi"""
print(borders._node["Italy"])

#--CRICCHE E STRUTTURA COMUNITARIA--
"""Le funzioni find_cliques() e isolates() individuano e isolano le cricche massimali (nodi a grado zero). find_cliques() non e' implementato per i grafi orientati."""
cricche = list(nx.find_cliques(borders))
print(cricche)
print(list(nx.isolates(borders)))
"""Utilizzando il modulo python 'community' si possono usare diversi metodi quali 'best_partition()' che impiega il metodo di Louvain e restituisce una partizione comunitaria.
La funzione modularity() restituisce, invece, la modularita' della partizione. Se e' troppo bassa (<< 0.5) allora significa che la rete non presenta una struttura comunitaria affidabile"""
partition = community.best_partition(borders)
print(partition)
print(community.modularity(partition,borders))

#--INPUT E OUTPUT--
"""
lista adiacente: read_adjlist(f), write_adjlist(G,f), no file extension
Lista degli spigoli: read_edgelist(f), write_edgelist(G,f), no file extension
GML: read_gml(f), write_fml(G,f), .gml
lista adiacente: read_graphml(f), write_graphml(G,f), .graphml
lista adiacente: read_pajek(f), write_pajek(G,f), .net

E' necessario scrivere i grafi su file per poi utilizzare altri strumenti di visualizzazione tipo Gephi
"""
with open("borders.graphml", "wb") as netfile:
    nx.write_pajek(borders,netfile)