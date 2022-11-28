# Task: If you were to design a robotic lawnmower
# 1) what PROGRAM would you write for it
# 2) what ALGORITHM would you use to keep the entire garden tidy and cut the grass!
# 3) Create a basic simulation using a technology of your choice (e.g.: Java, C++, PYTHON, MATLAB, ...).
# 4) The simulation does not have to be graphic, it is enough if e.g. you INDICATE THE PATH with CHARACTERS;
# 5) there is NO need to request INPUT parameters from the user.

# Approach
# 1) Program consists of 2 classes: main, map
# 2) Chosen algorithm: Graph Traversal
# 3) Chosen language: Python
# 4) Visualization with grids
# 5) Input hardcoded, but can be replaced

# Possible improvements:
# Logical
#   1) Map can be improved to support not only rectangular shapes
#   2) Lawnmower class, instantiating garden
#   3) Lawnmower placement
#   4) Better edge case handling/algorithm improvements
#   5) Adding sensors
#   6) Obstruction recognition
# Visualization changes

import os
import time

from map import *

# Manual testcase
# grid = [
#     ['0', '0', '1', '1', '0'],
#     ['1', '0', '1', '1', '1'],
#     ['1', '1', '0', '0', '1'],
#     ['1', '1', '0', '0', '1'],
#     ['0', '0', '1', '0', '0'],
#     ['1', '1', '0', '0', '0'],
# ]

if __name__ == "__main__":
    print("""\nLegend for below grid:
        1: Large grass
        0: Short grass
        L: Lawnmower\n""")
    # time.sleep(5)

    grid1 = create_grid(5)
    print("Basic Linear Search:\n")
    print_grid(grid1)
    time.sleep(5)
    # print_grid(grid1)
    # print()
    basic_mowing(grid1)
    print("Result:\n")
    print_grid(grid1)
    time.sleep(2)
    os.system('cls')

    grid2 = create_grid(5)
    print("\nDepth First Search Iterative:\n")
    print_grid(grid2)
    time.sleep(5)
    # print_grid(grid2)
    print()
    dfs_iter_mowing(grid2)
    print("Result:\n")
    print_grid(grid2)
    time.sleep(2)
    os.system('cls')

    grid3 = create_grid(5)
    print("\nDepth First Search Recursive:\n")
    print_grid(grid3)
    time.sleep(5)
    # print_grid(grid3)
    dfs_rec_mowing(grid3)
    print("Result:\n")
    print_grid(grid3)
    time.sleep(2)
