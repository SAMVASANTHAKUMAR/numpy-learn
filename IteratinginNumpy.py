import numpy as np
#nditer() avoids nested loops for displaying each element in 3D and M D arrays
array=np.array([[1,2],[3,4],[5,6],[7,8]])
for x in np.nditer(array):
    print("Element using nditer : ",x)
#flags  and op_types as parameters
#flags="buffered" allocates some buffer 
#op_types we can change the dtype of elements ex: op_types='i'>change into integer
for x in np.nditer(array,flags=['buffered'],op_dtypes=['S']):
    print("Element using nditer with flags and op_types = ",x)

print()

#enumerate() describes the indices and corresponding elements
array=np.array([[1,2],[3,4],[5,6]])
for x in np.ndenumerate(array):
    print("Enumerated = ",x)
print()
#removing unwanted paranthesis in output
for idx,x in np.ndenumerate(array):
    print("After removing unwanted()= ",idx,x)

