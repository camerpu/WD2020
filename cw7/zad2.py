import numpy as np
a = np.arange(12).reshape(3, 4)
b = np.arange(16).reshape(4, 4)
print(a)
print(b)

print(b.min(axis=0))
print(b.min(axis=1))

print(a.min(axis=0))
print(a.min(axis=1))