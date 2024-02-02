import numpy as np

# Sum by Axis
arr = np.array([[1 , 2 , 3 , 4] , [1 , 2 , 3 , 4]])
sumAxis0 = np.sum(arr , axis=1)
print(f"Sum by Axis : {sumAxis0}")

print("*" * 50)

# Union 1d
arr01 = np.array([1 , 2 , 3 , 4 , 5])
arr02 = np.array([1 , 2 , 3 , 4 , 6])
union1d = np.union1d(arr01 , arr02)
print(f"Union 1d : {union1d}")

print("*" * 50)

# intersect1d
intersection1d = np.intersect1d(arr01 , arr02)
print(f"intersection 1d : {intersection1d}")

print("*" * 50)

# Unique Element == Array without repetition
arr03 = np.array([1 , 2 , 3 , 2 , 4 , 5 , 3 , 10])
uniqueElements = np.unique(arr03)
print(f"Unique Element : {uniqueElements}")

print("*" * 50)

# Trim Zero
arr05 = np.array([0 , 0 , 1 , 2 , 5 , 0])
trimZeros = np.trim_zeros(arr05)
print(f"Trime Zeros : {trimZeros}")

print("*" * 50)

# Operation in array
arr06 = np.array([1 , 2])
arr07 = np.array([1 , 2])
sum = np.add(arr06 , arr07)
subtract = np.subtract(arr06 , arr07)
multiply = np.multiply(arr06 , arr07)
divide = np.divide(arr06 , arr07)
print(f"Sum 2 arrays : {sum}")
print(f"Subtract 2 arrays : {subtract}")
print(f"Multiply 2 arrays : {multiply}")
print(f"Divide 2 arrays : {divide}")

print("*" * 50)

# Dot Product
arr08 = np.array([[1, 2], [3, 4]])
arr09 = np.array([[5, 6], [7, 8]])
dot = np.dot(arr08 , arr09)
print(f"Dot Product : {dot}")

print("*" * 50)

# Sqrt
arr10 = np.array([4 , 16])
sqrt =  np.sqrt(arr10)
print(f"Sqrt : {sqrt}")

print("*" * 50)

# Transpose
arr11 = np.array([[1 , 2 , 3 , 4] , [5 , 6 , 7 , 8]])
transpose = arr11.T
print(f"Transpose : {transpose}")

print("*" * 50)

# Matlib Empty , matlib zeros , matlib eyes, matlib identity
# empty_matrix = np.matlib.empty((2, 2))
# zero_matrix = np.matlib.zeros((2, 2))
# eye_matrix = np.matlib.eye(2)
# identity_matrix = np.matlib.identity(2)
# print("Empty Matrix:", empty_matrix)
# print("Zero Matrix:", zero_matrix)
# print("Eye Matrix:", eye_matrix)
# print("Identity Matrix:", identity_matrix)

print("*" * 50)

# Cross
arr12 = np.array([1 , 2 , 3])
arr13 = np.array([4 , 5 , 8])
cross = np.cross(arr12 , arr13)
print(f"Cross : {cross}")

print("*" * 50)

# Determinant
arr13 = np.array([[1 , 2] , [3 , 4]])
determinant = np.linalg.det(arr13)
print(f"Determinant : {determinant}")

print("*" * 50)

# Var
arr14 = np.array([1 , 2 , 3 , 4 , 5])
var = np.var(arr14)
print(f"Variance: {var}")

print("*" * 50)

# Array equal
arr15 = np.array([1 , 2 , 3 , 4 , 5])
arr16 = np.array([1 , 2 , 3 , 7 , 5])
equal = np.array_equal(arr15 , arr16)
print(f"Equal Array : {equal}")

print("*" * 50)

# Append in np array
arr17 = np.array([1 , 2 , 3 , 4 , 5])
arr18 = np.append(arr17 , [ 6 , 7 , 8 , 9 , 10])
print(f"Append Arr : {arr18}")
# Insert in np array
arr19 = np.insert(arr18 , 10 , 11)
print(f"after insert : {arr19}")
# Delete from np array
arr20 = np.delete(arr19 , 10)
print(f"after delete 11 : {arr20}")

print("*" * 50)

# Stack to concat tow array each athor
arr21 = np.array([1 , 2 , 3 , 4 , 5])
arr22 = np.array([ 6 , 7 , 8 , 9 , 10])
arr23 = np.stack((arr21 , arr22))
print(f"- Concat Arr01 : {arr21} - with Arr02 : {arr22} - Result stack : {arr23}" , end="\n")

# to load extrenal file
arr24 = np.load('nomFichier')