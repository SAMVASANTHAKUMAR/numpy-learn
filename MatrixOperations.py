import numpy as np 
#use dot() or @ or matmul() for matrix multiplication
#use T for transposing matrix
arraya=np.array([[1,2],[3,6]])
arrayb=np.array([[2,3],[8,7]])
print("Multiplied matrix using dot() = ",np.dot(arraya,arrayb))
print()
print("Multiplied matrix using @ = ",arraya@arrayb)
print()
print("Multiplied matrix using matmul() = ",np.matmul(arraya,arrayb))
print()
arrayc=arraya.T
print("Transposed array using T = ",arrayc)
