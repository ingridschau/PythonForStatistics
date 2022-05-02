import numpy as np 
from scipy.stats import poisson 
 
lambdal = 300 
t=1/60 
n=7 
 
F= np.zeros(n+1) 
 
print("________________________________________________") 
 
x=0 
while x < 7 : 
    F[x]=poisson.cdf(x,lambdal*t) 
    print(f'P(X <= {x}) = {"{:.5f}".format(F[x])}') 
    x=x+1
