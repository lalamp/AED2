import networkx as nx
import matplotlib.pyplot as plt

class GrafoDFS:
    def __init__(self, grafo):
        self.grafo = grafo
        self.nodes_color = {node: 'white' for node in grafo.nodes}
        self.d = {} # registra quando cada vértice é descoberto
        self.f = {} # registra quando termina a lista de adjacência de cada vértice
        self.p = {} # dicionário que associa a cada vértice seu pai, ou seja, de onde partiu o caminho para esse vértice
        self.edges_visited = []

    def dfs(self, node, time):
        self.nodes_color[node] = 'gray'
        time += 1
        self.d[node] = time
        print(f'\nDescoberto({node}): {self.d[node]}')
        print('Cores dos nós:', self.nodes_color)
        self.desenhar_grafo()

        for neighbor in self.grafo.neighbors(node):
            if self.nodes_color[neighbor] == 'white':
                print(f'\nAresta visitada: ({node}, {neighbor})')
                self.edges_visited.append((node, neighbor))
                self.dfs(neighbor, time)

        self.nodes_color[node] = 'black'
        self.f[node] = time
        time += 1
        print(f'\nFinalizado({node}): {self.f[node]}')
        print('Cores dos nós:', self.nodes_color)
        self.desenhar_grafo()

    def percorrer_dfs(self):
        time = 0
        for node in self.grafo.nodes:
            if self.nodes_color[node] == 'white':
                self.p[node] = None
                print('Cores dos nós:', self.nodes_color)
                self.desenhar_grafo()
                self.dfs(node, time)

    def desenhar_grafo(self):
        colors = [self.nodes_color[node] for node in self.grafo.nodes]
        edges_order = {(edge[0], edge[1]): j for j, edge in enumerate(grafo_dfs.edges_visited, start=1)}
        nx.draw(self.grafo, pos=nx.spring_layout(grafo, seed=42), with_labels=True, node_color=colors, font_color='red', cmap=plt.cm.Blues)
        nx.draw_networkx_edge_labels(grafo, pos=nx.spring_layout(grafo, seed=42), edge_labels=edges_order)
        plt.show()

# grafo com subgrafos não conectados
grafo = nx.Graph()
grafo.add_edges_from([(0, 1), (1, 2), (2, 0), (2, 3), (1, 4), (5, 6), (6, 7), (7, 9), (6, 8)])

# criar e percorrer GrafoDFS
print('Percurso DFS:')
grafo_dfs = GrafoDFS(grafo)
grafo_dfs.percorrer_dfs()

# imprimir resultados finais
print('\nCores dos nós:', grafo_dfs.nodes_color)
print('Arestas visitadas:', grafo_dfs.edges_visited)
print('Grafo final: ')
grafo_dfs.desenhar_grafo()