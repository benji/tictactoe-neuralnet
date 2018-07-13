from game import TicTacToeGame
from players import *

p1 = RandomTicTacToePlayer('randbot1')
p2 = RandomTicTacToePlayer('randbot2')

training_data_desired_size = 1000000

# find ratio
factor=1.2
desired_games_per_board_size = {}
desired_game_ratio_per_board_size = {1: 9}
for board_size in range(2, 9):
    desired_game_ratio_per_board_size[board_size] = desired_game_ratio_per_board_size[board_size-1]*factor
print desired_game_ratio_per_board_size

total = sum(desired_game_ratio_per_board_size.values())
if training_data_desired_size < total:
    raise 'Not enough training data requested to produce meaningful training set.'

for board_size in range(1, 9):
    desired_games_per_board_size[board_size] = int(
        desired_game_ratio_per_board_size[board_size]*1.0*training_data_desired_size/total)

total = sum(desired_games_per_board_size.values())
print desired_games_per_board_size, total

collected_games_per_board_size = {}
for board_size in range(1, 9):
    collected_games_per_board_size[board_size] = 0

print_every = 1000

with open('training.dat', 'w') as file:
    game_i = 0
    while sum(collected_games_per_board_size.values()) < total:
        if (game_i+1) % print_every == 0:
            stats = ['{}:{}/{}'.format(bs, collected_games_per_board_size[bs],
                                       desired_games_per_board_size[bs]) for bs in range(1, 9)]
            print '{} games, {}'.format(game_i+1, ' '.join(stats))

        game = TicTacToeGame(size=3, verbose=False)
        game.register_players(p1, p2)

        while not game.over:
            game.play()

        for i, data in enumerate(game.serialize_training_data()):
            board_size = i+1
            if board_size < 9 and collected_games_per_board_size[board_size] < desired_games_per_board_size[board_size]:
                file.write(data+'\n')
                collected_games_per_board_size[board_size] = collected_games_per_board_size[board_size]+1
        game_i = game_i+1

print collected_games_per_board_size

print 'Done.'
