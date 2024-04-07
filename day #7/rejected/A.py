# Time limit exceeded for the second test case

import math
from collections import defaultdict
import sys

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def primeFactorDecomposition(n):
    neg = False if n > 0 else True
    currentNumber = n if not neg else n * (-1)
    currentPrime = 2
    numbers = defaultdict(int)
    if neg:
        numbers[-1] =+ 1
    while currentNumber >= currentPrime:
        # print(currentNumber, currentPrime)
        if isPrime(currentPrime):
            while currentPrime <= currentNumber:
                if currentNumber % currentPrime == 0:
                    numbers[currentPrime] += 1
                    currentNumber /= currentPrime
                else:
                    currentPrime += 1
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
    if k < 0:
        break
    sys.stdout.flush()

# while True:
#     n = int(input())
#     print(formatPrimeRepresentation(n))
#     if n < 0:
#         print(formatPrimeRepresentation(n))
#         break

