from game import TicTacToeGame
from random_player import RandomTicTacToePlayer

game1 = TicTacToeGame(size=3)
game1.register_players(RandomTicTacToePlayer('randbot1'),
                       RandomTicTacToePlayer('randbot2'))

while not game1.over:
    game1.play(print_game=True)

print 'Training data:'
print game1.serialize_training_data()