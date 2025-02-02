# other graphs candidates to check

import random

import networkx as nx


# -> Cycle Graph C8
def cycle_graph_c8():
    G = nx.cycle_graph(8)
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=500)
    return G


# Path Graph P16
def path_graph_p16():
    G = nx.path_graph(16)
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color="lightgreen", edge_color="gray", node_size=300)
    return G


# -> Complete Bipartite Graph K8,8
def complete_bipartite_graph_k88():
    G = nx.complete_bipartite_graph(8, 8)
    pos = nx.bipartite_layout(G, nodes=range(8))
    nx.draw(
        G, pos, with_labels=True, node_color=["lightcoral"] * 8 + ["lightblue"] * 8, edge_color="gray", node_size=300
    )
    return G


# -> Complete Bipartite Graph K8,8
def complete_bipartite_graph_k_nn(n):
    G = nx.complete_bipartite_graph(n, n)
    pos = nx.bipartite_layout(G, nodes=range(n))
    nx.draw(
        G, pos, with_labels=True, node_color=["lightcoral"] * n + ["lightblue"] * n, edge_color="gray", node_size=300
    )
    return G


# Star Graph S16
def star_graph_s16():
    G = nx.star_graph(16)
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color="gold", edge_color="gray", node_size=300)
    return G


# Grid Graph 8x4
def grid_graph_8x4():
    G = nx.grid_graph(dim=[8, 4])
    pos = {node: node for node in G.nodes()}
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=300)
    return G


# Grid Graph 8x4
def grid_graph_nxm(n, m):
    G = nx.grid_graph(dim=[n, m])
    pos = {node: node for node in G.nodes()}
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=300)
    return G


# -> 4-Regular Graph with 8 Vertices
def regular_graph_4_8():
    G = nx.random_regular_graph(d=4, n=8, seed=42)
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightgreen", edge_color="gray", node_size=500)
    return G


# -> Cubic (3-Regular) Graph with 16 Vertices
def cubic_graph_3_16():
    G = nx.random_regular_graph(d=3, n=16, seed=42)
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color="lightcoral", edge_color="gray", node_size=300)
    return G


# Disjoint Union of Four C4 Cycles
def disjoint_union_c4():
    cycles = [nx.cycle_graph(4) for _ in range(4)]
    G = nx.disjoint_union_all(cycles)
    pos = {}
    shift_x = 0
    for component in nx.connected_components(G):
        subgraph = G.subgraph(component)
        pos_sub = nx.circular_layout(subgraph, scale=1, center=(shift_x, 0))
        pos.update(pos_sub)
        shift_x += 3
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=300)
    return G


# Complete Bipartite Graph K16,16
def complete_bipartite_graph_k1616():
    G = nx.complete_bipartite_graph(16, 16)
    pos = nx.bipartite_layout(G, nodes=range(16))
    nx.draw(
        G, pos, with_labels=False, node_color=["lightcoral"] * 16 + ["lightblue"] * 16, edge_color="gray", node_size=100
    )
    return G


# 5-Dimensional Hypercube Graph Q5
def hypercube_graph_q5():
    G = nx.hypercube_graph(5)
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=False, node_color="lightgreen", edge_color="gray", node_size=200)
    return G


# Tree Graph with 8 Vertices
def tree_graph_8():
    G = nx.balanced_tree(r=2, h=2)
    G.add_edge(6, 7)
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=300)
    return G


# Wheel Graph W16
def wheel_graph_w16():
    G = nx.wheel_graph(16)
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightcoral", edge_color="gray", node_size=300)
    return G


# -> Random Connected Graph with 16 Vertices
def random_connected_graph_16(p=0.15):
    # n, p = 16, 0.25
    n = 16
    while True:
        G = nx.erdos_renyi_graph(n, p, seed=random.randint(1, 10000))
        if nx.is_connected(G):
            break
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=False, node_color="lightgreen", edge_color="gray", node_size=100)
    return G


# Expander Graph with 32 Vertices
def expander_graph_32():
    G = nx.random_regular_graph(4, 32, seed=42)
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=False, node_color="lightblue", edge_color="gray", node_size=100)
    return G


# -> Expander Graph with n Vertices
def expander_graph_n(n):
    G = nx.random_regular_graph(4, n, seed=42)
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=False, node_color="lightblue", edge_color="gray", node_size=100)
    return G


# Planar Connected Graph with 16 Vertices
def planar_connected_graph_16():
    G = nx.grid_graph(dim=[8, 2])
    G = nx.convert_node_labels_to_integers(G)
    additional_edges = [
        (0, 9),
        (1, 10),
        (2, 11),
        (3, 12),
        (4, 13),
        (5, 14),
        (6, 15),
        (7, 15),
        (8, 7),
    ]  # , (6, 15), (14, 1), (1, 13), (10, 9), (0, 10), (12, 2), (8, 7)]
    G.add_edges_from([e for e in additional_edges if e[0] < 16 and e[1] < 16])
    assert nx.check_planarity(G)[0], "Graph is not planar."
    pos = {node: (node // 2, node % 2) for node in G.nodes()}
    nx.draw(G, pos, with_labels=False, node_color="lightcoral", edge_color="gray", node_size=100)
    return G
