import numpy as np

# Determinant of a matrix
A = np.array([[1, 2], [3, 4]])
det_A = np.linalg.det(A)
print("Determinant of A:", det_A)

# Inverse of a matrix
if det_A != 0:
    A_inv = np.linalg.inv(A)
    print("Inverse of A:\n", A_inv)

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues of A:", eigenvalues)
print("Eigenvectors of A:\n", eigenvectors)

# Singular Value Decomposition (SVD)
U, S, Vt = np.linalg.svd(A)
print("U matrix:\n", U)
print("Singular values:", S)
print("V^T matrix:\n", Vt)