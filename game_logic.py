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
	Checks the surrounding cells for a new green birth potential
	'''
	def check_green_birth(self, row, column) :
	
		green_neighbors = 0
	
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
			
		# if left and right are potentially populated, but their sum
		# is not at least one, it is impossible for a cell to be born 
		if(check_left and check_right) :
			if self.green_column_counts[column - 1] == 0 and self.green_column_counts[column + 1] == 0 :
				return False
				
		# same logic as above, just applied for different situations
		if check_left and not check_right :
			if self.green_column_counts[column - 1] == 0 :
				return False
				
		# same logic as above....
		if check_right and not check_left :
			if self.green_column_counts[column + 1] == 0 :
				return False
				
		# if made it this far, manually check
		if check_left :
			if self.current_state[row][column - 1] == 'G' :
				green_neighbors += 1
				
		if check_right :
			if self.current_state[row][column + 1] == 'G' :
				green_neighbors += 1
				
		if check_top :
			if self.current_state[row - 1][column] == 'G' :
				green_neighbors += 1
		
		if check_bottom :
			if self.current_state[row + 1][column] == 'G' :
				green_neighbors += 1
				
		# check top left diagonal
		if check_left and check_top :
			if self.current_state[row - 1][column - 1] == 'G' :
				green_neighbors += 1
				
		# check bottom left diagonal
		if check_left and check_bottom :
			if self.current_state[row + 1][column - 1] == 'G' :
				green_neighbors += 1
				
		# check top right diagonal
		if check_right and check_top :
			if self.current_state[row - 1][column + 1] == 'G' :
				green_neighbors += 1
				
		# check bottom right diagonal
		if check_right and check_bottom :
			if self.current_state[row + 1][column + 1] == 'G' :
				green_neighbors += 1
				
		# final logic for birth
		if green_neighbors == 3 :
			return True
		else : 
			return False
		
	'''
	Checks the surrounding cells for a new blue birth potential
	'''
	def check_blue_birth(self, row, column) :
	
		blue_neighbors = 0
	
		# helps determine what to check while preventing index out of bounds
		check_left = True
		check_right = True
		check_top = True
		check_bottom = True
		
		if column == 1 :
			check_left = False
		
		if column == self.columns - 1 :
			check_right = False
			
		if row == 1 :
			check_top = False
			
		if row == self.rows - 1 :
			check_bottom = False
			
		# if left and right are potentially populated, but their sum
		# is not at least one, it is impossible for a cell to be born 
		if(check_left and check_right) :
			if self.blue_column_counts[column - 1] == 0 and self.blue_column_counts[column + 1] == 0 :
				return False
				
		# same logic as above, just applied for different situations
		if check_left and not check_right :
			if self.blue_column_counts[column - 1] == 0 :
				return False
				
		# same logic as above....
		if check_right and not check_left :
			if self.blue_column_counts[column + 1] == 0 :
				return False
				
		# if made it this far, manually check
		if check_left :
			if self.current_state[row][column - 1] == 'B' :
				blue_neighbors += 1
				
		if check_right :
			if self.current_state[row][column + 1] == 'B' :
				blue_neighbors += 1
				
		if check_top :
			if self.current_state[row - 1][column] == 'B' :
				blue_neighbors += 1
		
		if check_bottom :
			if self.current_state[row + 1][column] == 'B' :
				blue_neighbors += 1
				
		# check top left diagonal
		if check_left and check_top :
			if self.current_state[row - 1][column - 1] == 'B' :
				blue_neighbors += 1
				
		# check bottom left diagonal
		if check_left and check_bottom :
			if self.current_state[row + 1][column - 1] == 'B' :
				blue_neighbors += 1
				
		# check top right diagonal
		if check_right and check_top :
			if self.current_state[row - 1][column + 1] == 'B' :
				blue_neighbors += 1
				
		# check bottom right diagonal
		if check_right and check_bottom : 
			if self.current_state[row + 1][column + 1] == 'B' :
				blue_neighbors += 1
				
		# final logic for birth
		if blue_neighbors == 3 :
			return True
		else : 
			return False
					
	
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
		#time.sleep(2)
		# start at one because zero indexes are never populated
		for row in range(1, self.rows) :
		
			for column in range(1, self.columns) :
				
				empty_cell = self.is_empty(row, column)
				
				# if an empty cell, check for possible births
				if empty_cell :
				
					green_birth = self.check_green_birth(row, column)
					blue_birth = self.check_blue_birth(row, column)
					
					if green_birth and blue_birth :
						
						self.next_state[row][column] = ' '
						
					elif green_birth :
						
						self.next_state[row][column] = 'G'
						
					elif blue_birth :
						
						self.next_state[row][column] = 'B'
				
				# otherwise check blue stuff
				elif self.current_state[row][column] == 'B' :
				
					surrounding_green = self.search_surroundings(row, column, 'G')
					surrounding_blue = self.search_surroundings(row, column, 'B')
					
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
					
					surrounding_green = self.search_surroundings(row, column, 'G')
					surrounding_blue = self.search_surroundings(row, column, 'B')
					
					#check population dead conditions
					if surrounding_green < 2 or surrounding_green > 3 :
						self.next_state[row][column] = ' '
					
					# check battle dead conditions
					elif surrounding_blue > 1 and surrounding_blue > surrounding_green :
						self.next_state[row][column] = ' '
					
					else :
						self.next_state[row][column] = 'G'
					
				
		
		self.update_canvas()
		
		
	def update_canvas(self) :
		
		
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
		
				
		