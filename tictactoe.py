### Compulsory Task 3: Tic Tac Toe with Python OOP ###


# ====================================
# Step 1: Import any required packages
# ====================================

# import os library
# will allow program to clear screen and print updated board
import os

# reference this site to found out how to clear screen for new game
# https://www.geeksforgeeks.org/clear-screen-python/

# ========================================================
# Step 2: Creating Necessary Fuctions to help run the Game
# ========================================================

def welcome():
	print("Welcome to my Tic Tac Toe Game\n")

def welcome_screen():
	# clears screen for new board
	# elimanites a full and cluttered terminal
	os.system('cls')
	welcome()
	board.display_board()

def player_turn(player,board):
	'''
	Get user choice
	Determine if user entered a valid choice ie. not already used
	Update Board 
	Display updated board
	'''
	
	player.get_choice()
	player.check_move(board)
	while player.check_move(board) == False:
		print("Please enter a valid number")
		player.get_choice()
		player.check_move(board)
	board.update_board(player)
	board.display_board()

# ===========================================
# Step 3: Creating the Piece, X and O Classes
# ===========================================

class Piece(object):

	'''
	The piece class will take in a player number - 1 to 9
	The class will assign each player a number and check for valid moves

	'''
	def __init__(self,player_name,player_choice = None):
		'''
		Constructs the piece class
		Assigns a player a number and player choice which is defaulted to None
		'''
		self.player_name = player_name
		self.player_choice = player_choice
		

	def get_choice(self):
		'''
		Gets a user choice from 1 to 9
		'''

		choice = int(input(f"Player {self.player_name}: Enter a number from 1 to 9 "))
		self.player_choice = choice

	def check_move(self,board):
		'''
		Checks to see if the players moves was valid
		'''

		board_num = self.player_choice
		if board.board[board_num] == " ":
			return True
		else:
			return False

class X(Piece):

	def __init__(self,player_name,player_choice = None, x_or_o = "X"):

		Piece.__init__(self,player_name,player_choice)
		self.x_or_o = x_or_o
		

	def __str__(self):
		return "X"

	def player_x(self):
		print(f"{self.player_name} you are X, you will go first")

class O(Piece):

	def __init__(self,player_name,player_choice = None ,x_or_o = "O"):

		Piece.__init__(self,player_name,player_choice)

		self.x_or_o = x_or_o
    
	def __str__(self):
		return "O"

	def player_o(self):
		print(f"{self.player_name} you are O, you will go second")



# ===================================
# Step 4: Create TicTacToeBoard Class
# ===================================


class TicTacToeBoard(object):
    
    '''
    This class represents the tic_tac_toe board.
    It will display the board, check for wins and control the game
    Resetting the board is necesary for further games
    '''

    def __init__(self):
    	'''
    	Constructor for the TicTacBoard Class
    	Constructs a list to store player moves for X and O
    	'''
    	self.board = [" "," "," "," "," "," "," "," "," "," "]
    	# board with 10 places
    	# nine for top 3, middle 3 and bottom 3 squares
    	# first cell at index zero will be skipped
    	# allows for mathcing user numbers to board without having to +1

    def display_board(self):
    	'''
    	This method displays the board on the screen for the players
    	'''
    	print(
    f'''
    {self.board[1]} | {self.board[2]} | {self.board[3]}
    ________________

    {self.board[4]} | {self.board[5]} | {self.board[6]}
    ________________
    
    {self.board[7]} | {self.board[8]} | {self.board[9]}
    '''
    )

    def update_board(self,piece_type):

    	num = piece_type.player_choice

    	if piece_type.x_or_o == "X":

    		self.board[num] = "X"

    	else:
    		self.board[num] = "O"

    def board_reset(self):

    	'''
    	Reset board for additional games
    	'''

    	self.board = [" "," "," "," "," "," "," "," "," "," "]
    		


    def check_win(self):
    	'''
    	Check if the game has a winner
    	Checks all possible win combinations
    	'''


    	# check top win
    	if (self.board[1] == self.board[2] == self.board[3]) and self.board[1] != " ":
    		return True
    	# check middle win
    	elif (self.board[4] == self.board[5] == self.board[6]) and self.board[4] != " ":
    		return True
    	# check bottom win
    	elif (self.board[7] == self.board[8] == self.board[9]) and self.board[7] != " ":
    		return True
    	# check first column win 
    	elif (self.board[1] == self.board[4] == self.board[7]) and self.board[1] != " ":
    		return True
    	# check second column win
    	elif (self.board[2] == self.board[5] == self.board[8]) and self.board[2] != " ":
    		return True
    	# check third column win
    	elif (self.board[3] == self.board[6] == self.board[9]) and self.board[3] != " ":
    		return True
    	# check for diagonal win
    	elif (self.board[1] == self.board[5] == self.board[9]) and self.board[1] != " ":
    		return True
    	else:
    		return False


    


# ===============================
# Step 5: Create the Game
# ===============================


board = TicTacToeBoard() # create a board


# clear screen and print welcome


welcome_screen()

x_name = input("Please enter the name of the first player ").strip().title()
o_name = input("Please enter the name of the second player ").strip().title()
x = X(x_name) # create player 1
o = O(o_name) # create player 2

print("\n")
x.player_x()
o.player_o()
print("\n")

print("The board layout is a follows - entering the matching number will enter your choice in the below positions on the board\n")
print(
    f'''
    "1" | "2" | "3"
    ________________

    "4" | "5" | "6"
    ________________
    
    "7" | "8" | "9"
    '''
    )


print("Lets Play!")

def game():
	turns = 0
	while True:
		# let X play turn
		player_turn(x,board)
		# add 1 to played turns
		turns += 1 

		# check for a winner after X's turn
		board.check_win()
		if board.check_win() == True:
			winner = "X"
			break
		
		# check if board is full
		# ie stale mate
		# checked by number of turns
		# if 9 turns played and no winner - stalemate

		if turns == 9:
			print("Stalemate!")
			winner = "Stalemate"
			break

		# let O play their turn		
		player_turn(o,board)
		turns += 1

		# check for a winner after O's turn
		board.check_win()

		if board.check_win() == True:
			winner = "O"
			break

		if turns == 9:
			print("Stalemate!")
			winner = "Stalemate"
			break

		else:
			continue
    
	return winner

winner = game()

if winner == "Stalemate":
	print("No winner this time")
else:	
	print("We have a winner!")
	print(f"{winner} wins!\n")



print("Would you like to play again? ")
user_continue = input("Enter Y to continue. Press Enter to Exit ").strip().lower()

while user_continue == 'y':
	board.board_reset()
	os.system('cls')
	welcome_screen()
	print("\n")
	x.player_x()
	o.player_o()
	print("\n")
	winner = game()

	if winner == "Stalemate":
		print("No winner this time")
	else:
		print("We have a winner!")
		print(f"{winner} wins!\n")
	
	user_continue = input("Enter Y to continue. Press Enter to Exit").strip().lower()

print("Thanks for playing!\n")


print("Exiting the game\n")








