import networkx as nx
import numpy as np
from qiskit import transpile
from qiskit_aer import AerSimulator

from final_score.ansatz_ham import build_ansatz, build_maxcut_hamiltonian
from final_score.qit_evolver import QITEvolver
from final_score.variables import GRAPH, LR, SHOTS


def compute_cut_size(graph, bitstring):
    """
    Get the cut size of the partition of ``graph`` described by the given
    ``bitstring``.
    """
    cut_sz = 0
    for u, v in graph.edges:
        if bitstring[u] != bitstring[v]:
            cut_sz += 1
    return cut_sz


def get_counts(shots, ansatz, graph, coef,lr=0.1):
    # Sample your optimized quantum state using Aer
    backend = AerSimulator()
    ham = build_maxcut_hamiltonian(graph,coef)
    qit_evolver = QITEvolver(ham, ansatz)
    qit_evolver.evolve(num_steps=40, lr=lr, verbose=True)
    optimized_state = ansatz.assign_parameters(qit_evolver.param_vals[-1])
    optimized_state.measure_all()
    counts = backend.run(optimized_state, shots=shots).result().get_counts()

    # Find the sampled bitstring with the largest cut value
    cut_vals = sorted(((bs, compute_cut_size(graph, bs)) for bs in counts), key=lambda t: t[1])
    best_bs = cut_vals[-1][0]

    # Now find the most likely MaxCut solution as sampled from your optimized state
    # We'll leave this part up to you!!!
    _most_likely_soln = ""

    return counts


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
    XS_brut, XS_balanced, XS_connected = get_classical_brute_force_scores(GRAPH)
    ansatz = build_ansatz(GRAPH)
    counts = get_counts(SHOTS, ansatz, GRAPH, LR)

    print("Base score: " + str(final_score(GRAPH, XS_brut, counts, SHOTS, ansatz)))
    print("Balanced score: " + str(final_score(GRAPH, XS_balanced, counts, SHOTS, ansatz)))
    print("Connected score: " + str(final_score(GRAPH, XS_connected, counts, SHOTS, ansatz)))
