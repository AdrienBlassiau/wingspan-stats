

class Color:
    """
    This class manages the colors of each source of points.
    """
    def __init__(self, birds, bonus_cards, end_of_round_goals, eggs, food_on_cards, tucked_cards, nectars):
        self.birds = birds
        self.bonus_cards = bonus_cards
        self.end_of_round_goals = end_of_round_goals
        self.eggs = eggs
        self.food_on_cards = food_on_cards
        self.tucked_cards = tucked_cards
        self.nectars = nectars

    def get_color(self, parameter_name):
        """
        This function returns the color of a source of score.
        :param parameter_name:    The name of the attribute we want to get the color.
        :return:                  The color of a source of score.
        """
        if parameter_name == "birds":
            return self.format_color(self.birds)
        elif parameter_name == "bonus_cards":
            return self.format_color(self.bonus_cards)
        elif parameter_name == "end_of_round_goals":
            return self.format_color(self.end_of_round_goals)
        elif parameter_name == "eggs":
            return self.format_color(self.eggs)
        elif parameter_name == "food_on_cards":
            return self.format_color(self.food_on_cards)
        elif parameter_name == "tucked_cards":
            return self.format_color(self.tucked_cards)
        elif parameter_name == "nectars":
            return self.format_color(self.nectars)

    def format_color(self, color):
        return "#"+color

