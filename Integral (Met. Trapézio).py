#Integrais método do trapézio

import math

def f(x):
    return math.e**x

#no intervalo (0,1)

#Aproximação da área de integral por trapézios

#n=1
h1 = 1
I1 = (f(1)+f(0))*h1/2
print(I1)

#n=2
h2 = 1/2
I2 = (f(1)+2*f(0.5)+f(0))*h2/2
print(I2)

#n=4
h4 = 1/4
I4 = (f(0)+2*f(0.25)+2*f(0.5)+2*f(0.75)+f(1))*h4/2
print(I4)

h = [h1, h2, h4]
I = [I1, I2, I4]

def erro(x,y):
    a = (1.712828-y)*x/2
    return a

#Erro relativo

for i in h:
    for j in I:
        erro(i,j)
        print(f'Com aproximação {i}, o valor aproximado = {j}')
        print(f'Erro relativo = {erro(i,j)}')

#Para n intervalos

n = int(input('valor de n = '))

h_var = 1/n
print(h_var)

def lista(a,b,n):
    dx = (b-a)/n
    x = []
    i = 0
    while len(x)<=n:
        x.append(a+i*dx)
        i+=1
    return x

lista = lista(0,1,n)
print(lista)

def f(x):
    return math.e**x

sum = sum(list(map(f,lista))) - (f(1)+f(0))
print(sum)

def I_var(h_var):
    b = (f(1)+f(0)+2*sum)*h_var/2
    return b

print(I_var(h_var))

