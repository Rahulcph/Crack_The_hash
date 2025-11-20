# Crack_The_hash
A simple Python project that demonstrates how salted hashes are created and brute-forced. Includes scripts for generating salted MD5, SHA-256, and SHA-512 hashes and a brute-force script that searches a 6-digit numeric range. Built for learning and educational purposes only.
# Salted Hash Brute Force Demo

This project contains two Python scripts that demonstrate how salted hashes are created and brute-forced within a 6-digit numeric range.

## Files
- **createhashes.py** – Generates three random 6-digit numbers, adds a fixed salt (`ABCDEFG`), and prints their MD5, SHA-256, and SHA-512 hashes.
- **Bruteforce.py** – Brute-forces the range `100000–999999` to find which number matches each salted hash.

## How to Use
1. Run `createhashes.py` to generate new hash values.
2. Copy the printed hashes into the target hash variables in `Bruteforce.py`.
3. Run `Bruteforce.py` to perform the brute-force search.

## Purpose
This project is for **educational learning only**, showing how hashing, salting, and brute-force attacks work in a controlled environment.

## Requirements
- Python 3.x
- No external libraries required
