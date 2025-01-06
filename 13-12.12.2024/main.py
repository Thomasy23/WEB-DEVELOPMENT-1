class Player:
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.0462262
        return pounds


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        # self.first_name = first_name
        # self.last_name = last_name
        # self.height_cm = height_cm
        # self.weight_kg = weight_kg
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


messi = FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=190, weight_kg=90, goals=100, yellow_cards=0, red_cards=0)
print(messi.first_name)
print(messi.weight_to_lbs())


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


doncic = BasketballPlayer(
    first_name="Luka",
    last_name="Doncic",
    height_cm=190,
    weight_kg=90,
    points=92.2,
    rebounds=10,
    assists=10.5,
)

lebron = BasketballPlayer(
    first_name="Lebron",
    last_name="James",
    height_cm=206,
    weight_kg=113,
    points=27.2,
    rebounds=7.3,
    assists=5.5,
)

doncic_pounds = doncic.weight_to_lbs()
print(doncic_pounds)
print(doncic.first_name)
print(lebron.first_name)
