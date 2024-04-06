def fizzbuzz(candidateOutput, N):
    count = 0
    for i in range(1, N + 1):
        if i % 3 == 0 and i % 5 == 0:
            expected = "fizzbuzz"
        elif i % 3 == 0:
            expected = "fizz"
        elif i % 5 == 0:
            expected = "buzz"
        else:
            expected = str(i)

        if candidateOutput[i - 1] == expected:
            count += 1

    return count

candidates, N = map(int, input().split())

maxCount = -1
winner = -1

for candidate in range(1, candidates + 1):
    output = input().split()
    count = fizzbuzz(output, N)

    if count > maxCount:
        maxCount = count
        winner = candidate

print(winner)