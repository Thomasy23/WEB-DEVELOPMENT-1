import json
import random
import datetime

secret = random.randint(1, 30)
attempts = 0

current_time = datetime.datetime.now()

# a = [5, 10, 15 ]
# element = a[0]
# element = 5

with open("game_state.json", "r") as game_state:
    score_list = json.loads(game_state.read())
    top_scores = sorted(score_list, key=lambda x: x["attempts"])[:3]
    print("-----Top scores------")
    for score in top_scores:
        print("{0} - {1}".format(score.get("name"), str(score.get("attempts"))))

print("\n------Game Start -----")

while True:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess == secret:
        print("You've guessed it!")
        name = input("Enter your name for high score list (optional)")
        if not name:
            name = "Anonymus Player"

        score = {
            "date": str(current_time),
            "attempts": attempts,
            "name": name
        }
        score_list.append(score)
        with open("game_state.json", "w") as game_state:
            game_state.write(json.dumps(score_list))
            break
    elif guess > secret:
        print("Wrong. Guess lower.")
    else:
        print("Wrong. Guess higher.")
