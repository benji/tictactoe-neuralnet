from player import TicTacToePlayer
import random


class MultiPlayer(TicTacToePlayer):
    def __init__(self, name, players):
        TicTacToePlayer.__init__(self, name)
        self.players = players

    def play(self, game, player_idx):
        player_idx = random.randint(0, len(self.players)-1)
        return self.players[player_idx].play(game, player_idx)
