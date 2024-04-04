seen = [-1] * 10000

Q = int(input())
for caseNum in range(Q):
    k = int(input())
    for i in range(k):
        seen[i] = -1

    f0, f1, n = 1 % k, 1 % k, 2
    while True:
        f2 = (f0 + f1) % k

        if seen[f2] != -1:
            print(seen[f2])
            break
        seen[f2] = n
        f0, f1 = f1, f2
        n += 1
