
import math
import matplotlib.pyplot as plt
import argparse
import json
import networkx as nx
import queue


# Input/Output and Graph creation

def read_gml(file: str) -> nx.Graph:
    g = nx.read_gml(file)
    # ensure all nodes are strings
    mapping = {u: str(u) for u in g.nodes}
    g = nx.relabel_nodes(g, mapping)
    return g


def write_gml(g: nx.Graph, file: str) -> None:
    nx.write_gml(g, file)


def create_random_graph(n: int, c: float, seed: int) -> nx.Graph:
    # ensure n is positive
    if n <= 0:
        raise ValueError("n must be greater than zero")
    # calculate p
    p = c * math.log(n) / n
    # random graph
    g = nx.erdos_renyi_graph(n, p, seed)
    # convert to string
    mapping = {i: str(i) for i in range(n)}
    g = nx.relabel_nodes(g, mapping)
    # return
    return g


# Algorithms
# BFS
"HELPER FUNCTION: create a bfs from g using directed graph so parent and child"
"relationships are conserved"


def bfs(g: nx.Graph, root: str) -> nx.DiGraph:
    visited = set([root])
    q = queue.Queue()
    q.put(root)
    bfs_tree = nx.DiGraph()
    bfs_tree.add_node(root, distance=0)
    order = []

    while not q.empty():
        vertex = q.get()
        for neighbour in g[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                bfs_tree.add_edge(vertex, neighbour)
                bfs_tree.nodes[neighbour]["distance"] = bfs_tree.nodes[vertex]["distance"] + 1
                q.put(neighbour)

    return bfs_tree


def multi_bfs(g: nx.Graph, roots: list[str]) -> dict[str, nx.DiGraph]:
    return {r: bfs(g, r) for r in roots}

g = create_random_graph(10, 2, 2)  # 10 nodes, c=2, seed=42
print("Number of nodes:", g.number_of_nodes())
print("Number of edges:", g.number_of_edges())
print("Nodes:", g.nodes())
print("Edges:", g.edges())

root = "0"
bfs_tree = bfs(g, root)

print("Nodes in BFS tree:", list(bfs_tree.nodes()))
print("Edges in BFS tree:", list(bfs_tree.edges()))


# anaylze

def analyze_graph(g: nx.Graph) -> dict:
    analysis = {}
    # Connected Components
    components = list(nx.connected_components(g))
    analysis["num_components"] = len(components)
    # Cycle Detection
    analysis["cycle_detection"] = nx.find_cycle(g)
    # Isolated Nodes
    analysis["isolated_nodes"] = list(nx.isolates(g))
    # Graph Density
    analysis["density"] = nx.density(g)
    # Average shortest path length
    if nx.is_connected(g):
        analysis["average_shortest_path"] = nx.average_shortest_path_length(g)
    else:
        analysis["average_shortest_path"] = None
    return analysis

# Print Graph



# command line

def main():
    parser = argparse.ArgumentParser("Graph analysis")
    parser.add_argument("--input", type=str, help="input file")
    parser.add_argument("--output", type=str, help="output file")
    parser.add_argument("--create_random_graph", nargs=3, help="create random graph")
    parser.add_argument("--multi_BFS", nargs="+", help="bfs graph")
    parser.add_argument("--analyze", action="store_true", help="analyze graph")
    parser.add_argument("--plot", action="store_true", help="plot graph")



if __name__ == "__main__":
    main()









