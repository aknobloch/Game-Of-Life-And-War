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
		
		self.initialized = True
		
	def place_green(self, row, column) :
		
		self.game_board[row][column] = 'G'
		self.__print()
	
	def place_blue(self, row, column) :
		
		self.game_board[row][column] = 'B'
		self.__print()
		
	def place_empty(self, row, column) :
	
		self.game_board[row][column] = ''
		self.__print()
		
	def is_empty(self, row, column) :
	
		if self.game_board[row][column] == '' :
			
			return True
			
		return False

	def __print(self) :
		
		print("\t~~~CURRENT GAME STATE~~~")
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