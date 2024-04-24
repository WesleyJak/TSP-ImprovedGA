import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt

class Graph():
    def __init__(self, nodes, complete, graph_matrix=None):
        self.nodes = nodes
        self.complete = complete
        if graph_matrix is None:
            # if there is no new graph, generate one
            return
        else:
            if len(graph_matrix) == nodes:
                self.graph = nx.from_numpy_array(np.array(graph_matrix))
            else:
                raise ValueError("Number of nodes not equal to dim of graph_matrix.")

    def get_num_nodes(self):
        return self.nodes
    
    def print_graph(self):
        nx.draw(self.graph)
        plt.show()

# Take a number of nodes and an option of complete or noncomplete. Generate the graph and return it.
# Either complete or noncomplete will be an adjacency matrix
def generate_graph(nodes=0, complete=True, graph_matrix=None):
    graph = Graph(nodes, complete, graph_matrix)
    return graph

