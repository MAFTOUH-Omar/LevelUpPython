import numpy as np

myList01 = [[1 , 2 , 3] , [4 , 5 , 7] , [8 , 9 , 10] , [11 , 12 , 13]]
myArray = np.array(myList01)

# print(myArray[0: , :2])

myArray02 = np.array([1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12])
print(myArray02.ndim) # 1
print(myArray02.shape) # (12 ,)

print("*" * 50)

reshape_myArray02 = myArray02.reshape(2 , 6)
print(reshape_myArray02.ndim) # 2
print(reshape_myArray02)  # [ [ 1  2  3  4  5  6] , [ 7  8  9 10 11 12] ]

print("*" * 50)

reshape02_myArray02 = myArray02.reshape(2 , 2 , 3)
print(reshape02_myArray02.ndim) # 3
print(reshape02_myArray02)  # [ [[ 1  2  3] , [ 4  5  6]] , [[ 7  8  9] , [10 11 12]] ]