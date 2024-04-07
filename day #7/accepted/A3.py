import sys
from collections import defaultdict

def factorize(n):
    factors = defaultdict(int)

    if n < 0:
        factors[-1] += 1
        n *= -1

    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            factors[i] += 1
        i += 1

    if n > 1:
        factors[n] += 1

    return factors

def main():
    for line in sys.stdin:
        if line.strip() == "":
            break

        n = int(line.strip())
        factors = factorize(n)
        
        for factor, count in factors.items():
            if count == 1:
                print(f"{factor} ", end='')
            else:
                print(f"{factor}^{count} ", end='')
        
        print()