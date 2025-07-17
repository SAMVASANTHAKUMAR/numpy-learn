import numpy as np
#sort() similar to python sort method
array=np.array([1,4,5,2,7,6])
print("Unsorted array = ",array)
print("Sorted array = ",np.sort(array))

print()

#filter() uses boolean values for filtering
array2=[True,False,True,False,False,True]
newarray=array[array2]
print("New array(filtered using boolean values in array2)=",newarray)
print()
filter=array%2==0
print("Filter array = ",filter)
nowarray=array[filter]
print("Filtered array = ",nowarray)