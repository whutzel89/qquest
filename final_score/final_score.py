from typing import List

import networkx as nx
import numpy as np
from qiskit import transpile

from final_score.variables import ANSATZ, COUNTS, GRAPH, SHOTS


def get_classical_brute_force_scores(graph):
    G = graph
    n = len(G.nodes())
    w = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            temp = G.get_edge_data(i, j, default=0)
            if temp != 0:
                w[i, j] = 1.0

    best_cost_brute = 0
    best_cost_balanced = 0
    best_cost_connected = 0

    for b in range(2**n):
        x = [int(t) for t in reversed(list(bin(b)[2:].zfill(n)))]

        # Create subgraphs based on the partition
        subgraph0 = G.subgraph([i for i, val in enumerate(x) if val == 0])
        subgraph1 = G.subgraph([i for i, val in enumerate(x) if val == 1])

        bs = "".join(str(i) for i in x)

        # Check if subgraphs are not empty
        if len(subgraph0.nodes) > 0 and len(subgraph1.nodes) > 0:
            cost = 0
            for i in range(n):
                for j in range(n):
                    cost = cost + w[i, j] * x[i] * (1 - x[j])
            if best_cost_brute < cost:
                best_cost_brute = cost
                XS_brut = []
            if best_cost_brute == cost:
                XS_brut.append(bs)

            outstr = "case = " + str(x) + " cost = " + str(cost)

            if (len(subgraph1.nodes) - len(subgraph0.nodes)) ** 2 <= 1:
                outstr += " balanced"
                if best_cost_balanced < cost:
                    best_cost_balanced = cost
                    XS_balanced = []
                if best_cost_balanced == cost:
                    XS_balanced.append(bs)

            if nx.is_connected(subgraph0) and nx.is_connected(subgraph1):
                outstr += " connected"
                if best_cost_connected < cost:
                    best_cost_connected = cost
                    XS_connected = []
                if best_cost_connected == cost:
                    XS_connected.append(bs)

    return XS_brut, XS_balanced, XS_connected


def final_score(graph, XS_brut, counts, shots, ansatz):
    sum_counts = 0
    for bs in counts:
        if bs in XS_brut:
            sum_counts += counts[bs]

    transpiled_ansatz = transpile(ansatz, basis_gates=["cx", "rz", "sx", "x"])
    cx_count = transpiled_ansatz.count_ops()["cx"]
    score = (4 * 2 * graph.number_of_edges()) / (4 * 2 * graph.number_of_edges() + cx_count) * sum_counts / shots

    return np.round(score, 5)


def main():
    graph = GRAPH
    XS_brut, XS_balanced, XS_connected = get_classical_brute_force_scores(graph)
    counts = COUNTS
    shots = SHOTS
    ansatz = ANSATZ

    print("Base score: " + str(final_score(graph, XS_brut, counts, shots, ansatz)))
    print("Balanced score: " + str(final_score(graph, XS_balanced, counts, shots, ansatz)))
    print("Connected score: " + str(final_score(graph, XS_connected, counts, shots, ansatz)))
