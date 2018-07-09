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

## Sample output
```Game 990 -> randbot1:2% neuralnet2:90% draw:8%
Game 991 -> randbot1:2% neuralnet2:90% draw:8%
Game 992 -> randbot1:2% neuralnet2:90% draw:8%
random bot wins!
  ...  O..  OX.  OX.  OX.  OX.  OX.  
  .X.  .X.  .X.  .X.  XX.  XX.  XXX  
  ...  ...  ...  .O.  .O.  OO.  OO.  
Game 993 -> randbot1:2% neuralnet2:90% draw:8%
Game 994 -> randbot1:2% neuralnet2:90% draw:8%
Game 995 -> randbot1:2% neuralnet2:90% draw:8%
Game 996 -> randbot1:2% neuralnet2:90% draw:8%
Game 997 -> randbot1:2% neuralnet2:90% draw:8%
Game 998 -> randbot1:2% neuralnet2:90% draw:8%
Game 999 -> randbot1:2% neuralnet2:90% draw:8%
Game 1000 -> randbot1:2% neuralnet2:90% draw:8%
```