from scipy.stats import binom
import numpy as np
n=10
p = 0.378149373
F = np.zeros(n+1)
print("_________________________________")
for i in range(n+1):
    F[i]=binom.cdf(i,n,p)
    print(f"F(X <= {i}) = {F[i]}")
