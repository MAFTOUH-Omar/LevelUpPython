import numpy as np

# axis
arr = np.array([[1, 2, 3], [4, 5, 6]])
result = np.sum(arr, axis=0)
print("Sum along axis 0:", result)

# union1d
arr1 = np.array([1, 2, 3])
arr2 = np.array([3, 4, 5])
result = np.union1d(arr1, arr2)
print("Union:", result)

# intersect1d
result = np.intersect1d(arr1, arr2)
print("Intersection:", result)

# unique
arr = np.array([1, 2, 2, 3, 3, 4, 5])
result = np.unique(arr)
print("Unique elements:", result)

# trim_zeros
arr = np.array([0, 0, 1, 2, 3, 0, 0])
result = np.trim_zeros(arr)
print("Trimmed array:", result)

# add, subtract, multiply, divide
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result_add = np.add(arr1, arr2)
result_subtract = np.subtract(arr1, arr2)
result_multiply = np.multiply(arr1, arr2)
result_divide = np.divide(arr1, arr2)
print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)

# dot
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
result = np.dot(arr1, arr2)
print("Dot product:", result)

# sqrt
arr = np.array([1, 4, 9])
result = np.sqrt(arr)
print("Square root:", result)

# sum
arr = np.array([1, 2, 3])
result = np.sum(arr)
print("Sum:", result)

# T
arr = np.array([[1, 2], [3, 4]])
result = arr.T
print("Transpose:", result)

# matlib.empty, matlib.zeros, matlib.eye, matlib.identity
empty_matrix = np.matlib.empty((2, 2))
zero_matrix = np.matlib.zeros((2, 2))
eye_matrix = np.matlib.eye(2)
identity_matrix = np.matlib.identity(2)
print("Empty Matrix:", empty_matrix)
print("Zero Matrix:", zero_matrix)
print("Eye Matrix:", eye_matrix)
print("Identity Matrix:", identity_matrix)

# cross
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.cross(arr1, arr2)
print("Cross product:", result)

# linalg.det
arr = np.array([[1, 2], [3, 4]])
result = np.linalg.det(arr)
print("Determinant:", result)

# var
arr = np.array([1, 2, 3, 4, 5])
result = np.var(arr)
print("Variance:", result)

# linalg.inv
arr = np.array([[1, 2], [3, 4]])
result = np.linalg.inv(arr)
print("Inverse matrix:", result)

# linalg
arr = np.array([[1, 2], [3, 4]])
result = np.linalg.norm(arr)
print("Norm:", result)

# random.normal, random.logistic
normal_distribution = np.random.normal(0, 1, 5)
logistic_distribution = np.random.logistic(0, 1, 5)
print("Normal Distribution:", normal_distribution)
print("Logistic Distribution:", logistic_distribution)

# np.fromfunction
def my_function(x, y):
    return x + y

result = np.fromfunction(my_function, (3, 3))
print("From function:", result)

# Universal functions
arr = np.array([1.5, 2.5, 3.5])
result_add = np.add(arr, 1)
result_subtract = np.subtract(arr, 1)
result_multiply = np.multiply(arr, 2)
result_power = np.power(arr, 2)
result_divide = np.divide(arr, 2)
result_divmod = np.divmod(arr, 2)
result_abs = np.abs(arr)
result_sqrt = np.sqrt(arr)
result_round = np.round(arr)
result_ceil = np.ceil(arr)
result_floor = np.floor(arr)
result_trunc = np.trunc(arr)
result_mean = np.mean(arr)

print("Add:", result_add)
print("Subtract:", result_subtract)
print("Multiply:", result_multiply)
print("Power:", result_power)
print("Divide:", result_divide)
print("Divmod:", result_divmod)
print("Absolute:", result_abs)
print("Square root:", result_sqrt)
print("Round:", result_round)
print("Ceil:", result_ceil)
print("Floor:", result_floor)
print("Truncate:", result_trunc)
print("Mean:", result_mean)
