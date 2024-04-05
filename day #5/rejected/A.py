import random

n = int(input())
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
letters = "abcdefghijklmnopqrstuvwxyz"
seen = set()

while len(seen) < n:

    x = random.randint(3, 7)
    L = [random.choice(letters) for _ in range(x)]
    s = "".join(L)

    if s not in seen:
        print(s)
        seen.add(s)
