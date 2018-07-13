# tictactoe-neuralnet
Using a Neural Network to play Tic Tac Toe

The neural network predicts the strength of a board for a player.
The training data looks like this: board (9 values {0;1;-1}) -> score ([-9;9])
The neural network will be used to assess the strength of all the possible moves of a player and select the best one.

After trying many different neural network configuration, it seems the best result is achieved with a single hidden layer of 9 neurons.  
The NN looks like this: 9 input -> 9 hidden -> 1 output.

## Result vs random

When playing first, neuralnet2 doesn't lose:

```Game 100 -> neuralnet2:99% (99) randbot1:0% (0) draw:1% (1)
Game 200 -> neuralnet2:99% (198) randbot1:0% (0) draw:1% (2)
Game 300 -> neuralnet2:99% (297) randbot1:0% (0) draw:1% (3)
Game 400 -> neuralnet2:99% (397) randbot1:0% (0) draw:1% (3)
Game 500 -> neuralnet2:99% (497) randbot1:0% (0) draw:1% (3)
Game 600 -> neuralnet2:99% (596) randbot1:0% (0) draw:1% (4)
Game 700 -> neuralnet2:99% (693) randbot1:0% (0) draw:1% (7)
Game 800 -> neuralnet2:99% (793) randbot1:0% (0) draw:1% (7)
Game 900 -> neuralnet2:99% (891) randbot1:0% (0) draw:1% (9)
Game 1000 -> neuralnet2:98% (986) randbot1:0% (0) draw:2% (14)
```

When playing second, we have a 90% win rate, 8% draw, 2% loss:

```Game 100 -> randbot1:1% (1) neuralnet2:89% (89) draw:10% (10)
Game 200 -> randbot1:2% (4) neuralnet2:90% (181) draw:8% (15)
Game 300 -> randbot1:2% (8) neuralnet2:89% (269) draw:9% (23)
Game 400 -> randbot1:2% (11) neuralnet2:88% (355) draw:10% (34)
Game 500 -> randbot1:2% (13) neuralnet2:89% (447) draw:9% (40)
Game 600 -> randbot1:3% (18) neuralnet2:89% (538) draw:8% (44)
Game 700 -> randbot1:2% (19) neuralnet2:89% (627) draw:9% (54)
Game 800 -> randbot1:2% (20) neuralnet2:89% (717) draw:9% (63)
Game 900 -> randbot1:2% (21) neuralnet2:90% (810) draw:8% (69)
Game 1000 -> randbot1:2% (22) neuralnet2:90% (905) draw:8% (73)
```

## Design

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

It is possible to print the moves in the console:

```Game 800 -> randbot1:1% (13) neuralnet2:92% (740) draw:7% (47)
Game 900 -> randbot1:1% (13) neuralnet2:92% (831) draw:7% (56)
random bot wins!
  ...  O..  O..  O.O  OXO  OXO  OXO  
  .X.  .X.  XX.  XX.  XX.  XX.  XXX  
  ...  ...  ...  ...  ...  .O.  .O.  
random bot wins!
  ...  O..  OX.  OX.  OX.  OX.  OX.  
  .X.  .X.  .X.  .X.  XX.  XX.  XXX  
  ...  ...  ...  .O.  .O.  OO.  OO.  
random bot wins!
  ...  ...  ...  ..O  ..O  ..O  X.O  
  ...  .O.  XO.  XO.  XO.  XO.  XO.  
  .X.  .X.  .X.  .X.  XX.  XXO  XXO  
Game 1000 -> randbot1:1% (16) neuralnet2:91% (918) draw:8% (66)
```
