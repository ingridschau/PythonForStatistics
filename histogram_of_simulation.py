from scipy.stats import binom 
import numpy as np 
import math 
import matplotlib.pyplot as plt 
 
n = 672 
p =0.08 
 
M= 1000 
X= np.zeros(M) 
 
for i in range(M): 
    for j in range(n): 
        r=np.random.rand() 
        if r < p: 
            X[i]=X[i]+1 
 
P = np.zeros(n+1) 
 
for x in range(n+1): 
    P[x]=binom.pmf(x,n,p) 
     
     
gjennomsnitt= sum(X)/M 
 
mu= n*p 
 
VarX=(sum((X - gjennomsnitt)**2))/(M-1) 
S=np.sqrt(VarX) 
sigma=np.sqrt(n*p*(1-p)) 
 
print(f"gjennom snitt fra simolation = {gjennomsnitt}") 
print(f"forventet antall feilvarer teoretisk = {mu}") 
print(f"standaravvik fra simolation = {S}") 
print(f"standaravvik teoretisk = {sigma}") 
 
 
fig,axis=plt.subplots(1,2,sharey=True,figsize=(12,6)) 
muInt=math.floor(mu) 
sigmaInt=math.floor(sigma) 
Min= muInt -3*sigmaInt 
Max=muInt +3*sigmaInt 
plt.subplot(1,2,1) 
plt.hist(X,bins=np.arange(Min-0.5,Max+0.5,1),density=True, ec='white') 
plt.xlabel('antall feilvarer') 
plt.ylabel('relativ frekvens fra simulation') 
 
plt.subplot(1,2,2) 
plt.bar(range(Min,Max+1,1),P[Min:Max+1], color='orange') 
 
plt.xlabel('antall feilvarer') 
plt.ylabel('teoretisk sannsynlighet ved binomisk fordeling')
