import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

df = pd.read_csv('SDFB_people.csv')

for index, row in df.iterrows():
    id = row['SDFB Person ID']
    G.add_node(id)

print(G.number_of_nodes())

def addEdges(df):
  for index, row in df.iterrows():
      person1 = row['Person 1 ID']
      person2 = row['Person 2 ID']
      G.add_edge(person1, person2)

addEdges(pd.read_csv('SDFB_relationships_100000000_100020000.csv'))
addEdges(pd.read_csv('SDFB_relationships_100020001_100040000.csv'))
addEdges(pd.read_csv('SDFB_relationships_100040001_100060000.csv'))
addEdges(pd.read_csv('SDFB_relationships_100060001_100080000.csv'))
addEdges(pd.read_csv('SDFB_relationships_100080001_100100000.csv'))
addEdges(pd.read_csv('SDFB_relationships_100100001_100120000.csv'))
addEdges(pd.read_csv('SDFB_relationships_100120001_100140000.csv'))
addEdges(pd.read_csv('SDFB_relationships_100140001_100160000.csv'))
addEdges(pd.read_csv('SDFB_relationships_100160001_100180000.csv'))
addEdges(pd.read_csv('SDFB_relationships_greater_than_100180000.csv'))

print(G.number_of_edges())

# número de nós e arestas
print(f'Número de nós: {G.number_of_nodes()}')
print(f'Número de arestas: {G.number_of_edges()}')

# densidade da rede
print(f'Densidade da rede: {nx.density(G)}')

# diâmetro da rede
print(f'Diâmetro da rede: {nx.diameter(G)}')

# comprimento médio do caminho
print(f'Comprimento médio do caminho: {nx.average_shortest_path_length(G)}')