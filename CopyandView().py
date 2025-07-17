import numpy as np 
#copy() No change even original array gets changed
arraya=np.array([1,2,3,4,5,6,7])
arrayb=arraya.copy()
print("original array before modifying = ",arraya)
print("Copied array before modifying = ",arrayb)
#modifying original array
arraya[0]=1000
print("original array after modifying = ",arraya)
print("Copied array after modifying = ",arrayb)

print()

#view Affected when Original array gets changed
arrayc=np.array([1,2,3,4,5])
arrayd=arrayc.view()
print("original array before modifying = ",arrayc)
print("Viewed array before modifying= ",arrayd)
#modifying original array
arrayc[0]=100
print("original array after modifying = ",arrayc)
print("Viewed array after modifying= ",arrayd)

