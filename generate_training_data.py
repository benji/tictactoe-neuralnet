from game import TicTacToeGame
from players import *

settings = [
    {
        'n_games': 50000,
        'p1':RandomTicTacToePlayer('rand1'),
        'p2':RandomTicTacToePlayer('rand2')
    }
]

file = open('training.dat', 'w')

for setting in settings:
    p1 = setting['p1']
    p2 = setting['p2']
    n_games = setting['n_games']

    win_p1 = 0
    print_every = 500

    for i in xrange(n_games):
        if (i+1) % print_every == 0:
            print '{}/{}'.format(i+1, n_games)
        game = TicTacToeGame(size=3, verbose=False)
        game.register_players(p1, p2)
        while not game.over:
            game.play()
        if game.winner_idx == 0:
            win_p1 = win_p1+1
        for data in game.serialize_training_data():
            file.write(data+'\n')
        # game.print_game()

    p1pct = win_p1*100/n_games
    print "%win P1:{}% P2:{}%".format(p1pct, 100-p1pct)

file.close()