 # Prime Field Model — Generative Dynamics for Prime Numbers

This repository contains the reference implementation of a discrete dynamical model
that reproduces the sequence of prime numbers up to N = 200,000 with perfect accuracy.

The model is described in the article:

**A Discrete Generative Model Reproducing Prime Numbers**  
(Submitted to the *Journal of Integer Sequences*, 2026)

---

## 📌 Overview

The model defines a local dynamical process on the integers, based on:
- a residue field evolving with each event,
- a threshold mechanism,
- a local absorption rule,
- and a minimal update equation.

Despite its simplicity, the system generates exactly the classical prime sequence.

This repository provides:
- the full Python implementation (`main.py`),
- the generated list of primes/events up to 200,000 (`events_200k.txt`),
- instructions for reproducing the results.

---

## 📦 Requirements

The code uses only the Python standard library.

- Python ≥ 3.10  
No external dependencies are required.

---

## ▶️ Running the model

To reproduce the results:

```bash
python main.py
