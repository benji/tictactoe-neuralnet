import random
from copy import copy, deepcopy
import numpy as np
from keras.wrappers.scikit_learn import KerasClassifier
from keras.models import model_from_json

from game import TicTacToeGame
from player import TicTacToePlayer


model = model_from_json(open('model_architecture.json').read())
model.load_weights('model_weights.h5')
model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])

for board in [[0,0,0,0,1,0,0,0,0],[1,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0]]:
  X = np.array(board)
  if (X.ndim == 1):
      X = np.array([X])
  y = model.predict([X])
  print board, y