secret = 22

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You've guessed it - congratulations! It's number 22.")
        break
    else:
        print("Sorry, your guess is not correct... The secret number is not " + str(guess))
