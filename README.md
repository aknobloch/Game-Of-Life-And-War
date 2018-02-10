# Game Of War
Game Of War is a cellular automaton game based on [Game of Life](https://www.youtube.com/watch?v=R9Plq-D1gEk). The rules are fairly simple:

For each civilization, the following rules apply:
* Any live cell with fewer than two live neighbours dies, as if caused by under-population.
* Any live cell with two or three live neighbours lives on to the next generation.
* Any live cell with more than three live neighbours dies, as if by over-population.
* Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

When civilizations meet, the following rules apply:
* A live cell existing next to only one neighbor of the opposing civilization becomes entrenched until killed off or aided.
* A live cell surrounded by more neighbors of the opposing civiliation than allied neighbors is killed, as if by war.
* A dead cell with even blue neighbors and even green neighbors stays dead.

Additionally, Game of War does not adhere to the standard infinite world that most Game of Life boards follow. Instead, Game of War takes place in a finite space.

# How to Play

### Prerequisites:
* Python 3
* Tkinter (Likely included w/ Python)

### Launching the Game
1. Navigate to the directory, then run `python .`, or you can specify the game board size by supplying the width and height, like `python . 800 600`. If the game board is not specified, it will dynamically calculate from the width and height of your screen. *Note: this calculation does not perform well with multiple monitors*. 

### Playing the Game
1. First, place the starting Green civiliazations by clicking on the grid. Next, select "Blue" from the radio buttons at the bottom and then place the starting Blue civilizations. 
2. Press "Start" to start the game, then "Stop" or "Reset" to finish.

---

This project turned out to be far more complex than I intially assumed, for a few reasons. 
Firstly, this was the first program I had written in Python, aside from smaller scripts. I chose Python mainly because I wanted to expand my knowledge of the language. However, I also knew that the primary backend data structure would be a multi-dimensional array and I like the way that Python handles lists. This was not as beneficial as I thought. Furthermore, it became apparent that Python does not scale well with larger systems. *Working with a dymanically typed, interpreted language is wonderful for quick scripts, but it becomes a burden to hold all that information in your head when working on a large system.* Additionally, it was hard to implement a good system design without clear static variables, classes and access modifiers, but most of that was a fault of my ignorance and not a shortcoming of the language. Another challenge in this project was effeciency. I challenged myself to come up with an effecient algorithm, and feel like I did a pretty good job, with tests taking an average of only 20 milliseconds to calculate the next board state, which I feel was a huge accomplishment. Overall, I am very happy with the project and the way it turned out. If I were to start over from the beginning, I would probably spend more time considering the overall design and familiarizing myself with some of the core components. For instance, the canvas component had some limitations that required me to tightly couple the GameLogic class with the GraphWidget class.

