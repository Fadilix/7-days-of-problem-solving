#TLE
import math
from collections import defaultdict
import sys


def primeFactorDecomposition(n):
    numbers = defaultdict(int)
    if n < 0:
        numbers[-1] = 1
        n = abs(n)
    # Factor out 2s
    while n % 2 == 0:
        numbers[2] += 1
        n //= 2
    # Factor out odd primes
    for i in range(3, math.isqrt(n) + 1, 2):
        while n % i == 0:
            numbers[i] += 1
            n //= i
    # If n is a prime greater than 2
    if n > 2:
        numbers[n] += 1
    return numbers

def formatPrimeRepresentation(numbers: defaultdict):
    ans = ""
    for k, v in numbers.items():
        if v > 1:
            ans += f"{k}^{v} " if v else f"{k} "
        else:
            ans += f" {k} "
    return ans.strip().replace("  ", " ")


while True:
    k = int(input())
    numbers = primeFactorDecomposition(k)
    # print(numbers)
    print(formatPrimeRepresentation(numbers))
    if k.strip() == "":
        break
    sys.stdout.flush()