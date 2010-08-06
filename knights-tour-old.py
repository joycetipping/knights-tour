# % vim: set syntax=pytex :
# 
# \documentclass{article}
# 
# \usepackage{spencer}
# \literatecode
# 
# \begin{document}
# 	\title{Knight's Tour}
# 	\author{Joyce Tipping}
# 	\maketitle
# 
# Assignment:
# Given a square chessboard of arbitrary side length and a
# knight that starts on an arbitrary square, output a path
# allowing the knight to traverse the entire board. The
# knight moves according to the traditional rules of chess.
# 
# ~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
# 
# \begin{python}

def moves(board, pos, n):

	# Computes all valid and available knight moves from a
	# given position on the chessboard.
	#
	# The Parameters:
	#
	# /board/: Chess board. Keep in mind that it's mutable.
	#
	# /pos/: Current position of the knight. Tuple: (row, col)
	#
	# /n/: The length of a side of the board.
	#

	#~*~*~*~#

	# Grab the row and column from /pos/. Compute all
	# theoretically possible moves.
	# Moves are: (row +- 1, col +- 2) and (row +- 2, col +- 1)
	#
	row = pos[0]
	col = pos[1]
	allmoves = [(row + 1, col + 2), (row + 1, col - 2),
			(row - 1, col + 2), (row - 1, col - 2),
			(row + 2, col + 1), (row + 2, col - 1),
			(row - 2, col + 1), (row - 2, col - 1)]

	# Check each move for the following:
	# 1. Validity: Does it fall within the chessboard?
	# 2. Availability: Is it marked (meaning already visited)?
	#
	# If the move is both valid and available, append it to
	# /realmoves/.
	#
	realmoves = [] 
	
	for (row, col) in allmoves: 
		if ((-1 < row < n) and (-1 < col < n) and
				(board[row][col] == 0)):
			realmoves.append((row, col))		
	
	return realmoves



def printboard(board, n):

	# Prints the board.
	#
	# Printing the board is a simple matter. The only concern
	# is that all the numbers be lined up neatly. 

	# /width/: The width of each number being printed out.
	# The number of digits in n^2 plus 2 extra spaces.
	#
	width = 2 + int(n**2 / 10)

	# Print out each number on the board with correct width.
	#
	for i in range(n):
		for j in range(n):
			print ("%"+str(width)+".0d") % (board[i][j]),
		print



def tour(board, pos, n, ct):

	# Conducts the knight's tour through recursion.
	#
	# The Parameters:
	# 
	# /board/, /pos/, and /n/ are the same as in "moves".
	#
	# /ct/:
	# Keeps count of how many squares our knight has
	# successfully visited. Recall that our board has n^2
	# squares.
	# 

	#~*~*~*~#

	# Base Case:
	#
	# Catches /ct/ on (n**2), the last square.
	# Hooray! We will mark this square and report success.
	#
	if (ct == (n**2)): 
		board[pos[0]][pos[1]] = ct 
		return True


	# Reverse Inductive Step:
	# 
	# Our base case didn't catch us, so clearly, we're not
	# done! Oh well: Hard work is the key. :)
	#
	else:

		# Mark current square
		#
		board[pos[0]][pos[1]] = ct

		# Compute move options.
		#
		move_opts = moves(board, pos, n)

		# We have 2 cases at this point:
		# 
		# Case 1.
		# We have no move options. This square is a dead
		# end. If so, we have an immediate failure. The
		# following loop does not execute, and we move on.
		#
		# Case 2.
		# We have move options. Again, we have two cases:
		#
		#	(a) At least one option leads to success. In that
		#			case, we will hit our base case, and the true will
		#			propagate up the stack.
		#
		#	(b) All options lead to failure. Every path branching
		#			from this position leads to a dead end somewhere down
		#			the line.


		# If we have move options, the following loop executes.
		# For each move option, repeat the recursive function: 
		# Mark square; check whether there are any move options;
		# if so, for each of those, repeat this process; etc.
		# 
		# If at any point we hit success, we return true, and
		# we're done. If not, we continue until we've exhausted
		# all options. In that case, we must have failure.
		#
		for move in move_opts:
			if (tour(board, move, n, ct+1)):
				return True

		# If we have reached this part of the program, then this
		# position has failed. Prepare to backtrack by clearing
		# the square. Then, return false.
		#
		board[pos[0]][pos[1]] = 0 
		return False



# "main":
# 
def main():
	print
	print "~*~*~*~*~*~*~*~*~*~*~*~*~*~*~"
	print "Welcome to the Knight's Tour."
	print
	
	# Prompt user for size of board:
	n = input("How many squares long is your board: ")

	# Prompt user for the starting position of the knight as a
	# tuple: (row, column). Since most normal people don't
	# number off from 0, we'll save them that confusion by
	# subtracting 1 from the row and column of their position.
	#
	pos = input("Please enter the starting position of your" +\
			" knight in the format (row, column): ")
	print

	pos = (pos[0] - 1, pos[1] - 1)

	# Now the fun begins!
	# First, we build our chess board ...
	#
	board = []

	for i in range(n):
		list = []
		for j in range(n):
			list.append(0)
		board.append(list)

	# ... and the tour commences!
	# 
	# Initial parameters:
	# /board/ = /board/
	# /pos/ = /pos/
	# /n/ = /n/
	# /ct/ = 1
	# 
	# If there exists a successful route, our function will
	# return true, and we will print out our numbered board.
	#
	# If there is no successful route, our function will
	# return false, and we will convey our regrets to our
	# gentle user.
	#
	if (tour(board, pos, n, 1)):
		printboard(board, n)
		print
		print "Thank you! Have a nice day."
		print "~*~*~*~*~*~*~*~*~*~*~*~*~*~*~"
		print

	else:
		print "We regret to inform you that there is no",
		print "successful knight's tour from this position."
		print "~*~*~*~*~*~*~*~*~*~*~*~*~*~*~"
		print
	
main()
# \end{python}
# \end{document}
