
import math
import matplotlib.pyplot as plt
import argparse
import json
import networkx as nx
import queue


# Input/Output and Graph creation

def read_gml(file: str) -> nx.Graph:
    g = nx.read_gml(file)
    # make sure all nodes are strings
    mapping = {u: str(u) for u in g.nodes}
    g = nx.relabel_nodes(g, mapping)
    return g


def write_gml(g: nx.Graph, file: str) -> None:
    nx.write_gml(g, file)


def create_random_graph(n: int, c: float, seed: int) -> nx.Graph:
    # make sure n is positive
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

# Helper function for multi_bfs

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


# multi_BFS
def multi_bfs(g: nx.Graph, roots: list[str]) -> dict[str, nx.DiGraph]:
    return {r: bfs(g, r) for r in roots}


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


# Plot Graph
def plot_graph(g: nx.Graph, bfs_trees: dict[str, nx.DiGraph]= None):
    pos = nx.spring_layout(g, seed=42)
    colors = ["red", "green", "orange", "purple"]
    # will make a new graph for each bfs each with a different color
    for i, (root, tree) in enumerate(bfs_trees.items()):
        nx.draw(
            g,
            # keep edges in the same position as the original edges
            pos=pos,
            with_labels=True,
            node_color="lightblue",
            edge_color="grey",
            node_size=500,
            font_size=10,
        )
        edges = list(nx.edges(tree))
        nx.draw_networkx_edges(
            g,
            # keep edges in the same position
            pos=pos,
            edgelist=edges,
            # just incase there's more than 4 inputs
            edge_color=colors[i % len(colors)],
            width=2,
            label=f"BFS from {root}"
        )
        plt.legend()
        plt.show()


# command line

def main():
    parser = argparse.ArgumentParser("Graph analysis")
    parser.add_argument("--input", type=str, help="input file")
    parser.add_argument("--output", type=str, help="output file")
    parser.add_argument("--create_random_graph", nargs=3, help="create random graph")
    parser.add_argument("--multi_BFS", nargs="+", help="bfs graph")
    parser.add_argument("--analyze", action="store_true", help="analyze graph")
    parser.add_argument("--plot", action="store_true", help="plot graph")

    args = parser.parse_args()

    if args.create_random_graph:
        # error handling for # of arguments in args=3
        n, c, seed = (int(args.create_random_graph[0]),
                      float(args.create_random_graph[1]), int(args.create_random_graph[2]))
        g = create_random_graph(n, c, seed)
    elif args.input:
        g = read_gml(args.input)
    else:
        print("Error: Must provide input file or create random graph")
        return

    bfs_trees = None
    if args.multi_BFS:
        bfs_trees = multi_bfs(g, args.multi_BFS)

    if args.analyze:
        analysis = analyze_graph(g)
        print(json.dumps(analysis, indent=2))

    if args.plot:
        plot_graph(g, bfs_trees)

    if args.output:
        write_gml(g, args.output)


if __name__ == "__main__":
    main()









