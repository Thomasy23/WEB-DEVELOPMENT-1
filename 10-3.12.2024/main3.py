import random

secret = random.randint(1, 30)
attempts = 0

while True:
    guess = int(input("Enter your guess:"))
    attempts = attempts + 1
    # attempts+= 1

    if guess == secret:
        print("You have guessed! It is number {0} and you needed {1} attempts".format(str(secret), str(attempts)))
        break
    elif guess > secret:
        print("Your guess is not correct. Try smaller!")
    else:
        print("Your guess is not correct. Try bigger!")
