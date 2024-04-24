from graph import generate_graph

# This is for size graph of 4
example_matrix = [
        [0, 10, 20, 15],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
        ]

# Use the example matrix to generate a graph and show it.
example_graph1 = generate_graph(nodes=4, edges=12, graph_matrix=example_matrix)
example_graph1.print_graph()

# Print example_graph1, showing the graph in matrix array form.
print(example_graph1.get_graph())

# Generate a random incomplete matrix and show it.
example_graph2 = generate_graph(nodes=8, edges=20)
example_graph2.print_graph()

# Print example_graph2, showing the graph in matrix array form.
print(example_graph2.get_graph())
