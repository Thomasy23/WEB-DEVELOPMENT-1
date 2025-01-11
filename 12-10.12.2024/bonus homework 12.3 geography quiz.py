import random

# Slovar držav in njihovih prestolnic
countries_cities = {
    "Austria": "Vienna",
    "Croatia": "Zagreb",
    "Spain": "Madrid",
    "Slovenia": "Ljubljana"
}

def geography_quiz():
    print("Welcome to the Geography Quiz!")
    play_again = True

    while play_again:
        # Izberemo naključno državo
        country = random.choice(list(countries_cities.keys()))
        correct_capital = countries_cities[country]

        # Postavimo vprašanje uporabniku
        print(f"\nGame: What is the capital city of {country}?")
        user_answer = input("User: ").strip()

        # Preverimo odgovor
        if user_answer.lower() == correct_capital.lower():
            print("Game: This is correct!")
        else:
            print(f"Game: Sorry, the correct answer is {correct_capital}.")

        # Vprašamo uporabnika, če želi igrati še enkrat
        play_again_input = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again_input != "yes":
            play_again = False

    print("Thank you for playing the Geography Quiz!")

# Zaženemo kviz
if __name__ == "__main__":
    geography_quiz()
