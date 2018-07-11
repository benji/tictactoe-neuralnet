import random
from copy import copy, deepcopy
import numpy as np
from keras.wrappers.scikit_learn import KerasClassifier
from keras.models import model_from_json

from player import TicTacToePlayer


class NeuralNetPlayer(TicTacToePlayer):
    def __init__(self, name, random=False):
        TicTacToePlayer.__init__(self, name)

        self.random = random

        # Loads trained model
        self.model = model_from_json(
            open('trained_models/{}_architecture.json'.format(name)).read())
        self.model.load_weights('trained_models/{}_weights.h5'.format(name))
        self.model.compile(loss='categorical_crossentropy',
                           optimizer='adam', metrics=['accuracy'])

    def play(self, game, player_idx):
        available_tiles = game.get_available_tiles()

        rated_moves = {}

        # Evaluates all possible moves
        for tile in available_tiles:
            board_copy = deepcopy(game.board)

            board_copy[tile[0]][tile[1]] = -1 if player_idx == 1 else 1

            board_array = game.board_to_array(board_copy, player_idx)
            y = self.predict(board_array)

            score = y[0][0]
            rated_moves[score] = tile

        sorted_scores = sorted(rated_moves.keys(), reverse=True)
        #for sc in sorted_scores:
        #    print rated_moves[sc], sc

        if not self.random:
            return rated_moves[sorted_scores[0]]

        # introduce some kind of randomness
        required_proba = .5
        i = 0
        while i < len(sorted_scores)-1:
            if random.uniform(0, 1) < required_proba:
                return rated_moves[sorted_scores[i]]
            i = i+1

        return rated_moves[sorted_scores[-1]]

    def predict(self, board_array):
        X = np.array(board_array)
        if (X.ndim == 1):
            X = np.array([X])
        return self.model.predict(X)

    def print_weigths(self):
        print self.model.summary()
        for i in range(len(self.model.layers)):
            print 'Layer {}'.format(i)
            layer = self.model.layers[i]
            all_weigths = layer.get_weights()
            for weigths in all_weigths:
                print weigths
