import sys


def guessNumber(lowerBound, upperBound):
    tries = 0
    while tries <= 10:
        guess = (lowerBound + upperBound) // 2
        print(guess)
        sys.stdout.flush()
        response = input().strip()
        if response == "lower":
            upperBound = guess - 1
        elif response == "higher":
            lowerBound = guess + 1
        elif response == "correct":
            return
        tries += 1


lowerBound = 1
upperBound = 1000

guessNumber(lowerBound, upperBound)
