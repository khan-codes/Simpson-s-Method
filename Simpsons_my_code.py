import random

from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)

def phi(a, b):
    n = random.randint(a+1, b-1)
    return n

def f(x):
    return (x + 1)**-1


def simpsons_rule(f, a, b):
    h = (b-a)/2
    E = phi(a, b)
    
    sum1 = f(a) + 4 * f(phi(a, b)) + f(b)
    sum1 *= h/3

    sum2 = h**5/90
    sum2 *= diff(f(E), x, x, x, x)     #4th derivative of f(E)

    total_sum = sum1 - sum2
    return total_sum


print(simpsons_rule(f, 0, 2))