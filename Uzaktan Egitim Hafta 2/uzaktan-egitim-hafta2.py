from sympy import Symbol

x = Symbol('x')
y = Symbol('y')

p = x*(x + x)
p = (x + 2)*(x + 3)

print(p)

from sympy import factor,expand

expr = x**2 - y**2

factors = factor(expr)
expand = expand(factors)

print(factors,expand)

expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3

factors = factor(expr)

from sympy import pprint
pprint(factors)

x = Symbol('x')
series = x
n = 5
for i in range(2, n+1):
    series = series + (x**i)/i

pprint(series)

expr = x*x + x*y + x*y + y*y
res = expr.subs({x:1, y:2})
print(res)

r = expr.subs({x:1-y})
print(r)

x = Symbol('x')
series = x
n = 5
x_value = 50
for i in range(2, n+1):
    series = series + (x**i)/i

pprint(series)
series_value = series.subs({x:x_value}) #x in alacagi deger belirlenir.
print(series_value)