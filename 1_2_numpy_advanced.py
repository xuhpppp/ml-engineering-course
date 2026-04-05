import numpy as np

# Array and scalar broadcasting
arr = np.array([1, 2, 3])
print("Original Array:", arr)
print("Array + 5:", arr + 5)

matrix = np.array([[1, 2], [3, 4]])
vector = np.array([10, 20])
print("Original Matrix:\n", matrix)
print("Matrix + Vector:\n", matrix + vector)

# Aggregation functions
arr = np.array([[1, 2], [3, 4]])
print("Sum of all elements:", np.sum(arr))
print("Sum along columns:", np.sum(arr, axis=0))
print("Sum along rows:", np.sum(arr, axis=1))
print("Mean of all elements:", np.mean(arr))
print("Standard Deviation:", np.std(arr))

# Boolean indexing and filtering
arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)
print("Elements greater than 3:", arr[arr > 3])
print("Elements that are even:", arr[arr % 2 == 0])

# Random number generation and seeding
np.random.seed(42)  # Set seed for reproducibility
random_array = np.random.rand(3, 3)
print("Random Array:\n", random_array)
random_int_array = np.random.randint(0, 10, (2, 5))
print("Random Integer Array:\n", random_int_array)