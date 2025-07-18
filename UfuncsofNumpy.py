import numpy as np
#Ufuncs = built-in functions of numpy(for aggregating operations)
#creating a ufunc
def myfunc(x,y):
    return x+y
myfunc=np.frompyfunc(myfunc,2,1) #frompyfunc(ufunc_name,no of inputs,no of outputs)
print(myfunc([1,2,3,4],[2,3,4,5]))
print()
#aggregate functions
a=np.array([1,2,3,4])
b=np.array([2,3,4,5])
#add()
print("Add() = ",np.add(a,b))
#subtract()
print("subtract() = ",np.subtract(a,b))
#multiply()
print("Multiply() = ",np.multiply(a,b))
#divide()
print("Divide() = ",np.divide(a,b))
#power()
print("Power() = ",np.power(a,b))
#remainder()
print("Remainder() = ",np.remainder(a,b))
#mod()
print("Modulus() = ",np.mod(a,b))
#divmod() for both remainder and quotient
print("DivMod() = ",np.divmod(a,b))
#abs() absolute difference(avoids -sign)
print("Abs() = ",np.abs(a,b))
