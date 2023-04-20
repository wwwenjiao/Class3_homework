data = np.array([[1, 2], [3, 4], [5, 6]])

# Reshape matrix into 1D array
arr = matrix.reshape(-1)

# Calculate mean and standard deviation of 1D array
mean = np.mean(arr)
std = np.std(arr)

# Reshape 1D array into 2D matrix with same number of rows and columns as original matrix
new_matrix = arr.reshape(matrix.shape[0], matrix.shape[1])

# Element-wise multiplication of original matrix and reshaped 2D matrix
mult_matrix = np.multiply(matrix, new_matrix)

# Sum of all elements in element-wise multiplied matrix
sum_mult_matrix = np.sum(mult_matrix)

print(f"Original matrix: {matrix}")
print(f"Reshaped 1D array: {arr}")
print(f"Mean of 1D array: {mean}")
print(f"Standard deviation of 1D array: {std}")
print(f"Reshaped 2D matrix: {new_matrix}")
print(f"Element-wise multiplied matrix: {mult_matrix}")
print(f"Sum of all elements in element-wise multiplied matrix: {sum_mult_matrix}")