import numpy as np

# Add and subtract matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("A + B:\n", A + B)
print("A - B:\n", A - B)

# Scalar multiplication
scalar = 2
print("2 * A:\n", scalar * A)

# Matrix multiplication
print("A @ B:\n", A @ B)

# Identity matrix
I = np.eye(2)
print("Identity Matrix:\n", I)
print("A @ I:\n", A @ I)

# Zero matrix
Z = np.zeros((2, 2))
print("Zero Matrix:\n", Z)

# Diagonal matrix
D = np.diag([1, 2, 3])
print("Diagonal Matrix:\n", D)