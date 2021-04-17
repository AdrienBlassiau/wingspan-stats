class Game:
    """
    This class manages a game. It describe a game of wingspan.
    """

    def __init__(self, index):
        self.index = index
        self.player_number = 0
        self.players = []

    def __str__(self):
        """
        This function returns a string description of a game.
        :return:    A string of a game.
        """
        game_string = '=> Game n°{index} : \n'.format(index=self.index)
        for p in self.players:
            game_string += str(p)
        return game_string

    def add_player(self, player):
        """
        This function adds a player to a game.
        :param player:  The player we want to add.
        :return:        nothing.
        """
        self.players.append(player)
        self.player_number += 1

    def find_player(self, player_name):
        """
        This function tests if a player with player_name belongs to a game.
        :param player_name:     The name of the player we want to test.
        :return:                The player if it belongs to the games, None otherwise.
        """
        for p in self.players:
            if p.player_name == player_name:
                return p
        return None

    def get_player_score(self, player_name):
        """
        This function returns the total score of a player with player_name.
        :param player_name:     The name of the player.
        :return:                The total score of player_name.
        """
        player = self.find_player(player_name)
        if player:
            return player.score
        return None

    def get_players(self):
        """
        This function returns the list of the players of the game.
        :return:    The list of the players of the game.
        """
        return self.players

    def get_winners(self):
        """
        This function returns a list of the winners (player names) of the games.
        :return:    A list of the winners (player names) of the games.
        """
        winners = []
        best_score = -1
        for p in self.players:
            if p.score >= best_score:
                if p.score != best_score:
                    winners = []
                winners.append(p.player_name)
                best_score = p.score
        return winners

    def get_losers(self):
        """
        This function returns a list of the losers (player names) of the games.
        :return:    A list of the losers (player names) of the games.
        """
        losers = []
        worst_score = 300
        for p in self.players:
            if p.score <= worst_score:
                if p.score != worst_score:
                    losers = []
                losers.append(p.player_name)
                worst_score = p.score
        return losers

    def get_middlers(self):
        """
        This function returns a list of the middlers = no loser, no winner (player names) of the games.
        :return:    A list of the middlers = no loser, no winner  (player names) of the games.
        """
        middlers = []
        for p in self.players:
            if p.player_name not in self.get_winners() and p.player_name not in self.get_losers():
                middlers.append(p.player_name)
        return middlers
