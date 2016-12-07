from tkinter import *
from tkinter import ttk
'''
GraphWidget provides the functionality for displaying the board
game's display. It handles user input for seeding, as well as 
keeping track of the chosen cells and current game board.

'''
class GraphWidget :
	

	empty = "#f5f5f0"
	
	visited_green = "#99ff99" 
	alive_green = "#009933" 
	
	visited_blue = "#33ccff" 
	alive_blue = "#0033cc" 
	
	'''
	Constructor takes in the root widget for this display,
	as well as the total columns, rows and the width each should be.
	'''
	def __init__(self, rootWidget, rows, columns, width) :
		
		self.total_rows = rows
		self.total_columns = columns
		self.cell_width = width
		self.color = self.alive_green
		
		self.root = rootWidget;
		
		self.__initialize_window()
		self.__create_cells()
		
	
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
	def paint_coordinate_color(self, column, row, paint_color):
	
		# calculate x and y to paint
		x1 = column * self.cell_width
		y1 = row * self.cell_width
		x2 = x1 + self.cell_width
		y2 = y1 + self.cell_width
				
		# paint it the current color
		self.window.create_rectangle(x1, y1, x2, y2, fill = paint_color)
		
		self.print_graph()
	
	'''
	Paints the column and row the appropriate color
	'''
	def paint_alive_green(self, column, row) :
				
		# paint it the alive green
		self.paint_coordinate_color(column, row, self.alive_green)
	
	'''
	Paints the column and row the appropriate color
	'''	
	def paint_dead_green(self, column, row) :
	
		# paint it the visited green
		self.paint_coordinate_color(column, row, self.visited_green)
		
	'''
	Paints the column and row the appropriate color
	'''	
	def paint_visited_blue(self, column, row) :
		
		# paint it the alive blue
		self.paint_coordinate_color(column, row, self.alive_blue)
		
		
	'''
	Paints the column and row the appropriate color
	'''	
	def paint_visited_blue(self, column, row) :
		
		# paint it the visited blue
		self.paint_coordinate_color(column, row, self.visited_blue)
	
	'''
	Defines the functionality for when the user clicks the graph.
	Paints the coordinate clicked to the current color attribute.
	'''
	def on_click(self, event) :
	
		# determine the column and row selected
		column_clicked = int(event.x / self.cell_width)
		row_clicked = int(event.y / self.cell_width)
		
		self.paint_coordinate_color(column_clicked, row_clicked, self.color)
		
	
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
				
				self.window.create_rectangle(x1, y1, x2, y2, fill = self.empty)
				
	'''
	Sets the color attribute to the specified color
	'''
	def set_color(self, new_color) :
	
		self.color = new_color
	


