from game import TicTacToeGame
from random_player import RandomTicTacToePlayer
from neuralnet_player import NeuralNetPlayer

n_games = 10000

p1 = RandomTicTacToePlayer('randbot1')
p2 = NeuralNetPlayer('neuralnet')

win_p1 = 0
win_p2 = 0

for _ in xrange(n_games):
    game = TicTacToeGame(size=3)
    game.register_players(p1, p2)
    while not game.over:
        game.play(print_game=False)

    if game.winner_idx is not None:
        if game.winner_idx == 0:
            win_p1 = win_p1+1
        else:
            win_p2 = win_p2+1

    p1pct = win_p1*100/(win_p1+win_p2)
    print "%win {}:{}% {}:{}%".format(p1.name, p1pct, p2.name, 100-p1pct)
