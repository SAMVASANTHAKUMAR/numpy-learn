import numpy as np 
#Concatenating 1D arrays
arraya=np.array([1,2,3,4,5])
arrayb=np.array([6,7,8,9,10])
print("Concatenated 1D array = ",np.concatenate((arraya,arrayb)))
#Concatenating 2D arrays
arrayc=np.array([[1,2],[3,4]])
arrayd=np.array([[5,6],[7,8]])
print("Concatenated 2D array =",np.concatenate((arrayc,arrayd),axis=1))
print()

#stacking
#hstack() horizontal stacking
arrayhstack=np.hstack((arrayc,arrayd))
print("H stacked array =",arrayhstack)
print()
#vstack() vertical stacking
arrayvstack=np.vstack((arrayc,arrayd))
print("V stacked array =",arrayvstack)
print()
#dstack depth of array
arraydstack=np.dstack((arrayc,arrayd))
print("D stack = ",arraydstack)
print()

#Splitting array
arraye=np.array([1,2,3,4,5,6,7,8,9])
newarr=np.array_split(arraye,5)
print("Splitted array = ",newarr)
print()

#indexing after splitting
print(newarr[2])

