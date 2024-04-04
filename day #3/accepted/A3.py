x = int(input())
count = 0
factor = 2

while factor**2 <= x:
    if x % factor == 0:
        x //= factor
        count += 1
    else:
        factor += 1
count += 1
print(count)
