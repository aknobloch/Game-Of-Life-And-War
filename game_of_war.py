from tkinter import *
from tkinter import ttk
from graph import GraphWidget
from graph_color import GraphColor
from game_logic import GameLogic
import time

def select_green(graph_view, blueb, greenb) :

	graph_view.set_color(GraphColor.alive_green)
	greenb.state(["disabled"])
	blueb.state(["!disabled"])
	
	
def select_blue(graph_view, blueb, greenb) :
	
	graph_view.set_color(GraphColor.alive_blue)
	greenb.state(["!disabled"])
	blueb.state(["disabled"])
	
def start(startb, blueb, greenb, canvas, runner) :
	
	canvas.paint_enabled = False
	greenb.state(["disabled"])
	blueb.state(["disabled"])
	
	# if game is not running
	if(not runner.running) :
		
		runner.running = True;
		startb.config(text = "Stop")
		
	else :
	
		runner.running = False;
		startb.config(text = "Start")
		
		
root = Tk()
root.title("Game of War")

# Initialize window
main_frame = ttk.Frame(root)
main_frame.grid(column = 1, row = 3)

#Create game runner
game = GameLogic()

# Add graph view
my_graph = GraphWidget(main_frame, game, 10, 10, 10)

#Initialize game runner with canvas
game.initialize(my_graph)

# Add label group
label_group = ttk.Frame(main_frame, padding = "10 0 10 20")
label_group.grid(column = 1, row = 2)

# Add color selection label
ttk.Label(label_group, text = "Place Civilization: ").grid(column = 1, row = 1)

# Add green color selection button
green_button = ttk.Button(label_group, text = "Green", command = lambda: select_green(my_graph, blue_button, green_button))
green_button.grid(column = 2, row = 1)
green_button.state(["disabled"])

# Add blue color selection button
blue_button = ttk.Button(label_group, text = "Blue", command = lambda: select_blue(my_graph, blue_button, green_button))
blue_button.grid(column = 3, row = 1)

# Add start button
start_button = ttk.Button(label_group, text = "Start", command = lambda: start(start_button, blue_button, green_button, my_graph, game))
start_button.grid(column = 2, row = 2, columnspan = 2)

while True:
    
	# update game logic
	game.update()
	
	# update canvas
	root.update_idletasks()
	root.update()