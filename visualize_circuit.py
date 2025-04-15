from quantum_hash.circuit_builder import build_parameterized_circuit
from quantum_hash.input_encoder import encode_input_to_params

sample_input = b"QuantumHashInputData1234567890!!"

num_qubits = 8  # or infer from the input length if needed
num_layers = 3  # same as in your builder

# Build the parameterized circuit structure
qc, param_list = build_parameterized_circuit(num_qubits, num_layers)

# Encode input to parameter values
param_value_dict = encode_input_to_params(sample_input, param_list)

# Bind actual parameter values
qc = qc.assign_parameters(param_value_dict)

# Visualize
fig = qc.draw(output="mpl")
fig.savefig("visualizations/mark1_quantum_hash_circuit.png", dpi=300, bbox_inches='tight')
print("\n Circuit image saved as mark1_quantum_hash_circuit.png")
