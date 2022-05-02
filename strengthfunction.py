import numpy as np
import matplotlib.pyplot as plt
mu_0 =200
sigma = 50
n = 12
alpha =0.05
mu_min = 180
mu_max = 260
mu = np.linspace(mu_min,mu_max,17)
P=1-norm.cdf((mu_0-mu)/(sigma/np.sqrt(n)) + abs(norm.ppf(alpha)),0,1)
for i in range(17):
 print(f"γ({mu[i]}) = {P[i]}")
plt.plot(mu,P)
plt.xlim(mu_min,mu_max)
plt.ylim(0,1.05)
plt.title("Styrkefunksjonenen for
radonstråling",fontsize=14,color="orange")
plt.grid(axis="both")
plt.show()
