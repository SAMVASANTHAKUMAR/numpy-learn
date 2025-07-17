import numpy as np 
#List of DataTypes in Numpy
        #i=integer
        #b=boolean
        #u=unsigned integer
        #U=unicode string
        #f=float
        #c=complex float
        #m=time delta
        #o=object
        #M=date time
        #S=string
        #v=void
#dtype()
array=np.array([1,2,3,4,5,6,7,8,9])
print(array.dtype)
array=np.array([1,2,3,4,5,6,],dtype='S')
print(array.dtype)
#astype()
arrayfloat=[1.1,2.2,3.3,4.5,6.7]
arraynew=array.astype("i")
print("array with float converted to integer using astype()= ",arraynew)
arrayint=np.array([1,2,0,3,1,0])
arraynew2=arrayint.astype(bool)
print("array with integer converted into boolean using astype()= ",arraynew2)


