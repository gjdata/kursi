# import sys
# sys.setrecursionlimit(10000)

import functools

# N draudzenes
# Pirmajā vietā A rozes tiek pārdotas par B latiem, otrajā C rozes tiek pārdotas par D latiem
N, A, B, C, D = map(int, input().split())

@functools.lru_cache()
def dynamic(roses):
    if A >= roses:
        a_b_price = B
    else:
        a_b_price = B + dynamic(roses - A)

    if C >= roses:
        c_d_price = D
    else:
        c_d_price = D + dynamic(roses - C)

    return min(a_b_price, c_d_price)


def gcd(u, v):
    while v:
        u, v = v, u % v
    return u


def lcm(a, b):
    return (a * b) // gcd(a, b)


price1 = B / A
price2 = D / C

cm = lcm(A, C)
reminder = N % cm
whole = N - reminder

if price1 > price2:
    cheap = (whole // C) * D
    print(cheap + dynamic(reminder))
else:
    cheap = (whole // A) * B
    print(cheap + dynamic(reminder))


