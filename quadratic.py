# Replace the "ANSWER HERE" for your answer
import math

def roots(a, b, c):
    return "ANSWER HERE"
    var1 = (b**2 - 4*a*c)
    if var1 < 0:
        return "( )"
    raiz = math.sqrt(var1)
    resultado1= (-b+raiz)/2*a
    resultado2= (-b-raiz)/2*a
    if resultado1 == resultado2:
        return f"({resultado1})"
    else:
        return f"({resultado1}, {resultado2})"





def value_y(a, b, c, x):
    return "ANSWER HERE"
    imagen= a*(x**2) + b*x + c
    return imagen



def to_string(a, b, c):
    return "ANSWER HERE"
    #a y b y c
    if a and b and c:
        return f"f(x) = {a}* x^2 + {b}* x + {c}"
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
    return "ANSWER HERE"
    if a and b:
        return f"f'(x) = {2 * a} * X + {b}"
    elif not a:
        return f"f'(x) = {c}"
    elif not b:
        return f"f'f(x) = {2 * a} * X"
