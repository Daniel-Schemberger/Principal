#integral pelo método de 3/8 de Simpson


import math
import numpy as np
import matplotlib.pyplot as plt
#determinando o tamanho do intervalo

def f(x):
    return math.e**x

# função para cálculo da área
def simpson38(x0,xn,n):
    # calculando intervalo
    dx = (xn - x0) / n
    
    # soma
    soma = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*dx
        
        if i%2 == 0:
            soma = soma + 2 * f(k)
        else:
            soma = soma + 3 * f(k)
    
    # área aproximada
    soma = soma * 3 * dx / 8
    
    return soma

print(simpson38(0,1.1,1000))

