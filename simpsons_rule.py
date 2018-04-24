from math import *
from sympy import *

# Method itself
def Simpson(f, a, b, n):

    h = (b - a)/float(n)
        
    sum1 = 0
    for i in range(1, n/2 + 1):
        sum1 += f(a + (2*i - 1)*h)
        
    sum1 *= 4
    sum2 = 0
    
    for i in range(1, n/2):
        sum2 += f(a + 2*i*h)
        
    sum2 *= 2
    approx = (b - a)/(3.0*n)*(f(a) + f(b) + sum1 + sum2)
    return approx

# Define the function
def f(x):
    return sin(x)

# Main execution
print "Simpson approximation of sin(x)"

for n in 2,4,6:
    print 'For n=%i:   approx=%f' % \
    (n, Simpson(f, 0, 2, n))
