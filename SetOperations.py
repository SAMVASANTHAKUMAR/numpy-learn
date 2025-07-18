import numpy as np
#union1d() for union operation
#intersect1d() for intersection
#setdiff1d() for set_difference
#setxor1d() for symmetric_difference 
arraya=np.array([1,3,4,5,6,7,8])
arrayb=np.array([2,3,4,1,5,6,7])
print("Union of arrays using union() = ",np.union1d(arraya,arrayb))
print("Intersection of arrays using intersect1d() = ",np.intersect1d(arraya,arrayb))
print("Difference of arrays using setdiff1d() = ",np.setdiff1d(arraya,arrayb))
print("symmetric_difference of arrays using setxor1d() = ",np.setxor1d(arraya,arrayb))
