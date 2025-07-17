import numpy as np 
#slicing 2D for new array with just 1 elements from each 1D of 2D array
arraya=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print("Sliced 2D = ",arraya[0:2,3])
#slicing 2D for new array with more than 1 element from each 1D of 2D array 
print("Sliced for more than one element = ",arraya[0:2,1:4]) 
