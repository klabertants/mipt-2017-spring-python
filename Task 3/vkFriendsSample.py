import numpy as np


a = np.array([1, 2, 3])
print(a)
a.shape  = ( (len(a), 1) )
for elem in a:
    np.append(elem, 0)
print(a)