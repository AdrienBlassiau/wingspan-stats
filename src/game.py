class Game:
    def __init__(self, index):
        self.index = index
        self.player_number = 0
        self.players = []

    def __str__(self):
        game_string =  '=> Game n°{index} : \n'.format(index=self.index)
        for p in self.players:
            game_string += str(p)
        return game_string

    def add_player(self, player):
        self.players.append(player)
        self.player_number += 1

    def find_player(self, player_name):
        for p in self.players:
            if p.player_name == player_name:
                return p
        return None

    def get_player_score(self, player_name):
        player = self.find_player(player_name)
        if player:
            return player.score
        return None

    def get_players(self):
        return self.players

    def get_winners(self):
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
        middlers = []
        for p in self.players:
            if p.player_name not in self.get_winners() and p.player_name not in self.get_losers():
                middlers.append(p.player_name)
        return middlers
