import math
def roots(a, b, c):
    var1 = b**2-4*a*c
    if var1 < 0:
        return "( )"
        
    raiz = math.sqrt(var1)
    result1= (-b+raiz)/2*a
    result2= (-b-raiz)/2*a
    if result1==result2:
        return f"({result1})"
    else:
        return f"({result1}, {result2})"
def value_y(a, b, c, x):
    imagen= a*(x**2) + b*x + c
    return imagen

def to_string(a, b, c):
    #a y b y c
    if a and b and c:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    #b y c
    elif b and c:
        return f"f(x) = {b} * X + {c}"
    #a y c
    elif a and c:
        return f"f(x) = {a} * X^2 + {c}"
    #c y no a y no b
    elif not a and not b and c:
        return f"f(x) = {c}"

def derivation(a, b, c):
    if a and b:
        return f"f'(x) = {2 * a} * X + {b}"
    elif not a:
        return f"f'(x) = {b}"
    elif not b:
        return f"f'(x) = {2 * a} * X"
