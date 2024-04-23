from graph import generate_graph

# Given a generated graph, solve the graph and output the minimum weight travel.
class TSP_Solve():
    def __init__(self, graph):
        self.graph = graph

    def solve(self):
        return

# This is for size graph of 4
example_matrix = [
        [0, 10, 20, 15],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
        ]

new_graph = generate_graph(nodes=4, complete=True, graph_matrix=example_matrix)
new_graph.get_num_nodes()
