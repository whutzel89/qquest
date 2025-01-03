import cirq

def main():
    circuit = cirq.Circuit()
    # qubits = cirq.LineQubit.range(3)
    # circuit.append(cirq.H(qubits[0]))
    # circuit.append(cirq.H(qubits[1]))
    # circuit.append(cirq.H(qubits[2]))
    # Define three qubits.
    a = cirq.NamedQubit("ayyyy")
    b = cirq.NamedQubit("beeee")
    c = cirq.NamedQubit("ceeee")
    circuit.append(cirq.H(a))
    circuit.append(cirq.H(b))
    circuit.append(cirq.H(c))
    circuit.append(cirq.CNOT(b,c))
    circuit.append(cirq.X(a))
    circuit.append(cirq.CZ(b,a))
    circuit.append(cirq.CNOT(c,b))
    print(circuit)


if __name__ == "__main__":
    main()
