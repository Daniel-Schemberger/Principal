import numpy as np

h = 0.2

def f(x,y):
    return y - x +1

xi = np.arange(1, 5.2, h)
yi2 = [-2]
yi4 = [-2]

y0 = yi2[0]
x0 = xi[0]

# DEFININDO RK2
def rk2(y0):
    for i in xi:
        k1 = f(i,y0)
        k2 = f(i+h, y0+h*k1)
        yn = y0 + h/2*(k1+k2)
        yi2.append(yn)
        y0 = yn
    return yi2

# DEFININDO RK4
def rk4(y0):
    for i in xi:
        k1 = f(i,y0)
        k2 = f(i+h/2, y0+h*k1/2)
        k3 = f(i+h/2, y0+h*k2/2)
        k4 = f(i+h, y0+h*k3)
        yn = y0 + h/6*(k1+2*k2+2*k3+k4)
        yi4.append(yn)
        y0 = yn
    return yi4

for k in range(0,22):
    print(round(rk2(y0)[k],2), round(rk4(y0)[k],2))
