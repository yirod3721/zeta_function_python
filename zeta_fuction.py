import math

def zeta(s, terms):
    result = 0
    for k in range(1, terms):
        result += 1 / (k ** s)
    return result
x = float(input('the number:'))
term = int(input('terms?'))
print(' % .100f ' % zeta(x, term))

