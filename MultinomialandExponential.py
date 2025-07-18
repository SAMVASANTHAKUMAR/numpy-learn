import numpy as np
from numpy import random
#Multinomial() similar to binomial() but the no of probability values should be<= the no of possible outcomes
#parameters: n=no of possible outcomes,pvals=list of probablity values,size=size of array
x=random.multinomial(n=6,pvals=[1/6,2/6,1/6,2/6,5/6],size=(2,4))
print("Multinomial Distrubuted array = ",x)
print()
#Exponential() to indicate the exponential growth or downfall in random sampling
#parameters: scale=inverse rate-default=1.0,size=size of array
y=random.exponential(scale=2,size=(4,5))
print("Exponential Distributed array = ",y)