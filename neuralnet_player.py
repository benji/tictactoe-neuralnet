import random
from copy import copy, deepcopy
import numpy as np
from keras.wrappers.scikit_learn import KerasClassifier
from keras.models import model_from_json

from player import TicTacToePlayer


class NeuralNetPlayer(TicTacToePlayer):
    def __init__(self, name):
        TicTacToePlayer.__init__(self, name)
        '''
        Loads trained model
        '''
        self.model = model_from_json(open('model_architecture.json').read())
        self.model.load_weights('model_weights.h5')
        self.model.compile(loss='categorical_crossentropy',
                           optimizer='adam', metrics=['accuracy'])

    def play(self, game, player_idx):
        available_tiles = game.get_available_tiles()
        best_tile = None
        best_score = None

        for tile in available_tiles:
            board_copy = deepcopy(game.board)  # possible board configuration
            board_copy[tile[0]][tile[1]] = -1 if player_idx == 1 else 1
            X = np.array(game.board_to_array(board_copy, player_idx))
            if (X.ndim == 1):
                X = np.array([X])
            y = self.model.predict([X])
            #print y
            i = np.argmax(y)
            score = y[0][i]
            if i == 0:
                if best_score is None or score > best_score:
                    best_score = score
                    best_tile = tile

        if best_tile is not None:
            return best_tile

        # for now default to rand
        random_tile_idx = random.randint(0, len(available_tiles)-1)
        return available_tiles[random_tile_idx]
