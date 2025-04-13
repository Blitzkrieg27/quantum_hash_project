# analysis/test_avalanche.py

import os
import random
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from quantum_hash.hash_core import quantum_hash_function

def count_bit_differences(b1: bytes, b2: bytes) -> int:
    return sum(bin(x ^ y).count('1') for x, y in zip(b1, b2))

def test_avalanche():
    input_data = bytearray(os.urandom(32))
    
    # Flip a single bit
    byte_index = random.randint(0, 31)
    bit_index = random.randint(0, 7)
    input_data[byte_index] ^= 1 << bit_index

    output_1 = quantum_hash_function(bytes(input_data))
    input_data[byte_index] ^= 1 << bit_index  # revert bit
    output_2 = quantum_hash_function(bytes(input_data))

    diff = count_bit_differences(output_1, output_2)

    print(f"Avalanche Effect Bit Differences: {diff} / {len(output_1) * 8}")

if __name__ == "__main__":
    test_avalanche()
