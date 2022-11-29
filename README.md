# Lawnmower
Interview Task - Lawnmover

**Task: If you were to design a robotic lawnmower**
1) what PROGRAM would you write for it
2) what ALGORITHM would you use to keep the entire garden tidy and cut the grass!
3) Create a basic simulation using a technology of your choice (e.g.: Java, C++, PYTHON, MATLAB, ...).
4) The simulation does not have to be graphic, it is enough if e.g. you INDICATE THE PATH with CHARACTERS;
5) there is NO need to request INPUT parameters from the user.

**Approach**
1) Program consists of 2 classes: main, map
2) Chosen algorithm: Graph Traversal
3) Chosen language: Python
4) Visualization with grids
5) Input hardcoded, but can be replaced

**Possible improvements:**

Logical
1) Map can be improved to support not only rectangular shapes
2) Lawnmower class, instantiating garden
3) Lawnmower placement
4) Better edge case handling/algorithm improvements
5) Adding sensors
6) Obstruction recognition

Visualization changes

Chosen approach:

Create random numpy array (0s and 1s), to represent the layout (1 is grass 0 is clean tile).
Traverse through all tiles, with different methods, and set the grass (1) to cut (0).

**(Base Layout:)**
![](Gif/first.gif)

**Chose Approaches:**

**Linear Search:**
![](Gif/second.gif)

**Depth First Search Iterative Approach:**
![](Gif/third.gif)

**Depth First Search Recursive Approach:**
![](Gif/fourth.gif)

**Summary:**
Perfect task to practice graph traversing algorithms, that can be presented in an interview environment.
