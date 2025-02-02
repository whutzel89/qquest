import networkx as nx
from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector
from qiskit.quantum_info import SparsePauliOp


def build_maxcut_hamiltonian(graph: nx.Graph,coef) -> SparsePauliOp:
    """
    Build the MaxCut Hamiltonian for the given graph H = (|E|/2)*I - (1/2)*Σ_{(i,j)∈E}(Z_i Z_j)
    """
    num_qubits = len(graph.nodes)
    edges = list(graph.edges())
    num_edges = len(edges)

    pauli_terms = ["I" * num_qubits]  # start with identity
    coeffs = [-num_edges / 2]

    for u, v in edges:  # for each edge, add -(1/2)*Z_i Z_j
        z_term = ["I"] * num_qubits
        z_term[u] = "Z"
        z_term[v] = "Z"
        pauli_terms.append("".join(z_term))
        coeffs.append(0.5)


        z_term = ["I"] * num_qubits
        z_term[u] = "X"
        z_term[v] = "X"
        pauli_terms.append("".join(z_term))
        coeffs.append(0.5)

        z_term = ["I"] * num_qubits
        z_term[u] = "Y"
        z_term[v] = "Y"
        pauli_terms.append("".join(z_term))
        coeffs.append(0.5)
    
    for i in range(num_qubits):
        for j in range(num_qubits):
            z_term = ["I"] * num_qubits
            z_term[i] = "Z"
            z_term[j] = "Z"
            pauli_terms.append("".join(z_term))
            coeffs.append(coef)

    return SparsePauliOp.from_list(list(zip(pauli_terms, coeffs)))


def build_ansatz(graph: nx.Graph) -> QuantumCircuit:

    ansatz = QuantumCircuit(graph.number_of_nodes())
    ansatz.h(range(graph.number_of_nodes()))

    theta = ParameterVector(r"$\theta$", graph.number_of_edges())
    # for j in range(graph.number_of_nodes() // 4):
    #     # if j4 == 8:
    #     #     break
    #     i = j*4
    #     print(i, j)
    #     ansatz.ry(theta[0], i+1)
    #     ansatz.ry(theta[0], i+3)
    #     ansatz.cx(i+0, i+1)
    #     ansatz.cx(i+2, i+3)
    #     ansatz.cx(i+1, i+2)
    #     ansatz.cx(i+3, i+0)
    #     ansatz.ry(theta[0], i+0)
    #     ansatz.ry(theta[0], i+2)
    #     ansatz.cx(i+1, i+2)
    #     ansatz.cx(i+3, i+0)

    # for i in range(graph.number_of_nodes()):
    #     ansatz.ry(theta[1], i)

    # for t, (u, v) in zip(theta, graph.edges):
    #     ansatz.cx(u, v)
    #     ansatz.ry(t, v)
    #     ansatz.cx(u, v)

    for t, (u, v) in zip(theta, graph.edges):
        ansatz.ry(t, v)
    for i in range(1,graph.number_of_nodes()):
        ansatz.cx(0,i)
    
    return ansatz
