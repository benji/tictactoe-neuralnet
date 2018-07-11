from player import TicTacToePlayer


class StaticPlayer(TicTacToePlayer):
    def __init__(self, name, moves):
        self.moves = moves
        self.move_count = 0
        TicTacToePlayer.__init__(self, name)

    def play(self, game, player_idx):
        next_move = self.moves[self.move_count]
        self.move_count = self.move_count+1
        return next_move
