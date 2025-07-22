import numpy as np
from numpy import random
#shuffle() shuffles the elements in array and affects original array
array=np.array([1,2,4,5,6,7])
print("original array before shuffle() = ",array)
random.shuffle(array)
print("Shuffled array using shuffle() = ",array)
print("original array after shuffle() = ",array)
print()
#permutation() similar to shuffle but does not affect the original array
array2=np.array([1,4,5,7,2,8])
newarray2=random.permutation(array2)
print("permutated array using permutation() = ",newarray2)
print("original array after permutation() = ",array2)

