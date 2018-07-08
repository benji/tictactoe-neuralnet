import numpy as np
import sys


SCORE_USED_OCCUPIED_TILE = -1
SCORE_FOUND_AVAILABLE_TILE = 1
SCORE_WIN = 10

PLAYERS_BOARD_VALUES = [-1, 1]


class TicTacToeGame:
    '''
    Board:
    0 -> not occupied
    1 -> player 1
    -1 -> player 2
    '''

    def __init__(self, size=3):
        self.size = size
        self.board = np.zeros((self.size, self.size), dtype=int)
        self.players = [None, None]
        self.play_count = 0
        self.over = False
        self.history = []
        self.winner_idx = None

    def register_players(self, p1, p2):
        self.players[0] = p1
        self.players[1] = p2

    def play(self, print_game=False):
        if self.over:
            raise 'Game is over.'
        player_idx = self.play_count % 2
        board_value = PLAYERS_BOARD_VALUES[player_idx]

        player = self.players[player_idx]
        x, y = player.play(self)

        if not self.is_tile_available(x, y):
            opponent_idx = 1-player_idx
            self.end_game('Board position already occupied.', opponent_idx)
            return

        self.history.append((x, y, board_value))
        self.board[x][y] = board_value

        if print_game:
            self.print_game()

        self.play_count = self.play_count+1

    def end_game(self, reason, winner_idx):
        self.winner_idx = winner_idx
        winner = self.players[winner_idx]
        print reason
        print 'Player {} wins'.format(winner.name)
        self.over = True
        return

    def print_game(self):
        for a in self.board:
            for v in a:
                if v == 0:
                    sys.stdout.write(' ')
                elif v == 1:
                    sys.stdout.write('X')
                elif v == -1:
                    sys.stdout.write('O')
            print ''

    def is_tile_available(self, x, y):
        return self.board[x][y] == 0

    def print_moves(self):
        print self.history

    def serialize_training_data(self):
        # all the moves made by the winner
        training_data = []
        # keep track of the board over time
        replay_board = np.zeros((self.size, self.size), dtype=int)

        for x, y, val in self.history:
            is_winner_move = val == PLAYERS_BOARD_VALUES[self.winner_idx]

            if is_winner_move:
                ser_vals = []

                # save board state
                for row in replay_board:
                    for rep_val in row.tolist():
                        ser_vals.append(str(rep_val))
                s = '|'.join(ser_vals)+'|'

                # save winner's move
                for bx in xrange(self.size):
                    for by in xrange(self.size):
                        s = s+str(1 if x == bx and y == by else 0)

                training_data.append(s)

            replay_board[x][y] = val

        return training_data
