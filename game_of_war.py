from tkinter import *
from tkinter import ttk
from graph import GraphWidget

root = Tk()
root.title("Game of War")

my_border = GraphWidget(root, 15, 15, 10)

root.mainloop()