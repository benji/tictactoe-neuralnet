# tictactoe-neuralnet
Using a Neural Network to play Tic Tac Toe

3x3 board
  0:  unoccupied tile
  1:  own tile
  -1: opponent's tile

INPUT: 9 values [-1,0,-1]
ex: -1,1,0,0,1,-1,-1,0,1

OUTPUT: board value (for own tiles, value 1)

Board valuations:
if player's move resulted in a win at the end of the game  -> 1
if player's move resulted in a loss at the end of the game -> 0