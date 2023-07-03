import community
import networkx as nx
import pandas as pd

with open("soc-Epinions1.txt", "r") as file:
    graph = nx.read_edgelist(file)

partition = pd.Series(community.best_partition(graph))
top10 = partition.value_counts().index[9]

subgraph = partition[partition == top10].index.values.astype('str')
F = graph.subgraph(subgraph)
(F)

df = pd.DataFrame()
df["degree"] = pd.Series(nx.degree_centrality(F))
df["closeness"] = pd.Series(nx.closeness_centrality(F))
df["betweenness"] = pd.Series(nx.betweenness_centrality(F))
df["eigenvalue"] = pd.Series(nx.eigenvector_centrality(F))
df["cluster"] = pd.Series(nx.clustering(F))

print(df.corr("pearson"))