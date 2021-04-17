class Player:
    """
    This class describes a player of a game of wingspan.
    It stores all the details of the player game, that's to say his detailed scores.
    """

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
        self.score = birds + bonus_cards + end_of_round_goals + eggs + food_on_cards + tucked_cards + nectars

    def __str__(self):
        """
        This function returns a string description of a player.
        :return:    A string of a player.
        """
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

    def get_type_from_string(self, parameter_name):
        """
        This function returns the attribute of a player according of his parameter_name.
        :param parameter_name:    The name of the attribute we want to return.
        :return:                  The attribute of a player according of his parameter_name.
        """
        if parameter_name == "birds":
            return self.birds
        elif parameter_name == "bonus_cards":
            return self.bonus_cards
        elif parameter_name == "end_of_round_goals":
            return self.end_of_round_goals
        elif parameter_name == "eggs":
            return self.eggs
        elif parameter_name == "food_on_cards":
            return self.food_on_cards
        elif parameter_name == "tucked_cards":
            return self.tucked_cards
        elif parameter_name == "nectars":
            return self.nectars
        elif parameter_name == "score":
            return self.score
        else:
            return self.birds
