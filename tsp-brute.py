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

given_graph = generate_graph(nodes=4, edges=12, graph_matrix=example_matrix)
#given_graph.print_graph()

new_graph = generate_graph(nodes=8, edges=20)
new_graph.print_graph()