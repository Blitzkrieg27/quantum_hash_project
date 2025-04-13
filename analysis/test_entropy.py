# analysis/test_entropy.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import os
from quantum_hash.hash_core import quantum_hash_function

def calculate_entropy(byte_sequence: bytes) -> float:
    """
    Calculate Shannon entropy of a byte sequence.
    """
    if len(byte_sequence) == 0:
        return 0.0
    _, counts = np.unique(list(byte_sequence), return_counts=True)
    probs = counts / counts.sum()
    entropy = -np.sum(probs * np.log2(probs))
    return entropy

def test_entropy(num_samples=100, input_size=32):
    """
    Tests entropy of quantum hash outputs across many random inputs.
    """
    entropies = []

    for _ in range(num_samples):
        random_input = os.urandom(input_size)
        hash_output = quantum_hash_function(random_input)
        entropy = calculate_entropy(hash_output)
        entropies.append(entropy)

    avg_entropy = np.mean(entropies)
    max_entropy = np.log2(len(hash_output)) * 8  # 256 bits of max entropy
    print(f"\n[*] Average entropy: {avg_entropy:.4f} / {max_entropy:.2f} bits")

if __name__ == "__main__":
    print("[*] Starting entropy test...")
    test_entropy(num_samples=100)
