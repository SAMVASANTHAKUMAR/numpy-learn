import numpy as np
from numpy import random
#Normal() method for Normal distribution(continuous)
#parameters: loc=mean,scale=Standard Deviation,size=size of the array to be displayed
x=random.normal(loc=34,scale=67,size=(3,4))
print("Normal Distributed array by normal() = ",x)
print()
#Binomial() method for Binomial distribution(discrete)
#parameters: n=no of trials,p=probability,size=size of array
y=random.binomial(n=10,p=.3,size=(3,9))
print("Binomial Distributed array by binomial() = ",y)
