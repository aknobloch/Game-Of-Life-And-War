from tkinter import *
from tkinter import ttk
from graph import GraphWidget
from graph_color import GraphColor

def select_green(graph_view, blueb, greenb) :

	graph_view.set_color(GraphColor.alive_green)
	greenb.state(["disabled"])
	blueb.state(["!disabled"])
	
	
def select_blue(graph_view, blueb, greenb) :
	
	graph_view.set_color(GraphColor.alive_blue)
	greenb.state(["!disabled"])
	blueb.state(["disabled"])

root = Tk()
root.title("Game of War")

# Initialize window
main_frame = ttk.Frame(root)
main_frame.grid(column = 1, row = 3)

# Add graph view
my_graph = GraphWidget(main_frame, 20, 45, 10)

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

root.mainloop()