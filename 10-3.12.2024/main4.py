import random

secret = random.randint(1, 30)
attempts = 0

with open("score.txt", "r") as game_score:
    best_score = int(game_score.read())
    print("Top score so far: {0} attempts. You can do better! :)".format(best_score))

while True:
    guess = int(input("Enter your guess:"))
    attempts = attempts + 1
    # attempts+= 1

    if guess == secret:
        print("You have guessed! It is number {0} and you needed {1} attempts".format(str(secret), str(attempts)))

        if attempts < best_score:
            with open("score.txt","w") as game_score:
                game_score.write(str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct. Try smaller!")
    else:
        print("Your guess is not correct. Try bigger!")
