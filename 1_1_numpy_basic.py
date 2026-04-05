import numpy as np

# Create a 1D array
arr1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1d)

# Create a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2d)

# Create a matrix of zeros
zeros_matrix = np.zeros((3, 3))
print("Matrix of Zeros:\n", zeros_matrix)

# Create a matrix of ones
ones_matrix = np.ones((2, 4))
print("Matrix of Ones:\n", ones_matrix)

# Create a range of numbers
range_array = np.arange(0, 10, 2)
print("Range Array:", range_array)

# Create a linearly spaced array
linspace_array = np.linspace(0, 1, 5)
print("Linearly Spaced Array:", linspace_array)

# Reshape an array
reshaped_array = arr1d.reshape(5, 1)
print("Reshaped Array:\n", reshaped_array)

# Mathematical operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Addition:", a + b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Statistical operations
print("Mean:", np.mean(arr1d))
print("Square Root:", np.sqrt(arr1d))
print("Maximum:", np.max(arr1d))
print("Minimum:", np.min(arr1d))

# Indexing and slicing
print("First element:", arr1d[0])
print("Last element:", arr1d[-1])
print("Slice from index 1 to 3:", arr1d[1:4])