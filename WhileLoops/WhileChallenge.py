import random

highest = 1000
answer = random.randint(1, highest)
guess = 0
while guess != answer:
    guess = int(input("Please guess a number between 1 and {} : ".format(highest)))
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    else:
        print("Well done you guessed correctly")