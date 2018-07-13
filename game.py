import numpy as np
import sys
from copy import copy, deepcopy

SCORE_USED_OCCUPIED_TILE = -1
SCORE_FOUND_AVAILABLE_TILE = 1
SCORE_WIN = 10

PLAYERS_BOARD_VALUES = [1, -1]


class TicTacToeGame:
    '''
    Board:
    0 -> not occupied
    1 -> player 1
    -1 -> player 2
    '''

    def __init__(self, size=3, verbose=True):
        self.size = size
        self.board = np.zeros((self.size, self.size), dtype=int)
        self.players = [None, None]
        self.play_count = 0
        self.over = False
        self.history = []
        self.winner_idx = None
        self.verbose = verbose
        if self.verbose:
            print '== New game =='

    def register_players(self, p1, p2):
        self.players[0] = p1
        self.players[1] = p2

    def play(self):
        if self.over:
            raise 'Game is over.'
        player_idx = self.play_count % 2
        board_value = PLAYERS_BOARD_VALUES[player_idx]

        player = self.players[player_idx]
        x, y = player.play(self, player_idx)

        if not self.is_tile_available(x, y):
            opponent_idx = 1-player_idx
            self.end_game('Board position already occupied.', opponent_idx)
            return

        self.history.append((x, y, board_value))
        self.board[x][y] = board_value

        self.play_count = self.play_count+1

        if self.has_winner():
            self.end_game('3 in a row.', player_idx)
            return

        if self.play_count == self.size*self.size:
            self.end_game('Board is full.', None)

    def has_winner(self):
        # horizontals
        for y in xrange(self.size):
            arr = [self.board[x][y] for x in range(self.size)]
            if self.array_all_same_player(arr):
                #print '3 horizontal '+str(y)
                return True
        # verticals
        for x in xrange(self.size):
            arr = [self.board[x][y] for y in range(self.size)]
            if self.array_all_same_player(arr):
                #print '3 vertical '+str(x)
                return True
        # diagonals
        arr = [self.board[x][x] for x in range(self.size)]
        if self.array_all_same_player(arr):
            # print '3 diagonal #1'
            return True
        arr = [self.board[x][self.size-x-1] for x in range(self.size)]
        if self.array_all_same_player(arr):
            # print '3 diagonal #2'
            return True
        return False

    def array_all_same_player(self, arr):
        firstval = arr[0]
        if firstval == 0:
            return False
        for i in range(1, len(arr)):
            if arr[i] != firstval:
                return False
        return True

    def end_game(self, reason, winner_idx):
        self.winner_idx = winner_idx
        if self.verbose:
            if self.winner_idx is None:
                print 'Draw.'
            else:
                winner = self.players[winner_idx]
                print reason
                print 'Player {} wins.'.format(winner.name)
        self.over = True

    def print_board(self, borders=False):
        if borders:
            print '-----'
        for y in range(self.size):
            if borders:
                sys.stdout.write('|')
            for x in range(self.size):
                v = self.board[x][y]
                c = self.get_print_char(v)
                sys.stdout.write(c)
            if borders:
                sys.stdout.write('|')
            print ''
        if borders:
            print '-----'

    def get_print_char(self, v):
        if v == 0:
            return '.'
        elif v == 1:
            return 'X'
        elif v == -1:
            return 'O'

    def print_game(self):
        for row in range(self.size):  # for each row
            vals = [0, 0, 0]
            sys.stdout.write('  ')
            for x, y, v in self.history:  # replay history
                if y == row:  # is move on that row?
                    vals[x] = v
                for v in vals:
                    c = self.get_print_char(v)
                    sys.stdout.write(c)
                sys.stdout.write('  ')
            print ''

    def get_available_tiles(self):
        available_tiles = []
        for x in xrange(self.size):
            for y in xrange(self.size):
                if self.board[x][y] == 0:
                    available_tiles.append((x, y))
        return available_tiles

    def is_tile_available(self, x, y):
        return self.board[x][y] == 0

    def print_moves(self):
        print self.history

    def serialize_training_data(self):
        # all the moves made by the winner
        training_data = []
        # keep track of the board over time
        replay_board = np.zeros((self.size, self.size), dtype=int)

        is_draw = self.winner_idx is None

        replay_play_count = 0
        for x, y, val in self.history:
            player_idx = 0 if val == 1 else 1

            replay_board[x][y] = val
            replay_play_count = replay_play_count + 1

            board_score = None
            
            if is_draw:
                board_score = 0
            else:
                moves_until_end = self.play_count - replay_play_count
                is_winner_move = val == PLAYERS_BOARD_VALUES[self.winner_idx]

                board_score = (self.size*self.size - moves_until_end)
                #board_score = 1 if moves_until_end == 0 else 1
                #board_score = 1 if is_winner_move == 0 else -1

                if not is_winner_move:
                    board_score = -1*board_score

            move_training_data = self.serialize_board_valuation(
                replay_board, player_idx, board_score)

            training_data.append(move_training_data)

        return training_data

    @staticmethod
    def board_to_array(board_data, player_idx):
        arr = []
        for y in range(len(board_data)):
            for x in range(len(board_data)):
                v = board_data[x][y]
                if player_idx == 1:
                    v = -v
                arr.append(v)
        return arr

    def serialize_board_valuation(self, board_data, player_idx, label):
        board_arr = self.board_to_array(board_data, player_idx)
        ser_vals = [str(v) for v in board_arr]
        return '|'.join(ser_vals)+'|'+str(label)
