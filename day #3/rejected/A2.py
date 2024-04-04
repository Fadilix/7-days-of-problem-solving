import math

x = int(input())


def isEven(n):
    return n % 2 == 0


def divisors(n):
    div = set()
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            div.add(i)
            div.add(n // i)
    return list(div)


divOfx = divisors(x)
count = 0
while x:
    if isEven(x):
        count += 1
        x //= 2
    else:
        if not divOfx:
            break
        max_ = max(divOfx)
        x //= max_
        divOfx.remove(max_)
        count += 1
print(count)
