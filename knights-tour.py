# vim: foldmethod=marker :

import math
import sys

# Assignment:
#
# Given a square chessboard of arbitrary side length and a knight that starts on an arbitrary
# square, output a path allowing the knight to traverse the entire board. The knight moves according
# to the traditional rules of chess.

# function "moves" {{{
def moves (board, pos, n):

  # Compute possible moves. Moves are: (row +- 1, col +- 2) and (row +- 2, col +- 1)
  row = pos[0]
  col = pos[1]
  allmoves = [(row + 1, col + 2), (row + 1, col - 2),
              (row - 1, col + 2), (row - 1, col - 2),
              (row + 2, col + 1), (row + 2, col - 1),
              (row - 2, col + 1), (row - 2, col - 1)]

  # Check each move for validity (does it fall within the chessboard?) and availability (has it
  # been visited?). If the move is both valid and available, append it to /realmoves/.
  realmoves = [] 
  for (row, col) in allmoves: 
    if ((-1 < row < n) and (-1 < col < n) and
        (board[row][col] == 0)):
      realmoves.append ((row, col))    

  return realmoves
#}}}

# function "printboard" {{{
def printboard (board, n):

  # The number of digits in n^2
  width = 1 + int (math.log (n * n, 10))

  for i in range (n):
    for j in range (n):
      print ("%" + str (width) + "d") % (board[i][j]),
    print
#}}}

# function "tour" {{{
def tour (board, pos, n, ct):
  if (ct == (n**2)): 
    # The knight has visited every square. Report success.
    board[pos[0]][pos[1]] = ct 
    return True

  else:
    # Mark the current square
    board[pos[0]][pos[1]] = ct

    # Follow each option
    move_opts = moves (board, pos, n)
    for move in move_opts:
      if (tour (board, move, n, ct + 1)):
        return True

    # Our position must have failed. Prepare to backtrack by clearing the square; return false.
    board[pos[0]][pos[1]] = 0 
    return False
#}}}

# function "main" {{{
def main():
  # Grab board size and position from the command line arguments
  # Notice that most normal people don't number from 0, so we subtract 1 from row and column. :)
  n = int (sys.argv[1])
  pos = (int (sys.argv[2]) - 1, int (sys.argv[3]) - 1)

  # Build our chess board
  board = []
  for i in range(n):
    list = []
    for j in range(n):
      list.append(0)
    board.append(list)

  # Conduct our tour
  if (tour(board, pos, n, 1)):
    printboard(board, n)

  else:
    print "There is unfortunately no successful knight's tour from this position."
#}}}
  
main()
