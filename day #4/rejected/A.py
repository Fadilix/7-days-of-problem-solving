def fiboMod(mod):
    a = 1
    b = 2
    arr = []
    while True:
        # print(arr)
        a, b = b, a + b
        adding = b % mod
        if adding not in arr:
            arr.append(adding)
        else:
            print(arr)
            print(adding)
            return arr.index(adding)


q = int(input())

arr = []
while q:
    arr.append(int(input()))
    q -= 1

for elem in arr:
    print(fiboMod(elem))