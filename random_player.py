import random

from player import TicTacToePlayer


class RandomTicTacToePlayer(TicTacToePlayer):
    def __init__(self, name):
        TicTacToePlayer.__init__(self,name)

    def play(self, game):
        return (random.randint(0, game.size-1), random.randint(0, game.size-1))
