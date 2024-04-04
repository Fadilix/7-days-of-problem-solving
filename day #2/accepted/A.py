from math import factorial as f

T = int(input())
arr = []
while T:
    N = int(input())
    arr.append(N)
    T -= 1

for i in arr:
    print(str(f(i))[-1])