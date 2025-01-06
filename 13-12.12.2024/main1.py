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

    def get_avg_yellow_cards_per_game(self, games_played):
        return games_played / self.yellow_cards


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


messi = FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=190, weight_kg=90, goals=100, yellow_cards=10, red_cards=0)
avg_ylw_cards = messi.get_avg_yellow_cards_per_game(150)
print(avg_ylw_cards)
