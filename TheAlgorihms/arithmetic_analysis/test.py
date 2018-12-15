import numpy as np

j = np.float32(425e-9)
v = 425e-9
v2 = 4.25 * 10**-9

jj = np.format_float_scientific(j,precision=15,unique=True)
print(v)
print(v2)
print(j)


