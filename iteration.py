# for fixed point iteration
import numpy as np

def g(p):
    return np.cbrt((2*p+5)/2)
p0=1.5
tolerance= 1.0e-6
NO=1000

i=1
while i<=NO:
    p=g(p0)
    if np.abs(p0-p)<tolerance:
        break
    print(i,"th iteration", " ",p)
    i=i+1
    p0=p

if(i==NO+1):
    print("The method failed after NO iteration")
else:
    print("The method is successful")
