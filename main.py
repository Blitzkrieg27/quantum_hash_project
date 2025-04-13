# main.py

from quantum_hash.hash_core import quantum_hash_function

def main():
    input_data = bytes(range(32))  # 32-byte input

    hash_output = quantum_hash_function(input_data)

    print("Input Bytes: ", list(input_data))
    print("Hash Output Bytes: ", list(hash_output))

if __name__ == "__main__":
    main()
