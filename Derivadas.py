import math

def f(x):
    return math.log(x)

def diff(x, h):
    d = (f(x+h)-f(x))/h
    print(d)

diff(1.8, 0.1)
diff(1.8, 0.01)
diff(1.8, 0.001)

def g(t):
    return t*math.e**t

def difg1(t, h):
    d = 1/(2*h)*(-3*g(t)+4*g(t+h)-g(t+2*h))
    return d

def difg2(t, h):
    d = 1/(2*h)*(g(t+h)-g(t-h))
    return d

def difg3(t, h):
    d = 1/(2*h)*(g(t-2*h)-4*g(t-h)+3*g(t))
    return d

a = difg1(2, 0.01)
b = difg2(2, 0.01)
c = difg3(2, 0.01)

delta1 = 22.167168 - a
delta2 = 22.167168 - b
delta3 = 22.167168 - c

print(a, b, c)
print(delta1, delta2, delta3)

difs = [delta1, delta2, delta3]

print(min(difs))
