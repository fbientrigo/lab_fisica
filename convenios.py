import numpy as np
from sympy import *

# errores = [0.1 , 0.2 , 0.1, 1]
# Resultado = 10
# ddf_i = [1, 2, 3, 4]

def error_cuadrado_uv(diF, errores, sqrt = True):
    """
    \Delta F = \sqrt{ \sum_i(\partial_i F \; \Delta x_i)^2  }
    """
    elementoi = []
    for idx, element in enumerate(diF):
        elementoi.append( element* errores[idx] * element * errores[idx] )
    E2 = sum(elementoi)
    if sqrt == True:
        return np.sqrt( float(E2) )
    else:
        return E2

