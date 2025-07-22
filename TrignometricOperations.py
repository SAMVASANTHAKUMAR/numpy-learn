import numpy as np
#for pi value usage np.pi
#for degree to radian values deg2rad
x=np.array([25,56,78])
print("Degree to Radian values using deg2rad = ",np.deg2rad(x))
print()
#for radian to degree values rad2deg
y=np.array([22,52,45])
print("Radian to Degree values using rad2deg = ",np.rad2deg(y))
print()
#for finding trignometric angles from given values
#arcsin(),arccos(),arctan()
z=np.array([0.1,0.6,0.7,0.9])
print("Sin angles of values using arcsin() = ",np.arcsin(z))
print()
a=np.array([0.1,0.6,0.7,0.9])
print("Cos angles of values using arccos() = ",np.arccos(a))
print()
b=np.array([25,56,78])
print("Tan angles of values using arctan() = ",np.arctan(b))
print()
print(np.pi)