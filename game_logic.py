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
		
		self.rows = canvas.get_rows()
		self.columns = canvas.get_columns()
		
		self.current_state = [[' ' for x in range(self.columns)] for y in range(self.rows)]
		self.next_state = [[' ' for x in range(self.columns)] for y in range(self.rows)]
		self.green_column_counts = [0 for x in range(self.columns)]
		self.blue_column_counts = [0 for x in range(self.columns)]
		
		self.initialized = True
	
	'''
	Places a green marker in the indicated cell, increments counter.
	'''
	def place_green(self, row, column) :
		
		self.current_state[row][column] = 'G'
		# update counts
		self.green_column_counts[column] += 1
		
	
	'''
	Places a blue marker in the indicated cell, increments counter.
	'''
	def place_blue(self, row, column) :
		
		self.current_state[row][column] = 'B'
		# update counts
		self.blue_column_counts[column] += 1
		
		
	'''
	Removes a marker from the indicated cell, decrements counter.
	'''
	def remove_cell(self, row, column) :
	
		removed = self.current_state[row][column]
		
		self.current_state[row][column] = ' '
		# update counts
		if removed == 'G' :
			self.green_column_counts[column] -= 1
		if removed == 'B' :
			self.blue_column_counts[column] -= 1
			
		
		
	'''
	Returns whether or not the inidicated cell is occupied
	'''	
	def is_empty(self, row, column) :
	
		if self.current_state[row][column] == ' ' :
			
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
		
		print("\t~~~NEXT GAME STATE~~~")
		
		for row in self.next_state :
			
			print(row)
			
		print("\n\n")
		
	
	'''
	Finds the number of surrounding cells with the given search char
	'''
	def search_surroundings(self, row, column, search_char) :
	
		neighbors = 0
	
		# helps determine what to check while preventing index out of bounds
		check_left = True
		check_right = True
		check_top = True
		check_bottom = True
		
		if column == 1 :
			check_left = False
		
		if column == self.columns - 1:
			check_right = False
			
		if row == 1 :
			check_top = False
			
		if row == self.rows - 1:
			check_bottom = False
			
		
		if check_left :
			if self.current_state[row][column - 1] == search_char:
				neighbors += 1
				
		if check_right :
			if self.current_state[row][column + 1] == search_char :
				neighbors += 1
				
		if check_top :
			if self.current_state[row - 1][column] == search_char :
				neighbors += 1
		
		if check_bottom :
			if self.current_state[row + 1][column] == search_char :
				neighbors += 1
				
		# check top left diagonal
		if check_left and check_top :
			if self.current_state[row - 1][column - 1] == search_char :
				neighbors += 1
				
		# check bottom left diagonal
		if check_left and check_bottom :
			if self.current_state[row + 1][column - 1] == search_char :
				neighbors += 1
				
		# check top right diagonal
		if check_right and check_top :
			if self.current_state[row - 1][column + 1] == search_char :
				neighbors += 1
				
		# check bottom right diagonal
		if check_right and check_bottom :
			if self.current_state[row + 1][column + 1] == search_char :
				neighbors += 1
				
		return neighbors
	
	
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
		# start at one because zero indexes are never populated
		for row in range(1, self.rows) :
		
			for column in range(1, self.columns) :
				
				empty_cell = self.is_empty(row, column)
				surrounding_green = self.search_surroundings(row, column, 'G')
				surrounding_blue = self.search_surroundings(row, column, 'B')
				
				# if an empty cell, check for possible births
				if empty_cell :
				
					if surrounding_blue == 3 and surrounding_green == 3 :
						# do nothing
						continue
					
					if surrounding_blue == 3 :
						self.next_state[row][column] = 'B'
						
					elif surrounding_green == 3 :
						self.next_state[row][column] = 'G'
				
				# otherwise check blue stuff
				elif self.current_state[row][column] == 'B' :
					
					#check population dead conditions
					if surrounding_blue < 2 or surrounding_blue > 3 :
						self.next_state[row][column] = ' '
					
					# check battle dead conditions
					elif surrounding_green > 1 and surrounding_green > surrounding_blue :
						self.next_state[row][column] = ' '
					
					else :
						self.next_state[row][column] = 'B'
					
				
				# otherwise check green stuff
				else :
					
					#check population dead conditions
					if surrounding_green < 2 or surrounding_green > 3 :
						self.next_state[row][column] = ' '
					
					# check battle dead conditions
					elif surrounding_blue > 1 and surrounding_blue > surrounding_green :
						self.next_state[row][column] = ' '
					
					else :
						self.next_state[row][column] = 'G'
					
				
		
		self.update_game()
		
		
	'''
	Updates the game, by sending appropriate commands to the canvas to paint,
	determining new counts for green and blue columns and then setting the
	states for the next round.
	'''
	def update_game(self) :
		
		
		for row in range(1, self.rows) :
		
			for column in range(1, self.columns) :
				
				previous_cell = self.current_state[row][column]
				current_cell = self.next_state[row][column]
				
				# check visited blue
				if previous_cell == 'B' and current_cell == ' ' :
					self.canvas.paint_visited_blue(row, column)
					self.blue_column_counts[column] -= 1
					
				# check visited green
				elif previous_cell == 'G' and current_cell == ' ' :
					self.canvas.paint_visited_green(row, column)
					self.green_column_counts[column] -= 1
					
				# check current green
				elif current_cell == 'G' :
					self.canvas.paint_alive_green(row, column)
					self.green_column_counts[column] += 1
					
				# check current blue
				elif current_cell == 'B' :
					self.canvas.paint_alive_blue(row, column)
					self.blue_column_counts[column] += 1
					
		# after, swap current state with next state
		self.current_state = self.next_state
		self.next_state = [[' ' for x in range(self.columns)] for y in range(self.rows)]
		
	'''
	Resets the game back to a new game.
	'''
	def reset(self) :
		
		self.current_state = [[' ' for x in range(self.columns)] for y in range(self.rows)]
		self.next_state = [[' ' for x in range(self.columns)] for y in range(self.rows)]
		
				
		