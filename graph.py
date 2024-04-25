import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt

# A tool for generating new graphs, processing existing graphs (as arrays), and visualizing graphs.
class Graph():
    def __init__(self, nodes, edges, graph_matrix=None):
        self.nodes = nodes
        self.edges = edges
        if graph_matrix is None:
            # if there is no new graph, generate one
            self.graph = nx.Graph()
            self.graph.add_nodes_from(range(nodes))
            for i in range(edges):
                 u, v = random.sample(range(nodes), 2)
                 weight = int(random.uniform(0, 100))
                 print(weight)
                 self.graph.add_edge(u, v, weight=weight)
            # make max range of 1000 if not exist (for unconnected weights)
            graph_arr = nx.to_numpy_array(self.graph)
            for index, weight in np.ndenumerate(graph_arr):
                if (index[0] != index[1]) and weight == 0:
                    graph_arr[index] = 1000
            self.solving_graph = nx.from_numpy_array(graph_arr)
        else:
            if len(graph_matrix) == nodes:
                self.graph = nx.from_numpy_array(np.array(graph_matrix))
                self.solving_graph = self.graph
            else:
                raise ValueError("Number of nodes not equal to dim of graph_matrix.")

    def get_num_nodes(self):
        return self.nodes
    
    def get_num_edges(self):
        return self.edges
    
    def get_graph(self):
        return nx.to_numpy_array(self.solving_graph)
    
    def print_graph(self):
        pos = nx.spring_layout(self.graph)
        plt.figure()
        edge_labels = {(u, v): f'{self.graph[u][v]["weight"]}' for u, v in self.graph.edges()}

        nx.draw(self.graph, pos)
        nx.draw_networkx_labels(self.graph, pos)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels)

        plt.axis('off')
        plt.show()

# Take a number of nodes and an option of complete or noncomplete. Generate the graph and return it.
# Either complete or incomplete will be an adjacency matrix
def generate_graph(nodes=0, edges=0, graph_matrix=None):
    graph = Graph(nodes, edges, graph_matrix)
    return graph

