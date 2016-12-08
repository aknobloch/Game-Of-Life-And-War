from tkinter import *
from tkinter import ttk
from graph_color import GraphColor

'''
GraphWidget provides the functionality for displaying the board
game's display. It handles user input for seeding, as well as 
keeping track of the chosen cells and current game board.
'''

class GraphWidget :
	
	'''
	Constructor takes in the root widget for this display,
	as well as the total columns, rows and the width each should be.
	'''
	def __init__(self, rootWidget, rows, columns, width) :
		
		self.total_rows = rows
		self.total_columns = columns
		self.cell_width = width
		self.color = GraphColor.alive_green.value
		
		self.root = rootWidget;
		
		self.__initialize_window()
		self.__create_cells()
		
		self.initial_colors = [[0 for y in range(self.total_rows)] for x in range(self.total_columns)]
		
	
	'''
	Paints the square associated with the given column and row 
	to the color that is currently set.
	'''
	def paint_coordinate(self, column, row) :
	
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
	def __paint_coordinate_color(self, column, row, paint_color):
	
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
	def paint_clear(self, column, row) :
		
		# paint it the default background
		self.__paint_coordinate_color(column, row, GraphColor.background.value)
	
	'''
	Paints the column and row the appropriate color
	'''
	def paint_alive_green(self, column, row) :
				
		# paint it the alive green
		self.__paint_coordinate_color(column, row, GraphColor.alive_green.value)
	
	'''
	Paints the column and row the appropriate color
	'''	
	def paint_dead_green(self, column, row) :
	
		# paint it the visited green
		self.__paint_coordinate_color(column, row, GraphColor.visited_green.value)
		
	'''
	Paints the column and row the appropriate color
	'''	
	def paint_visited_blue(self, column, row) :
		
		# paint it the alive blue
		self.__paint_coordinate_color(column, row, GraphColor.alive_blue.value)
		
		
	'''
	Paints the column and row the appropriate color
	'''	
	def paint_visited_blue(self, column, row) :
		
		# paint it the visited blue
		self.__paint_coordinate_color(column, row, GraphColor.visited_blue.value)
	
	'''
	Defines the functionality for when the user clicks the graph.
	Paints the coordinate clicked to the current color attribute.
	'''
	def on_click(self, event) :
	
		# determine the column and row selected
		column_clicked = int(event.x / self.cell_width)
		row_clicked = int(event.y / self.cell_width)
		
		# if the square hasn't been selected, paint color and mark
		if(self.initial_colors[row_clicked][column_clicked] == 0) :
			self.__paint_coordinate_color(column_clicked, row_clicked, self.color)
			self.initial_colors[row_clicked][column_clicked] = 1
			
		# otherwise, paint back to background and unmark
		else :
			self.__paint_coordinate_color(column_clicked, row_clicked, GraphColor.background.value)
			self.initial_colors[row_clicked][column_clicked] = 0
			
		self.__print_graph()
		
	
	'''
	Initializes the window, placing it inside the root specified at construction
	'''
	def __initialize_window(self) :
		
		self.window = Canvas(self.root, 
							width = (self.total_columns * self.cell_width),
							height = (self.total_rows * self.cell_width), 
							borderwidth = 0, 
							highlightthickness=0)
							
		self.window.pack(side = "top", fill = "both", expand = "true")
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
	
		self.color = new_color
	
	'''
	Debugging purposes
	'''
	def __print_graph(self) :
		
		for row in self.initial_colors :
			
			print(row)
	


