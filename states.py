import numpy as np
import quantum as q

# |0⟩
q0 = np.array([[1], [0]])
# |1⟩
q1 = np.array([[0], [1]])

# |00⟩
q00 = q.states([q0, q0])

# |01⟩
q01 = q.states([q0, q1])

# |10⟩
q10 = q.states([q1, q0])

# |11⟩
q11 = q.states([q1, q1])
