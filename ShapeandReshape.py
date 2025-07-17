import numpy as np
#shape tells no of elements in each dimension
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print("arr =",arr)
print("Shape of arr = ",arr.shape)
arr2=np.array([1,2,3,],ndmin=5)
print("arr2 =",arr2)
print("Shape of arr2 = ",arr2.shape)

print()

#reshape reshapes original array in required way
arraya=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arrayb=arraya.reshape(2,3,2)
print("original array = ",arraya)
print("Reshaped array = ",arrayb)

print()

#checking which is original array
print("original array (base array) = ",arrayb.base)
print()
#getting back the original array
print("using -1 in reshape,getting original array back = ",arrayb.reshape(-1))

