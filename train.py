import pandas as pd
import math
import json
import sys
import os
import time
import collections
from tqdm import tqdm
from os import path

import numpy as np
import pandas as pd
from numpy import array


#from sklearn.model_selection import cross_val_score
#from sklearn.model_selection import KFold
#from sklearn.pipeline import Pipeline
#from sklearn.utils import shuffle

# fix random seed for reproducibility
seed = 7
np.random.seed(seed)  # pylint: disable=E1101
# np.random.seed(int(time.time()))

board_size = 3
n_tiles = board_size**2

X_train = []
y_train = []

with open("training.dat", "r") as file:
    for line in file:
        arr = line.strip().split('|')
        board = [int(v) for v in arr[0:len(arr)-1]]
        score = int(arr[len(arr)-1])

        X_train.append(board)
        y_train.append([score])

print 'Loaded training data ({} samples)'.format(len(X_train))

X_train = array(X_train)
y_train = array(y_train)

from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline


def baseline_model():
        # create model
    model = Sequential()
    model.add(Dense(n_tiles, input_dim=n_tiles, activation='relu'))
    model.add(Dense(n_tiles, input_dim=n_tiles, activation='relu'))
    model.add(Dense(n_tiles, input_dim=n_tiles, activation='relu'))
    #model.add(Dense(n_tiles, input_dim=6, activation='relu'))
    model.add(Dense(1, activation='relu'))
    # Compile model
    model.compile(loss='mean_squared_error',
                  optimizer='adam', metrics=['accuracy'])
    return model


estimator = KerasClassifier(build_fn=baseline_model,
                            epochs=300, batch_size=500, verbose=1)

#kfold = KFold(n_splits=3, shuffle=True, random_state=seed)
#results = cross_val_score(estimator, X_train, y_train, cv=kfold)
#print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))

estimator.fit(X_train, y_train)

modelname = 'neuralnet2'
print 'Saving model {}...'.format(modelname)
json_model = estimator.model.to_json(indent=4)
open('trained_models/{}_architecture.json'.format(modelname), 'w').write(json_model)
estimator.model.save_weights(
    'trained_models/{}_weights.h5'.format(modelname), overwrite=True)
