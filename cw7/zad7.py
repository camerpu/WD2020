import numpy as np
b = np.arange(6).reshape(2, 3)
print(b)

b = np.sin(b)

print(b)

a = np.arange(6).reshape(2, 3)
print(a)

a = np.sin(a)

print(a)

print(a+b)