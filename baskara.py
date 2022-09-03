from math import sqrt
import numpy as np
a = float(input("Qual valor de A: ?"))
b = float(input("Qual valor de B: ?"))
c = float(input("Qual valor de C: ?"))
delta = (b * b) - (4 * a * c)
print("O valor de DELTA é = ",delta)
raiz = np.sqrt(delta)
x1 = (- b + raiz) / (2 * a)
x2 = (- b - raiz) / (2 * a)
print("O valor de X1 é =  ", x1)
print("O valor de X2 é = ", x2)




