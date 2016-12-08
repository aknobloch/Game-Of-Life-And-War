# Game-Of-War
Game Of War is a cellular automaton game based on [Game of Life](https://www.youtube.com/watch?v=R9Plq-D1gEk). The rules are fairly simple:

For each civilization, the following rules apply:
* Any live cell with fewer than two live neighbours dies, as if caused by under-population.
* Any live cell with two or three live neighbours lives on to the next generation.
* Any live cell with more than three live neighbours dies, as if by over-population.
* Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

When civilizations meet, the following rules apply:
* A live cell surrounded by 2 or more neighbors of the opposing civiliation is killed, as if by war.
* A live cell existing next to only one neighbor of the opposing civilization becomes entrenched until killed off or aided.
* A dead cell with even blue neighbors and even green neighbors stays dead.

