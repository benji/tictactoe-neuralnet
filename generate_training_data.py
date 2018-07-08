from game import TicTacToeGame
from random_player import RandomTicTacToePlayer

p1 = RandomTicTacToePlayer('randbot1')
p2 = RandomTicTacToePlayer('randbot2')

n_games = 10000

with open('training.dat', 'w') as file:
    for _ in xrange(n_games):
        game = TicTacToeGame(size=3)
        game.register_players(p1, p2)
        while not game.over:
            game.play(print_game=False)
        for data in game.serialize_training_data():
            file.write(data+'\n')
