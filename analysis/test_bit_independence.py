# analysis/test_bit_independence.py

import os
import sys
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from quantum_hash.hash_core import quantum_hash_function

def test_bit_independence(num_samples=200):
    bit_counts = np.zeros(8 * 16, dtype=int)  # 16 bytes * 8 bits

    for _ in range(num_samples):
        input_data = os.urandom(32)
        output = quantum_hash_function(input_data)

        for byte_idx, byte in enumerate(output):
            for bit_idx in range(8):
                if byte & (1 << bit_idx):
                    bit_counts[byte_idx * 8 + bit_idx] += 1

    # Expectation is ~num_samples / 2 for each bit
    deviations = [abs(count - num_samples / 2) for count in bit_counts]
    avg_deviation = np.mean(deviations)
    max_deviation = np.max(deviations)

    print(f"Average deviation from balanced bit (50%): {avg_deviation:.2f}")
    print(f"Max deviation: {max_deviation}")

if __name__ == "__main__":
    test_bit_independence()
