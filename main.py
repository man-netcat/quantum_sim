import quantum as q
from gates import *
from states import *


def main():
    circuit = [[H, H], [CNOT], [H, H]]
    psi = q.apply_circuit(q01, circuit)
    print(psi)
    measurement = q.measure(psi)
    print(measurement)


if __name__ == "__main__":
    main()
