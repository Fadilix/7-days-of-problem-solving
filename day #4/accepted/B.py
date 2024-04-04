def getPrimeFactors(num):
    factors = []
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors

while True:
    n = int(input())
    if n == 4:
        break
    times = 0
    while True:
        times += 1
        factors = getPrimeFactors(n)
        if len(factors) == 1:
            print(factors[0], times)
            break
        n = sum(factors)
