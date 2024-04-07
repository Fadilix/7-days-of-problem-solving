a = input()
b = input()

count = 0
i = 0
while i < len(a):
    if a[i] != b[i]:
        count += 1
    i += 1
print(2 ** count)