print("*** WELCOME TO MOOD CHECKING APP ***")
print("")
mood = input("Can you tell me your mood, please? ")

if mood == "happy":
    print("It is great to see you happy!")
elif mood == "nervous":
    print("Take a deep breath 3times.")
elif mood == "sad":
    print("How can we cheer you up? :(")
elif mood == "excited":
    print("What are you waiting for?")
elif mood == "relaxed":
    print("Oh, nice!")
else:
    print("I have no idea about your mood")
