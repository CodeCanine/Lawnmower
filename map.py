import numpy as np
import time
import os


# Method declarations for main.py

# r = row
# c = column
# Time complexity = O(rc)
# Space complexity = O(rc)
class Map:
    def __init__(self, *n):
        self.grid = None
        self.n = n[0]
        if len(n) > 1:
            self.m = n[1]
        else:
            self.m = None
        self.create_grid()

    def create_grid(self):
        if self.m is None:
            self.grid = np.random.randint(0, 2, size=(self.n, self.n)).astype(str)
        else:
            self.grid = np.random.randint(0, 2, size=(self.n, self.m)).astype(str)

    # Basic method to show grid
    def print_grid(self):
        print(self.grid)
        time.sleep(0.1)

    # Basic solution, no algorithm, linear search
    # Direction:
    # ----->
    # <-----
    # ----->
    # <-----
    # ----->
    def basic_mowing(self):
        # Check all the rows
        # print_grid(grid)
        # time.sleep(2)
        os.system('cls')
        for row in range(0, len(self.grid), 1):
            # And columns
            # Asymmetry grid [0]
            if row % 2 == 0:
                # ->
                for col in range(0, len(self.grid[0]), 1):
                    # If it finds '1' (grass) cut it (turn it to '0')
                    if self.grid[row][col] == '1':
                        self.grid[row][col] = 'L'

                        # print_grid(grid)
                        # os.system('cls')
                    else:
                        self.grid[row][col] = 'L'
                        # print_grid(grid)
                        # os.system('cls')
                    self.print_grid()
                    os.system('cls')
                    self.grid[row][col] = '0'

            else:
                # <-
                for col in range(len(self.grid[0]) - 1, -1, -1):
                    # If it finds '1' (grass) cut it (turn it to '0')
                    if self.grid[row][col] == '1':
                        self.grid[row][col] = 'L'
                        # print_grid(grid)
                        # os.system('cls')
                    else:
                        self.grid[row][col] = 'L'
                        # print_grid(grid)
                        # os.system('cls')
                    self.print_grid()
                    os.system('cls')
                    self.grid[row][col] = '0'

    # Depth First Search - Iterative approach
    # Direction:
    # ----->
    # >---xv
    # ^---<v
    # >---^v
    # ^----v
    def dfs_iter_mowing(self):
        # Stack to be working from with (0,0) start (grid index) value (top left corner)
        # print_grid(grid)
        os.system('cls')
        stack = [(0, 0)]
        # Empty set to be populated, to avoid cycles
        cut_grass = set()
        while stack:
            # Taking the last added element of stack (LIFO), and removing from the stack
            row, col = stack.pop()
            # If this element-pair is already visited, skip it
            if (row, col) in cut_grass:
                continue
            # Add the element to the visited tiles set (no duplicates will be added)
            cut_grass.add((row, col))
            # If it is '1' (grass), turn it to 'L' (move the 'L'awnmower)
            if self.grid[row][col] == "1":
                self.grid[row][col] = "L"
                # Show the current state
                self.print_grid()
                os.system('cls')

            # If it is '0' (clean) turn it to 'L' (move the 'L'awnmower)
            else:
                self.grid[row][col] = "L"
                # Show the current state
                self.print_grid()
                os.system('cls')
            # In any case, after showing the current state, turn the tile to '0' (cut the grass)
            self.grid[row][col] = "0"

            # Directions:
            # Upwards
            if 0 <= row - 1 < len(self.grid):
                stack.append(tuple((row - 1, col)))
            # Left
            if 0 <= col - 1 < len(self.grid[0]):
                stack.append(tuple((row, col - 1)))
            # Downwards
            if 0 <= row + 1 < len(self.grid):
                stack.append(tuple((row + 1, col)))
            # Right
            if 0 <= col + 1 < len(self.grid[0]):
                stack.append(tuple((row, col + 1)))

    # Depth First Search - Recursive approach
    # No given direction, it will consider islands of grass patches, cut them,
    # then move back until it can find another grass patch.
    # If no grass can be found along the given path, go back to the first '0'
    def dfs_rec_mowing(self):
        os.system('cls')
        self.print_grid()
        # Set to avoid going in loops
        # Declaring outside the helper method, to avoid t resetting with every call.
        cut_grass = set()
        # Just to keep track of grass patches removed
        grass_patches = 0
        # Need to traverse the whole grid, therefore nested for loop
        for row in range(0, len(self.grid), 1):
            # Asymmetry grid [0]
            for col in range(0, len(self.grid[0]), 1):
                # If helper function finds a patch count it (optional)
                if self.hunt_grass(self.grid, row, col, cut_grass) is True:
                    grass_patches += 1
        print(f'Grass patch(es) removed: {grass_patches}')

    def hunt_grass(self, grid, row, col, cut_grass):
        # Due to the nature of traversal, to avoid multiple ifs, a boundary must be given to the 'L'awnmower,
        # To avoid fx.: (-1,0) or (4,5) coordinates, that fall outside the grid
        row_inbounds = 0 <= row < len(grid)
        col_inbounds = 0 <= col < len(grid[0])
        # Checking if we are still in the given grid
        self.print_grid()
        os.system('cls')
        if not row_inbounds or not col_inbounds:
            return False
        # Check if tile is a patch of grass
        if grid[row][col] == "0":
            return False
        # If it is, move the 'L'awnmower there
        else:
            grid[row][col] = "L"
            # Show the current state
            self.print_grid()
            os.system('cls')
        # Then turn it to '0' (cut the grass)
        grid[row][col] = "0"
        # Create a tuple from the current tile's indexes, to avoid for example 0,1 and 1,0 being the same
        current = (row, col)
        # Cycle prevention
        if current in cut_grass:
            return False
        # Add the tile to the visited set outside the method
        cut_grass.add(current)
        # Check Upwards Tile
        self.hunt_grass(grid, row - 1, col, cut_grass)
        # Check Left Tile
        self.hunt_grass(grid, row, col - 1, cut_grass)
        # Check Downwards Tile
        self.hunt_grass(grid, row + 1, col, cut_grass)
        # Check Right Tile
        self.hunt_grass(grid, row, col + 1, cut_grass)
        # If this returns True, it means it has found grass, and gives this back to the main function call
        return True

    # Creating grid, converting elements to string, so the 'L'awnmower is visible
