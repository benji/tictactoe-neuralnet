from game import TicTacToeGame
from random_player import RandomTicTacToePlayer
from neuralnet_player import NeuralNetPlayer

n_games = 1000

p1 = RandomTicTacToePlayer('randbot1')
#p1 = NeuralNetPlayer('neuralnet1')
p2 = NeuralNetPlayer('neuralnet2')

win_p1 = 0
win_p2 = 0
n_draw = 0

for i in xrange(n_games):
    game = TicTacToeGame(size=3, verbose=False)
    game.register_players(p1, p2)
    while not game.over:
        game.play()

    if game.winner_idx is None:
        n_draw = n_draw+1
    else:
        if game.winner_idx == 0:
            # game.print_board(borders=True)
            print 'random bot wins!'
            game.print_game()
            win_p1 = win_p1+1
        else:
            win_p2 = win_p2+1

    p1pct = win_p1*100/(i+1)
    p2pct = win_p2*100/(i+1)
    drawpct = 100-p1pct-p2pct
    print "Game {} -> {}:{}% {}:{}% draw:{}%".format(
        i+1, p1.name, p1pct, p2.name, p2pct, drawpct)
