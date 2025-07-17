import numpy as np
#where() similar to SQL WHERE clause
#simple where condition
array=np.array([1,2,3,4,5,6,7,8,9,10])
y=np.where(array==2)
print("Index of element 2 = ",y)
print()
#getting Condition as input
x=int(input("Enter Search element:"))
z=np.where(array==x)
print("Index of element ",x,"=",z)
print()
#Other conditions example:indices of even elements
a=np.where(array%2==0)
print("Indices of Even Elements: ",a)
print()

#searchsorted()
print("Index using searchsorted()=",np.searchsorted(array,7))
print("Indices using searchsorted()=",np.searchsorted(array,[2,5,6]))
