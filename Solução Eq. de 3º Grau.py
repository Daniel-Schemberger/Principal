print ('Formato geral da equacao de 3° grau é  ax^3+bx^2+cx+d=0')

a=float(input('Digite o valor de a: '))
b=float(input('Digite o valor de b: '))
c=float(input('Digite o valor de c: '))
d=float(input('Digite o valor de d: '))

# Newton Raphson        

x0=(2**0.5)

i = 0

MF = 1.0

while (MF > 10**(-17)):

    F = a*x0**3 + b*x0**2 + c*x0 + d

    dF = 3*a*x0**2 + 2*b*x0 + c

    if dF == 0.0:

        x1 = x0 - F/(dF + 10**(-13))

    else:

        x1 = x0 - F/dF

    F = a*x1**3 + b*x1**2 + c*x1 + d

    MF = abs(F)

    i=i+1

    x0=x1

    if i > 500:

        print ("Não convergiu")

        break

print("x1 = ", x0)

 

# Divisao de polinômios

A = a

B = a*x0 + b

C = a*x0**2 + b*x0 + c

 

# Solução Equação de 2 grau

# Calculo do valor delta

delta = B**2 - 4*A*C

if delta>=0:

    x1=(-B-delta**0.5)/(2*A)

    x2=(-B+delta**0.5)/(2*A)

    print ('x2 = ', x1)

    print ('x3 = ', x2)

elif delta<0:

    raizdelta=complex(0,abs(delta))

    x1=(-B-raizdelta)/(2*A)

    x2=(-B+raizdelta)/(2*A)

    print ('x2 = ', x1)

    print ('x3 = ', x2)