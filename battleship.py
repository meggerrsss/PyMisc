from random import randint

board = []
boardsize = 5
nships = 3

for x in range(boardsize): # creating a blank grid
  board.append(["O"] * boardsize)

def print_board(board): # printing the board nicely
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board): # randomization for ship placement
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

shipmatrix = [[""]*2]*nships # ship locations

for i in range(0,nships): #somehow not getting different ships
	shipmatrix[i][0] = random_row(board)
	shipmatrix[i][1] = random_col(board)
  
print shipmatrix


for turn in range(boardsize-1):
  print "\n", "Turn",turn+1

  # Everything from here on should go in your for loop!
  # Be sure to indent four spaces!
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if [guess_row,guess_col] in shipmatrix: 
    print "Congratulations! You sunk a battleship! \n"
    cont = str(raw_input("Continue?: "))
    if cont.lower in ["no","n","f","false"]:
    	break
  else: # missed guess
    if (guess_row < 0 or guess_row > boardsize-1) or (guess_col < 0 or guess_col > boardsize-1):
      print "Oops, that's not even in the ocean."
    elif(board[guess_row][guess_col] == "X"):
      print "You guessed that one already."
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    if turn == boardsize-2:
      print "Game Over"
    # Print (turn + 1) here!
    print_board(board)

# From CodeCademy's Python -- Battleship lesson
# https://www.codecademy.com/courses/learn-python/lessons/battleship/

