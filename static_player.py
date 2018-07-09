import random
from copy import copy, deepcopy
import numpy as np
from keras.wrappers.scikit_learn import KerasClassifier
from keras.models import model_from_json

from player import TicTacToePlayer


class StaticPlayer(TicTacToePlayer):
    def __init__(self, name, moves):
        self.moves = moves
        self.move_count = 0
        TicTacToePlayer.__init__(self, name)

    def play(self, game, player_idx):
        next_move = self.moves[self.move_count]
        self.move_count = self.move_count+1
        return next_move
