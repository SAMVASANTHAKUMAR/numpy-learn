import numpy as np
from numpy import random
#in choice() p as a parameter,we can give probabilities of each element to be appeared
#ex: element with high probability appears more than element with less probability
x=random.choice([1,2,3,4,5,],p=[0.2,0.2,0.2,0.3,0.1],size=(5))
print("Choice with probablity specified = ",x)