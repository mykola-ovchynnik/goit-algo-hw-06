from task_1 import G, show_graph

weighted_edges = [
    ("Station A", "Station B", 1),
    ("Station A", "Station C", 2),
    ("Station B", "Station D", 4),
    ("Station C", "Station D", 1),
    ("Station D", "Station E", 3),
    ("Station E", "Station F", 2),
    ("Station F", "Station G", 1),
    ("Station G", "Station H", 5),
    ("Station H", "Station A", 2),
    ("Station B", "Station G", 3),
]
G.add_weighted_edges_from(weighted_edges)


def dijkstra(graph, start):
    distances = {vertex: float("infinity") for vertex in graph.nodes}
    distances[start] = 0
    unvisited = list(graph.nodes)
    visited = []
    shortest_paths = {vertex: [] for vertex in graph.nodes}
    shortest_paths[start] = [start]

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float("infinity"):
            break

        for neighbor, attributes in graph[current_vertex].items():
            weight = attributes["weight"]
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_paths[neighbor] = shortest_paths[current_vertex] + [neighbor]

        visited.append(current_vertex)
        unvisited.remove(current_vertex)

    return distances, shortest_paths


if __name__ == "__main__":
    all_shortest_paths = {}
    all_shortest_path_lengths = {}
    for node in G.nodes:
        distances, paths = dijkstra(G, node)
        all_shortest_paths[node] = paths
        all_shortest_path_lengths[node] = distances

    print("Shortest paths:")
    for start_node, paths in all_shortest_paths.items():
        print(f"From {start_node}:")
        for target, path in paths.items():
            print(f"  To {target}: {path}")
        print()

    print("Shortest path lengths:")
    for start_node, lengths in all_shortest_path_lengths.items():
        print(f"From {start_node}:")
        for target, length in lengths.items():
            print(f"  To {target}: {length}")
        print()

    show_graph(G)
