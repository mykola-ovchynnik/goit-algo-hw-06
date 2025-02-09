import networkx as nx
from collections import deque
from task_1 import G, show_graph


def dfs(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


if __name__ == "__main__":
    start_node = "Station A"
    end_node = "Station G"

    dfs_paths = list(dfs(G, start_node, end_node))
    bfs_paths = list(bfs(G, start_node, end_node))

    print("DFS paths from {} to {}:".format(start_node, end_node))
    for path in dfs_paths:
        print(path)

    print("\nBFS paths from {} to {}:".format(start_node, end_node))
    for path in bfs_paths:
        print(path)

    show_graph(G)
