import math


def primeFactors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors


x = int(input())
factors = primeFactors(x)
print(len(factors))
