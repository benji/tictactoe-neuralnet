import random

from player import TicTacToePlayer


class RandomTicTacToePlayer(TicTacToePlayer):
    def __init__(self, name):
        TicTacToePlayer.__init__(self, name)

    def play(self, game, player_idx):
        available_tiles = game.get_available_tiles()
        random_tile_idx = random.randint(0, len(available_tiles)-1)
        return available_tiles[random_tile_idx]
