# Path Finding Visualizer

This project is made on **Pygame**. It uses A* Search Algorithm, which is an "informed" graph-traversal technique. It uses a heuristic-based approach to find the short path between two nodes while avoiding walls. I have used Manhattan distance to calculate the path in this project.


## Working of the visualiser

Choose a starting cell and ending cell in the 2D matrix, by left-clicking on them. Now, choose the cells which are to be blocked (walls). We can reset the cells by right-clicking on them. Here, the magenta cell represents the starting cell and blue cell represents the ending cell. The black cells represent walls.


### Representation of Starting Cell, Ending Cell and Blocked Cells

![alt text](https://i.imgur.com/0ixdjUt.png)

Press the spacebar key to run the algorithm. As soon as the ending node is found by the A* Search algorithm, a red-coloured path appears connecting the starting cell and ending cell.

### Representation of the Path

![alt text](https://i.imgur.com/SwsbMED.png)

