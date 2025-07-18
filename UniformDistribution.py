import numpy as np
from numpy import random
#Uniform() for uniform distribution 
#parameters: a=loewerbound-default(0.0),b=upperbound-default(1.0),size=size of the array
x=random.uniform(low=0.8,high=0.9,size=(2,3))
print("Uniform Distributed array = ",x)