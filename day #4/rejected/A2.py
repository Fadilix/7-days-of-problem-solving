a = 1
b = 2
arr = []
Q = int(input())

while Q:
    arr.append(int(input()))
    Q -= 1

contains = []
for elem in arr:
    while True:
        newB = b % elem
        a, b = b, (a + b) % elem
        if newB not in contains:
            contains.append(newB)
        else:
            print(contains.index(newB))
            break
