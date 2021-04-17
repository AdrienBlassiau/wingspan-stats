import csv

from src.config import Config
from src.game import Game
from src.i18n import I18n
from src.path import Path
from src.player import Player
from src.plot import Plot


class Games:
    """
    This class manages the games list. It is the core class of this project.
    """

    def __init__(self):
        self.games = []  # The list of games
        self.i18n = None  # The translation module

    def run_config(self):
        """
        This function runs the configuration of the project.
        :return:   nothing
        """
        config = Config()
        self.i18n = I18n(config.language)

    def run_import(self):
        """
        This function imports the scores from the score file
        :return:    nothing
        """
        with open(Path.get_score_path(), newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
            current_number = -1
            game = None
            row_count = 0
            for row in csv_reader:
                if row_count > 0:
                    number = int(row[0])
                    player_name = str(row[1])
                    birds = int(row[2])
                    bonus_cards = int(row[3])
                    end_of_round_goals = int(row[4])
                    eggs = int(row[5])
                    food_on_cards = int(row[6])
                    tucked_cards = int(row[7])
                    nectars = int(row[8])
                    game_type = int(row[9])
                    player = Player(player_name, birds, bonus_cards, end_of_round_goals, eggs, food_on_cards,
                                    tucked_cards,
                                    nectars, game_type, number)
                    if number != current_number:
                        current_number = number
                        if game is not None:
                            self.add_game(game)
                        game = Game(number)
                        game.add_player(player)
                    else:
                        game.add_player(player)
                row_count += 1
        if self.nb_games() > 0:
            self.add_game(game)

    def add_game(self, game):
        """
        This function adds a game
        :param game:
        :return:
        """
        self.games.append(game)

    def nb_games(self):
        return len(self.games)

    def get_winner_dict(self):
        winner_dict = {}
        for g in self.games:
            winners = g.get_winners()
            for winner in winners:
                if winner not in winner_dict:
                    winner_dict[winner] = 1
                else:
                    winner_dict[winner] += 1
        return winner_dict

    def get_loser_dict(self):
        loser_dict = {}
        for g in self.games:
            losers = g.get_losers()
            for loser in losers:
                if loser not in loser_dict:
                    loser_dict[loser] = 1
                else:
                    loser_dict[loser] += 1
        return loser_dict

    def get_best(self, type):
        best = -1
        for g in self.games:
            for p in g.get_players():
                if p.get_type_from_string(type) > best:
                    best = p.get_type_from_string(type)
        return best

    def get_worst(self, type):
        worst = 1000
        for g in self.games:
            for p in g.get_players():
                if p.get_type_from_string(type) < worst:
                    worst = p.get_type_from_string(type)
        return worst

    def get_player_number_wins(self, player_name):
        winner_dict = self.get_winner_dict()
        if player_name in winner_dict:
            return winner_dict[player_name]
        return 0

    def get_player_number_loses(self, player_name):
        loser_dict = self.get_loser_dict()
        if player_name in loser_dict:
            return loser_dict[player_name]
        return 0

    def get_player_list(self):
        players_list = []
        for g in self.games:
            players = g.get_players()
            for player in players:
                if player.player_name not in players_list:
                    players_list.append(player.player_name)

        return players_list

    def get_player_games(self, player_name):
        player_games = []
        for g in self.games:
            res = g.find_player(player_name)
            if res:
                player_games.append(res)

        return player_games

    def get_games_where_player(self, player_name):
        games_where_player = []
        for g in self.games:
            res = g.find_player(player_name)
            if res:
                games_where_player.append(g)

        return games_where_player

    def get_player_nb_games(self, player_name):
        return len(self.get_player_games(player_name))

    def get_won_games(self, player_name, included_games=[]):
        won_games = []
        for i in range(0, len(self.games)):
            current_game = self.games[i]
            if (len(included_games) == 0) or (len(included_games) > 0 and current_game.index in included_games):
                if current_game.find_player(player_name):
                    won_games.append(player_name not in current_game.get_winners())
                else:
                    won_games.append(True)
        return won_games

    def get_lost_games(self, player_name, included_games=[]):
        lost_games = []
        for i in range(0, len(self.games)):
            current_game = self.games[i]
            if (len(included_games) == 0) or (len(included_games) > 0 and current_game.index in included_games):
                if current_game.find_player(player_name):
                    lost_games.append(player_name not in current_game.get_losers())
                else:
                    lost_games.append(True)
        return lost_games

    def get_middle_games(self, player_name, included_games=[]):
        middle_games = []
        for i in range(0, len(self.games)):
            current_game = self.games[i]
            if (len(included_games) == 0) or (len(included_games) > 0 and current_game.index in included_games):
                if current_game.find_player(player_name):
                    middle_games.append(player_name not in current_game.get_middlers())
                else:
                    middle_games.append(True)
        return middle_games

    def run_plot(self):
        player_list = self.get_player_list()
        for p in player_list:
            Plot.plot(self, p, self.i18n)
