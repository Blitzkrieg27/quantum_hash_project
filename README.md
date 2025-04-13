# quantum_hash_project
Prototype quantum hash function using parameterized circuits - with testing entropy, collision, avalanche &amp; bit independence tests. Built with Qiskit.

# Mark-1: A Quantum Hash Function Prototype

## Overview

Mark-1 of a prototype quantum hash function built using parameterized quantum circuits. It simulates a hash mechanism based on quantum circuit behavior, aiming to explore the feasibility of quantum-era cryptographic primitives.

It's apparent for anyone with a little domain know-how as to how & why quantum hash functions may offer new cryptographic security models in the presence of quantum computing capabilities. This project demonstrates a first-step implementation that maps classical input data to quantum parameters, extracts measurement-based signatures, and ensures desirable hash properties such as high entropy and sensitivity to input changes.

## Features

- Parameterized quantum circuit with entangling layers
- Input encoding into continuous quantum gate parameters
- Statevector-based computation
- Tests for entropy, collisions, avalanche effect, and bit independence

## Installation

### Requirements

- Python 3.9+
- Qiskit
- NumPy

### Setup

Clone the repo:

```bash
git clone https://github.com/yourusername/quantum_hash_project.git
cd quantum_hash_project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the main script:

```bash
python main.py
```

This hashes a 32-byte input using the quantum circuit and prints both input and output bytes.

## Hash Quality Analysis

### Entropy Test

- Average Entropy over 100 samples: **\~1.74 to 2.31 bits per byte**
- Maximum possible entropy: **4 bits per byte (32 bytes output)**

### Collision Test

- **0 collisions** found across **1000 randomly generated 32-byte inputs**

### Avalanche Effect

- **Bit Differences:** 72 / 128 (i.e., over **56%** bits flipped on 1-bit input change)

### Bit Independence

- **Average deviation from 50% distribution:** 6.21 bits
- **Maximum deviation:** 23 bits

These results indicate a moderate-to-strong diffusion and randomness profile, suitable for a prototype.

## Project Structure

```
quantum_hash_project/
├── analysis/
│   ├── test_entropy.py
│   ├── test_collisions.py
│   ├── test_avalanche.py
│   └── test_bit_independence.py
├── quantum_hash/
│   ├── circuit_builder.py
│   ├── hash_core.py
│   └── input_encoder.py
├── main.py
└── README.md
```

## Limitations

- Operates on simulated quantum circuits (limited scalability)
- Uses statevector output, which may contain biases
- Fixed number of qubits (16) and layers (3)

## Future Work

- Transition to measurement-based output extraction
- Postprocessing via classical mixing functions
- More statistical testing (NIST suite)
- Implementation on real quantum hardware

## License

MIT License. See `LICENSE` file for details.

## Citation

If using this project in academic work, please cite as:

```bibtex
@misc{mark1_quantum_hash,
  author = Bhvyadhirr Bharadwaj,
  title = {Mark-1: A Quantum Hash Function Prototype},
  year = {2025},
  howpublished = {\url{https://github.com/Blitzkrieg27/quantum_hash_project}},
}
```

---

Feel free to contribute or reach out for collaboration!

