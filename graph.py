from tkinter import *
from tkinter import ttk
from graph_color import GraphColor

'''
GraphWidget provides the functionality for displaying the board
game's display. It handles user input for seeding, as well as 
keeping track of the chosen cells and current game board.
'''

class GraphWidget :
	
	paint_enabled = True
	
	'''
	Constructor takes in the root widget for this display,
	as well as the total columns, rows and the width each should be.
	'''
	def __init__(self, root_widget, logic_controller, rows, columns, width) :
		
		self.total_rows = rows
		self.total_columns = columns
		self.cell_width = width
		self.color = GraphColor.alive_green.value
		
		self.root = root_widget
		self.game_logic = logic_controller
		
		self.__initialize_window()
		self.__create_cells()
		
	
	'''
	Paints the square associated with the given column and row 
	to the color that is currently set.
	'''
	def paint_coordinate(self, row, column) :
	
		# calculate x and y to paint
		x1 = column * self.cell_width
		y1 = row * self.cell_width
		x2 = x1 + self.cell_width
		y2 = y1 + self.cell_width
				
		# paint it the current color
		self.window.create_rectangle(x1, y1, x2, y2, fill = self.color)
	
	'''
	Paints the indicated column and row the given color.
	'''
	def __paint_coordinate_color(self, row, column, paint_color):
	
		# calculate x and y to paint
		x1 = column * self.cell_width
		y1 = row * self.cell_width
		x2 = x1 + self.cell_width
		y2 = y1 + self.cell_width
				
		# paint it the current color
		self.window.create_rectangle(x1, y1, x2, y2, fill = paint_color)
		
		
	'''
	Paints the column and row the appropriate color
	'''	
	def paint_clear(self, row, column) :
		
		# paint it the default background
		self.__paint_coordinate_color(row, column, GraphColor.background.value)
	
	'''
	Paints the column and row the appropriate color
	'''
	def paint_alive_green(self, row, column) :
				
		# paint it the alive green
		self.__paint_coordinate_color(row, column, GraphColor.alive_green.value)
	
	'''
	Paints the column and row the appropriate color
	'''	
	def paint_visited_green(self, row, column) :
	
		# paint it the visited green
		self.__paint_coordinate_color(row, column, GraphColor.visited_green.value)
		
	'''
	Paints the column and row the appropriate color
	'''	
	def paint_alive_blue(self, row, column) :
		
		# paint it the alive blue
		self.__paint_coordinate_color(row, column, GraphColor.alive_blue.value)
		
		
	'''
	Paints the column and row the appropriate color
	'''	
	def paint_visited_blue(self, row, column) :
		
		# paint it the visited blue
		self.__paint_coordinate_color(row, column, GraphColor.visited_blue.value)
	
	'''
	Defines the functionality for when the user clicks the graph.
	Paints the coordinate clicked to the current color attribute.
	If the selected square is already painted, reverts back to background.
	'''
	def on_click(self, event) :
	
		if not self.paint_enabled :
			return
	
		# determine the column and row selected
		column_clicked = int(event.x / self.cell_width)
		row_clicked = int(event.y / self.cell_width)
		
		# check for index out of bounds
		if(column_clicked > self.total_columns - 1 or row_clicked > self.total_rows - 1) :
			return
			
		# check for zero index
		if(column_clicked == 0) or (row_clicked == 0) :
			return
		
		# if the square hasn't been selected, paint color and mark
		if(self.game_logic.is_empty(row_clicked, column_clicked)) :
			self.__paint_coordinate_color(row_clicked, column_clicked, self.color)
			
			if(self.color == GraphColor.alive_green.value) :
				
				self.game_logic.place_green(row_clicked, column_clicked)
			
			else :
				
				self.game_logic.place_blue(row_clicked, column_clicked)
			
		# otherwise, paint back to background and unmark
		else :
		
			self.__paint_coordinate_color(row_clicked, column_clicked, GraphColor.background.value)
			self.game_logic.remove_cell(row_clicked, column_clicked)
			
			
		
	
	'''
	Initializes the window, placing it inside the root specified at construction
	'''
	def __initialize_window(self) :
		
		self.window = Canvas(self.root, 
							width = (self.total_columns * self.cell_width),
							height = (self.total_rows * self.cell_width), 
							borderwidth = 10, 
							highlightthickness=0)
							
		self.window.grid(column = 1, row = 1)
		self.window.bind("<Button-1>", self.on_click)
	
	'''
	Creates an empty grid
	'''
	def __create_cells(self) :
	
		for row in range(self.total_rows) :

			for column in range(self.total_columns) :
			
				x1 = column * self.cell_width
				y1 = row * self.cell_width
				x2 = x1 + self.cell_width
				y2 = y1 + self.cell_width
				
				self.window.create_rectangle(x1, y1, x2, y2, fill = GraphColor.background.value)
				
	'''
	Sets the color attribute to the specified color
	'''
	def set_color(self, new_color) :
	
		if(new_color == GraphColor.alive_blue or new_color == GraphColor.alive_green) :
			
			self.color = new_color.value
			
		else :
			
			print("Must pass in a valid GraphColor color")
			
	def get_rows(self) :
		return self.total_rows
		
	def get_columns(self) :
		return self.total_columns
	
	


