# PERCURSO DFS EM GRAFO SEGUNDO O ALGORITMO DE HOPCROFT E TARJAN
import networkx as nx
import matplotlib.pyplot as plt

class GrafoDFS:
    def __init__(self, grafo):
        self.grafo = grafo
        self.node_visited = {node: 0 for node in grafo.nodes} # 0 => vértice não visitado; caso contrário, vértice descoberto ou visitado
        self.edges_visited = [] # lista com as arestas visitadas

    def dfs(self, node, edges, i):
        self.node_visited[node] = i
        i += 1
        for neighbor in self.grafo.neighbors(node):
            if self.node_visited[neighbor] == 0:
                print(f'({node}, {neighbor})')
                edges.append((node, neighbor))
                self.dfs(neighbor, edges, i)

    def percorrer_dfs(self):
        i = 1
        for node in self.grafo.nodes:
            if self.node_visited[node] == 0:
                self.dfs(node, self.edges_visited, i)

# grafo com subgrafos não conectados
grafo = nx.Graph()
grafo.add_edges_from([(0, 1), (1, 2), (2, 0), (2, 3), (1, 4), (5, 6), (6, 7), (7, 9), (6, 8)])

# criar e percorrer GrafoDFS
print('Percurso DFS:')
grafo_dfs = GrafoDFS(grafo)
grafo_dfs.percorrer_dfs()

# imprimir as arestas visitadas
print('Arestas visitadas:', grafo_dfs.edges_visited)
print()

# desenhar o grafo com as ordem que as arestas foram visitadas
edges_order = {(edge[0], edge[1]): j for j, edge in enumerate(grafo_dfs.edges_visited, start=1)}
nx.draw(grafo, pos=nx.spring_layout(grafo, seed=42), with_labels=True, node_color='skyblue', font_color='black')
nx.draw_networkx_edge_labels(grafo, pos=nx.spring_layout(grafo, seed=42), edge_labels=edges_order)
plt.show()