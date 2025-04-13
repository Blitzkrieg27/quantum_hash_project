# analysis/test_collisions.py

import os
import sys
import hashlib
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from quantum_hash.hash_core import quantum_hash_function

def test_collisions(num_samples=1000):
    seen_hashes = set()

    for i in range(num_samples):
        input_data = os.urandom(32)
        output = quantum_hash_function(input_data)
        
        # Convert to hex for fast lookup and display
        hash_hex = output.hex()
        
        if hash_hex in seen_hashes:
            print(f"\n[!] Collision found at sample {i + 1}!")
            print(f"Input: {list(input_data)}")
            print(f"Hash: {hash_hex}")
            return

        seen_hashes.add(hash_hex)

        if (i + 1) % 100 == 0:
            print(f"[*] Tested {i + 1} inputs... no collision.")

    print(f"\n[✓] No collisions found after {num_samples} samples.")

if __name__ == "__main__":
    print("[*] Starting collision test...")
    test_collisions()
