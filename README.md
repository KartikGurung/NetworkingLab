# Network Security Lab Experiments

This repository contains a small set of Python-based networking and security experiments demonstrating classic cryptographic and authentication concepts.

## Contents

- `exp-1.py` — Caesar cipher and Vigenere cipher encryption/decryption examples
- `exp-2.py` — SHA-256 file integrity checking demonstration
- `exp-3.py` — Challenge-response authentication and replay attack example
- `sample.txt` — sample file used in the integrity experiment

## Experiment Overview

### 1. Encryption and Decryption
The first script demonstrates:
- Caesar cipher encryption and decryption
- Vigenere cipher encryption and decryption

Run it with:

```bash
python3 exp-1.py
```

### 2. Data Integrity
The second script shows how SHA-256 hashing can be used to detect tampering:
- Create a trusted hash for a sample file
- Modify the file content
- Recalculate the hash and compare it with the original

Run it with:

```bash
python3 exp-2.py
```

### 3. Authentication and Replay Attack
The third script demonstrates:
- Challenge-response authentication using a shared secret and SHA-256
- Replay attack prevention logic by validating responses against the current challenge

Run it with:

```bash
python3 exp-3.py
```

## Requirements

- Python 3
- No external libraries are required

## Notes

These scripts are intended for learning and demonstration purposes in a network security lab environment.
