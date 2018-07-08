from game import TicTacToeGame
from random_player import RandomTicTacToePlayer

p1 = RandomTicTacToePlayer('randbot1')
p2 = RandomTicTacToePlayer('randbot2')

n_games = 10000

win_p1 = 0

with open('training.dat', 'w') as file:
    for _ in xrange(n_games):
        game = TicTacToeGame(size=3)
        game.register_players(p1, p2)
        while not game.over:
            game.play(print_game=False)
        if game.winner_idx == 0:
            win_p1 = win_p1+1
        for data in game.serialize_training_data():
            file.write(data+'\n')

p1pct = win_p1*100/n_games
print "%win P1:{}% P2:{}%".format(p1pct,100-p1pct)
