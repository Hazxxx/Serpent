# Serpent Cipher - Full Python Implementation

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Security Level](https://img.shields.io/badge/Security-AES--Finalist-red.svg)]()
[![Build Status](https://img.shields.io/badge/Tests-NESSIE--Verified-brightgreen.svg)]()

## 🛡️ Overview
This repository contains a high-fidelity, standalone implementation of the **Serpent symmetric block cipher**. Designed for maximum security and transparency, this project covers the full encryption/decryption pipeline, including key scheduling and linear transformation layers.

Developed in collaboration with **Jakub Adam Pokorski** at **Warsaw University of Technology**.

## 🚀 Technical Features
* **32-Round SP-Network**: Complete implementation of the Serpent architecture.
* **Electronic Codebook (ECB) Mode**: Integrated `SerpentECB` class for block-based encryption.
* **PKCS7 Padding**: Built-in support for arbitrary data lengths.
* **Bit-sliced S-Boxes**: Efficient implementation of S-boxes (S0-S7) using bitwise logic.
* **Key Scheduling**: Supports 256-bit keys with a full 132-word expansion (W0...W131).

## 📊 Verification & Performance
The implementation has been rigorously tested against official standards:
* **NESSIE Test Vectors**: Verified against standard vectors (e.g., Key: `80...00`, PT: `00...00`).
* **Integrity Checks**: Includes tests for ciphertext corruption and key sensitivity.
* **Performance**: Capable of processing 1MB of data with full encryption/decryption cycles for benchmarking.
