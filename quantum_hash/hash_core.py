# quantum_hash/hash_core.py

import numpy as np
from qiskit.quantum_info import Statevector, Pauli
from quantum_hash.circuit_builder import build_parameterized_circuit
from quantum_hash.input_encoder import encode_input_to_params

def quantum_hash_function(input_data: bytes) -> bytes:
    """
    Performs quantum hashing on the given byte input using a parameterized circuit
    and returns the resulting hash output as bytes.
    """

    # Validate input
    if not isinstance(input_data, bytes):
        raise ValueError("Input must be of type 'bytes'.")

    num_qubits = 16  # Configurable: must be ≤ 20
    circuit, params = build_parameterized_circuit(num_qubits)

    # Encode input to parameters
    param_dict = encode_input_to_params(input_data, params)

    # Assign params
    bound_circuit = circuit.assign_parameters(param_dict)

    # Simulate and get statevector
    sv = Statevector.from_instruction(bound_circuit)

    # Get Z-expectations for each qubit
    expectations = [sv.expectation_value(Pauli("Z"), [i]).real for i in range(num_qubits)]

    # Map expectations [-1, 1] → bytes [0, 255]
    output_bytes = bytearray([min(int(((val + 1) / 2) * 256), 255) for val in expectations])

    return bytes(output_bytes)
