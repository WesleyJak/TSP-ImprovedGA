class Graph():
    def __init__(self, nodes, complete):
        self.nodes = nodes
        self.complete = complete

    def get_num_nodes(self):
        return self.nodes
    
    def show(self):
        return


# Take a number of nodes and an option of complete or noncomplete. Generate the graph and return it.
# Either complete or noncomplete will be an adjacency matrix
def generate_graph(nodes, complete=True):
    graph = Graph(nodes, complete)
    return graph

