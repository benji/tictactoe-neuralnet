# tictactoe-neuralnet
Using a Neural Network to play Tic Tac Toe

3x3 board:
*  0:  unoccupied tile  
*  1:  own tile  
*  -1: opponent's tile  

INPUT: 9 values [-1,0,-1]  
example: -1,1,0,0,1,-1,-1,0,1

OUTPUT: board value (for own tiles, value 1)

Board valuations:  
if game ends with a draw:
  all successive board positions are valued at 0
otherwise:
  score is (9 - number of moves before end of game)

Example: A victorious move will make the resulting board position valued at 9

##Sample output
```Game 396 -> randbot1:4% neuralnet2:90% draw:6%
random bot wins!
  ..X  ..X  .XX  OXX  OXX  OXX  OXX  
  ...  .O.  .O.  .O.  .O.  OO.  OOX  
  ...  ...  ...  ...  ..X  ..X  ..X  
Game 397 -> randbot1:4% neuralnet2:90% draw:6%
Game 398 -> randbot1:4% neuralnet2:90% draw:6%
Game 399 -> randbot1:4% neuralnet2:90% draw:6%
Game 400 -> randbot1:4% neuralnet2:90% draw:6%
Game 401 -> randbot1:4% neuralnet2:90% draw:6%
Game 402 -> randbot1:4% neuralnet2:90% draw:6%
Game 403 -> randbot1:4% neuralnet2:90% draw:6%
Game 404 -> randbot1:4% neuralnet2:90% draw:6%
Game 405 -> randbot1:4% neuralnet2:90% draw:6%
Game 406 -> randbot1:4% neuralnet2:90% draw:6%
Game 407 -> randbot1:4% neuralnet2:90% draw:6%
Game 408 -> randbot1:4% neuralnet2:90% draw:6%
Game 409 -> randbot1:4% neuralnet2:90% draw:6%
Game 410 -> randbot1:4% neuralnet2:90% draw:6%
Game 411 -> randbot1:4% neuralnet2:90% draw:6%
Game 412 -> randbot1:4% neuralnet2:90% draw:6%
Game 413 -> randbot1:4% neuralnet2:90% draw:6%
Game 414 -> randbot1:4% neuralnet2:90% draw:6%
Game 415 -> randbot1:4% neuralnet2:90% draw:6%
random bot wins!
  ...  ...  ..X  O.X  O.X  
  ..X  .OX  .OX  .OX  .OX  
  ...  ...  ...  ...  ..X  
Game 416 -> randbot1:4% neuralnet2:90% draw:6%
```