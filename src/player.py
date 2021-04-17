class Player:
    def __init__(self, player_name, birds, bonus_cards, end_of_round_goals, eggs, food_on_cards, tucked_cards, nectars,
                 game_type, index):
        self.player_name = player_name
        self.birds = birds
        self.bonus_cards = bonus_cards
        self.end_of_round_goals = end_of_round_goals
        self.eggs = eggs
        self.food_on_cards = food_on_cards
        self.tucked_cards = tucked_cards
        self.nectars = nectars
        self.game_type = game_type
        self.index = index
        self.score = birds+bonus_cards+end_of_round_goals+eggs+food_on_cards+tucked_cards+nectars

    def __str__(self):
        str = 'player_name: {player_name}\n' \
              '     birds: {birds}\n' \
              '     bonus_cards: {bonus_cards}\n' \
              '     end_of_round_goals: {end_of_round_goals}\n' \
              '     eggs: {eggs}\n' \
              '     food_on_cards: {food_on_cards}\n' \
              '     tucked_cards: {tucked_cards}\n' \
              '     nectars: {nectars}\n' \
            .format(player_name=self.player_name,
                    birds=self.birds,
                    bonus_cards=self.bonus_cards,
                    end_of_round_goals=self.end_of_round_goals,
                    eggs=self.eggs,
                    food_on_cards=self.food_on_cards,
                    tucked_cards=self.tucked_cards,
                    nectars=self.nectars,
                    game_type=self.game_type)
        return str

    def get_type_from_string(self, type):
        if type == "birds":
            return self.birds
        elif type == "bonus_cards":
            return self.bonus_cards
        elif type == "end_of_round_goals":
            return self.end_of_round_goals
        elif type == "eggs":
            return self.eggs
        elif type == "food_on_cards":
            return self.food_on_cards
        elif type == "tucked_cards":
            return self.tucked_cards
        elif type == "nectars":
            return self.nectars
        elif type == "score":
            return self.score
        else:
            return self.birds