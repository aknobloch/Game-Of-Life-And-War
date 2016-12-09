from tkinter import *
from tkinter import ttk
from graph import GraphWidget
from graph_color import GraphColor
from game_logic import GameLogic
import time
	
def start(startb, blueb, greenb, canvas, runner) :
	
	canvas.paint_enabled = False
	blueb.state(["disabled"])
	greenb.state(["disabled"])
	
	# if game is not running
	if(not runner.running) :
		
		runner.running = True;
		startb.config(text = "Stop")
		
	else :
	
		runner.running = False;
		startb.config(text = "Start")
		
def reset(startb, blueb, greenb, canvas, game_runner) :
	
	startb.config(text = "Start")
	blueb.state(["!disabled"])
	greenb.state(["!disabled"])
	game_runner.rollback()
	canvas.paint_enabled = True\
	
def clear(startb, blueb, greenb, canvas, game_runner) :
	
	startb.config(text = "Start")
	blueb.state(["!disabled"])
	greenb.state(["!disabled"])
	game_runner.reset()
	canvas.clear()
	canvas.paint_enabled = True

# Initialize window
root = Tk()
root.title("Game of War")

# Initialize frame
main_frame = ttk.Frame(root)
main_frame.grid(column = 1, row = 3)

#Create game runner
game = GameLogic()

# calculate screen size to determine game board size
screen_width = root.winfo_screenwidth() * 1/2  # game board covers 1/2 of screen
screen_height = root.winfo_screenheight() * 1/2
square_pixel_size = 10

game_board_len = int(screen_width / square_pixel_size)
game_board_height = int(screen_height / square_pixel_size)

my_graph = GraphWidget(main_frame, game, game_board_height, game_board_len, square_pixel_size)

#Initialize game runner with canvas
game.initialize(my_graph)

# Add label group
label_group = ttk.Frame(main_frame, padding = "10 0 10 20")
label_group.grid(column = 1, row = 2)

# Add color selection label
ttk.Label(label_group, text = "Place Civilization: ").grid(column = 1, row = 1)

# Create variable to allow green to be default selected
v = IntVar()
v.set(1) # 1 is green radio button

# Add green color radio button
green_button = ttk.Radiobutton(label_group, text = "Green", variable = v, command = lambda: my_graph.set_color(GraphColor.alive_green), value = 1)
green_button.grid(column = 2, row = 1, padx = 5, pady = 5)

# Add blue color radio button
blue_button = ttk.Radiobutton(label_group, text = "Blue", variable = v, command = lambda: my_graph.set_color(GraphColor.alive_blue), value = 2)
blue_button.grid(column = 3, row = 1, padx = 5, pady = 5)

# Add start button
start_button = ttk.Button(label_group, text = "Start", command = lambda: start(start_button, blue_button, green_button, my_graph, game))
start_button.grid(column = 2, row = 2, columnspan = 2, padx = 5, pady = 5)

# Add reset button
reset_button = ttk.Button(label_group, text = "Reset", command = lambda: reset(start_button, blue_button, green_button, my_graph, game))
reset_button.grid(column = 2, row = 3, columnspan = 2, padx = 5, pady = 5)

# Add clear button
clear_button = ttk.Button(label_group, text = "Clear", command = lambda: clear(start_button, blue_button, green_button, my_graph, game))
clear_button.grid(column = 2, row = 4, columnspan = 2, padx = 5, pady = 5)

while True:
    
	# update game logic
	game.update()
	
	# update canvas
	root.update()