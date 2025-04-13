# quantum_hash/circuit_builder.py

from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from typing import List, Tuple

def build_parameterized_circuit(num_qubits: int, num_layers: int = 3) -> Tuple[QuantumCircuit, List[Parameter]]:
    """
    Builds a layered parameterized quantum circuit with entanglement.

    Returns:
        qc (QuantumCircuit): The quantum circuit.
        params (List[Parameter]): List of parameters.
    """
    qc = QuantumCircuit(num_qubits)
    params = []

    for layer in range(num_layers):
        for i in range(num_qubits):
            theta = Parameter(f"theta_ry_{layer}_{i}")
            qc.ry(theta, i)
            params.append(theta)

        for i in range(num_qubits):
            phi = Parameter(f"theta_rz_{layer}_{i}")
            qc.rz(phi, i)
            params.append(phi)

        for i in range(num_qubits):
            qc.cx(i, (i + 1) % num_qubits)

    return qc, params
