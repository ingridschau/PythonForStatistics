from scipy.stats import norm
import math

alpha = 0.5
n = 12
X = 2015.42
sigma = 50

z_alpha = abs(norm.ppf(alpha/2))
lower_limit = X - sigma / math.sqrt(n) * z_alpha
upper_limit = X + sigma / math.sqrt(n) * z_alpha

print(f'{float("{:.1f}".format(100*(1-alpha)))}% -confidence Z-interval for
average radon radiation (i Bq/m3)
t=[{float("{:.9f}".format(lower_limit))};
{float("{:.9f}".format(upper_limit))}]')
