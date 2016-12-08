import time

class GameLogic :
	
	# tracks whether the game is paused or not
	running = False;
	
	'''
	Creates an empty GameLogic class. The class must also be initialized
	after with a canvas. This is neccessary because the canvas also needs 
	to be initialized with a GameLogic object. This tight coupling hurts 
	my soul.
	'''
	def __init__(self) :
		
		self.initialized = False
		
	'''
	Initializes this GameLogic object with a canvas to send data to.
	'''
	def initialize(self, canvas) :
	
		self.canvas = canvas
		
		rows = canvas.get_rows()
		columns = canvas.get_columns()
		
		self.current_state = [['' for x in range(columns)] for y in range(rows)]
		self.next_state = [['' for x in range(columns)] for y in range(rows)]
		self.green_column_counts = [0 for x in range(columns)]
		self.blue_column_counts = [0 for x in range(columns)]
		
		self.initialized = True
	
	'''
	Places a green marker in the indicated cell, increments counter.
	'''
	def place_green(self, row, column) :
		
		self.current_state[row][column] = 'G'
		# update counts
		self.green_column_counts[column] += 1
		self.__print()
	
	'''
	Places a blue marker in the indicated cell, increments counter.
	'''
	def place_blue(self, row, column) :
		
		self.current_state[row][column] = 'B'
		# update counts
		self.blue_column_counts[column] += 1
		self.__print()
		
	'''
	Removes a marker from the indicated cell, decrements counter.
	'''
	def remove_cell(self, row, column) :
	
		removed = self.current_state[row][column]
		
		self.current_state[row][column] = ''
		# update counts
		if removed == 'G' :
			self.green_column_counts[column] -= 1
		if removed == 'B' :
			self.blue_column_counts[column] -= 1
			
		self.__print()
		
	'''
	Returns whether or not the inidicated cell is occupied
	'''	
	def is_empty(self, row, column) :
	
		if self.current_state[row][column] == '' :
			
			return True
			
		return False

	'''
	Prints the current status of the game board. Mostly for debug.
	'''	
	def __print(self) :
		
		print("\t~~~CURRENT GAME STATE~~~")
		
		print("Green counts:", self.green_column_counts)
		print("Blue counts:", self.blue_column_counts)
		print("\n")
		
		for row in self.current_state :
			
			print(row)
			
		print("\n\n")
		
	'''
	Main logic of the class. Loops through all of the cells and determines next state
	'''	
	def update(self) :
	
		if not self.initialized :
			print("GameLogic was never initialized!")
			return
	
		if not self.running :
			return
			
		# Game Logic
		