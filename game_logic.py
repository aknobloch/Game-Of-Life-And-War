import time

class GameLogic :
	
	running = False;
	
	def __init__(self) :
		
		self.initialized = False
		
	def initialize(self, canvas) :
	
		self.canvas = canvas
		
		rows = canvas.get_rows()
		columns = canvas.get_columns()
		
		self.game_board = [['' for x in range(columns)] for y in range(rows)]
		self.green_column_counts = [0 for x in range(columns)]
		self.blue_column_counts = [0 for x in range(columns)]
		
		self.initialized = True
		
	def place_green(self, row, column) :
		
		self.game_board[row][column] = 'G'
		# update counts
		self.green_column_counts[column] += 1
		self.__print()
	
	def place_blue(self, row, column) :
		
		self.game_board[row][column] = 'B'
		# update counts
		self.blue_column_counts[column] += 1
		self.__print()
		
	def remove_green(self, row, column) :
	
		self.game_board[row][column] = ''
		# update counts
		self.green_column_counts[column] -= 1
		self.__print()
		
	def remove_blue(self, row, column) :
	
		self.game_board[row][column] = ''
		# update counts
		self.blue_column_counts[column] -= 1
		self.__print()
		
	def is_empty(self, row, column) :
	
		if self.game_board[row][column] == '' :
			
			return True
			
		return False

	def __print(self) :
		
		print("\t~~~CURRENT GAME STATE~~~")
		
		print("Green counts:", self.green_column_counts)
		print("Blue counts:", self.blue_column_counts)
		print("\n")
		
		for row in self.game_board :
			
			print(row)
		print("\n\n")
		
	def update(self) :
	
		if not self.initialized :
			print("GameLogic was never initialized!")
			return
	
		if not self.running :
			return
			
		# Game Logic
		