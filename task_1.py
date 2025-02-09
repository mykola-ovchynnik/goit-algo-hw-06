import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(
    [
        "Station A",
        "Station B",
        "Station C",
        "Station D",
        "Station E",
        "Station F",
        "Station G",
        "Station H",
    ]
)

edges = [
    ("Station A", "Station B"),
    ("Station A", "Station C"),
    ("Station B", "Station D"),
    ("Station C", "Station D"),
    ("Station D", "Station E"),
    ("Station E", "Station F"),
    ("Station F", "Station G"),
    ("Station G", "Station H"),
    ("Station H", "Station A"),
    ("Station B", "Station G"),
]
G.add_edges_from(edges)


def show_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color="lightblue", edge_color="gray")
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Transport Network")
    plt.show()


if __name__ == "__main__":
    print("Nodes:", G.number_of_nodes())
    print("Edges:", G.number_of_edges())
    print("Node connections:")
    for node, degree in G.degree():
        print(f"{node}: {degree}")

    show_graph(G)
