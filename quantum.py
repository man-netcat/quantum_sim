import itertools
from functools import reduce

import numpy as np


def states(qs):
    """Applies the kronecker product on an arbitrary number of qubits"""
    return reduce(np.kron, qs)


def apply_gates(q, gates):
    """Applies a sequence of gates to a quantum state."""
    return reduce(np.kron, gates) @ q


def apply_circuit(q, circuit):
    """Applies a circuit of gates to a quantum state."""
    return reduce(apply_gates, circuit, q)


def measure(q, num_measurements=1):
    """
    Measures the state q num_measurements times, collapsing it into a classical
    bitstring of zeros and ones representing the measurement outcomes.
    Returns the resulting bitstring.
    """
    num_qubits = int(np.log2(len(q)))
    width = num_qubits + num_measurements - 1
    probs = np.abs(q.flatten()) ** 2
    bitstring = ""
    for _ in range(num_measurements):
        outcome = np.random.choice(len(q), p=probs)
        bitstring += f"{outcome:0>{width}b}"
        q = np.zeros_like(q)
        q[outcome] = 1
    return bitstring
