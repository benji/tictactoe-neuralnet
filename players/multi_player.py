from player import TicTacToePlayer
import random


class MultiPlayer(TicTacToePlayer):
    def __init__(self, name, players, player_probabilities=None):
        TicTacToePlayer.__init__(self, name)
        self.players = players
        self.player_probabilities = player_probabilities
        if not self.player_probabilities:
            self.player_probabilities = [1 for _ in self.players]

    def play(self, game, player_idx):
        player_idx = None
        threshold = 0
        r = random.uniform(0, sum(self.player_probabilities))
        for player_proba in self.player_probabilities:
            threshold = threshold+player_proba
            if r < threshold:
                break
            player_idx += 1
        #player_idx = random.randint(0, len(self.players)-1)
        return self.players[player_idx].play(game, player_idx)
