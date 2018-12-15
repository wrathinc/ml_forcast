import numpy as np 
from decimal import Decimal

planks_constant = 6.6260701509e-34 
c = np.float(3e8)

v = np.float32(425e-9)

energy =  planks_constant*c/v

waveLenght = lambda c, v : c/v 
waveLenghtoflight = waveLenght(c,v)





test = ("{:.2E}").format(Decimal(energy))

print(test)
print(energy)