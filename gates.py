import numpy as np

# Pauli X gate
X = np.array([[0, 1], [1, 0]])

# Pauli Y gate
Y = np.array([[0, -1j], [1j, 0]])

# Pauli Z gate
Z = np.array([[1, 0], [0, -1]])

# T gate
T = np.array([[1, 0], [0, np.exp(1j*np.pi/4)]])

# S gate
S = np.array([[1, 0], [0, 1j]])

# Hadamard gate
H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

# Identity gate
I = np.eye(2)

# CNOT gate
CNOT = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0]])

# CZ gate
CZ = np.array([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, -1]])
