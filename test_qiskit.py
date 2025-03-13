from qiskit import QuantumCircuit

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)
qc.h(0)  # Apply Hadamard gate on qubit 0
qc.cx(0, 1)  # Apply CNOT gate
qc.measure_all()

# Draw the circuit
print(qc.draw())
