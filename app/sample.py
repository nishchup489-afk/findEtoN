# method 1 : built in `e` , most simple way



#code uncomment from here ⬇️
# ----------------------------------------------------------------------



# import math 

# n = int(input('Enter number of digit you want after decimal: '))

# def get_e(n):
#     return f"{math.e:.{n}f}"

# print(get_e(n))




# ------------------------------------------------------------------------

# problem : 50 max digits
# ===========================






# method 2 : Tylor series -> $e = \sum \frac{1}{n!}$
# easy and if used with Decimal , much better

from decimal import Decimal , getcontext
from math import factorial
import time

inp = int(input("Enter number of digit you want after decimal: "))

def get_e_in_way_2(n):
    getcontext().prec = n+2
    e = Decimal(0)

    for i in range(n+5):
        e += Decimal(1) / Decimal(factorial(i))
    return str(e)[:n+2]
        


def get_e(n):
    getcontext().prec = n+2

    e = Decimal(2)
    term = Decimal(1)

    for i in range(2, n+5):
        term /= i # faster than 1/factorial(n)
        e += term

        if term < Decimal(10)**-(n + 2):
            break

    return str(e)[:n+2]
    
start = time.time()
res1 = get_e(inp)
end1 = time.time()
print(f"Fast Way: {res1} (Time: {end1-start:.6f}s)")
print(get_e(inp))

start = time.time()
res2 = get_e_in_way_2(inp)
end2 = time.time()
print(f"Slow Way: {res2} (Time: {end2-start:.6f}s)")
print(get_e_in_way_2(inp))

