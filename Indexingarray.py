import numpy as np 

# 1D indexing
arraya = np.array([1, 2, 3, 4])
print("1D:", arraya[2])
# 2D indexing 
arrayb = np.array([[1, 2], [3, 4], [5, 6]])
print("2D:", arrayb[1, 1])
# 3D indexing
arrayc = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D:", arrayc[0, 1, 1])
# Negative indexing
print("Negative:", arrayb[-1])
input("AS the terminal prematurely stops i gave an input for forcing it to be opened")