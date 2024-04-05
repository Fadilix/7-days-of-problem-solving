import string
import random

vowels = "aeiou"
consonants = "".join(x for x in string.ascii_lowercase if x not in vowels)

n = int(input())


def randomName():
    return "".join(random.choice(vowels) + random.choice(consonants) for _ in range(5))


names = set()
while len(names) < n:
    names.add(randomName())

for x in names:
    print(x)
