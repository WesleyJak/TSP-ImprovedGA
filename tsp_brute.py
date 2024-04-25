# Given a generated graph, solve the graph and output the minimum weight travel.
def tsp_brute(graph, start = 0):
    n = len(graph)
    visited = [False] * n
    visited[start] = True
    shortest_path = None
    shortest_distance = float('inf')

    def _find_route(current_node, current_path, current_distance):
        nonlocal shortest_path, shortest_distance

        if len(current_path) == n:
            current_distance += graph[current_path[-1], start]
            if current_distance < shortest_distance:
                shortest_distance = current_distance
                shortest_path = current_path[:]
            return

        for next_node in range(n):
            if not visited[next_node]:
                visited[next_node] = True
                _find_route(next_node, current_path + [next_node], current_distance + graph[current_node, next_node])
                visited[next_node] = False

    _find_route(start, [start], 0)
    return shortest_path, shortest_distance


