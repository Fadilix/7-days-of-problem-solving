import random
randomNumber = random.randint(1, 1001)
guesses = 10

for _ in range(guesses):
   guess = int(input())
   if guess > randomNumber:
      print("lower")
   elif guess < randomNumber:
      print("higher")
   else:
      print("correct")
