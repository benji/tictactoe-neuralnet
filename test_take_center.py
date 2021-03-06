from game import TicTacToeGame
from players import *

p2 = NeuralNetPlayer('neuralnet3')

for y in range(3):
    for x in range(3):
        if x == 1 and y == 1:
            continue
        game = TicTacToeGame(size=3, verbose=False)
        p1 = StaticPlayer('staticplayer', [(x, y)])
        game.register_players(p1, p2)
        game.play()
        game.play()
        game.print_board()
        if game.board[1][1] == 0:
            print 'WARNING: Player has not taken the center!'
        print ''
