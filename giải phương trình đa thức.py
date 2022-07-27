import numpy as np

# x^^4 + 4.6x^^3 - 6.8x^^2 + 9.4x - 5.2
coef = [1.0, 4.6, -6.8, 9.4, -5.2]
roots = np.roots(coef)

print(roots)

