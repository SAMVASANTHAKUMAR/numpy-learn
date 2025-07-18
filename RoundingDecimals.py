import numpy as np
#truncation trunc()-rounds off given float and converts them into int data type
x=np.trunc([8.99,4.55,5.99,3.22])
print("Truncated values using trunc() = ",x)
#fix() similar to trunc() - same operation of trunc()
y=np.fix([8.99,4.55,5.99,3.22])
print("Fixed values using fix() = ",y)
print()
#around() or round() - we can fix the no of decimals 
z=np.around([8.9997653245,4.5555545,5.98898459,3.26765342],3)
print("Rounded values using around() = ",z)
print()
#flooring using floor()-lower bound rounding  similar to trunc() but does not change the datatype of the elements
a=np.floor([8.9997653245,4.5555545,5.98898459,3.26765342])
print("floor values using floor() = ",a)
print()
#ceiling using ceil()-upper bound rounding off
b=np.ceil([8.9997653245,4.5555545,5.98898459,3.26765342],)
print("Ceiled values using ceil() = ",b)
print()