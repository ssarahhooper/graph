
import math
import matplotlib.pyplot as plt
import argparse
import json
import networkx as nx


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
    # relabel

    # return


# Algorithms









