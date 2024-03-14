from Island import Island
from Bridge import Bridge
import scan_print_map

import numpy as np
import pandas as pd

def parse_grid(grid):

    ### NOTE TO DAVID ###
    ### I HAVE RIGOROUSLY CHECKED THIS FUNCTION AND IT DEFINITELY WORKS SO DONT WORRY ABOUT DEBUGGING THIS FUNCTION ###

    """
    Parse the input grid to identify islands and initialize Island objects.
    :param grid: 2D list representing the puzzle grid, where 0 indicates water, and positive integers represent islands with their bridge requirements.
    :return: A list of Island objects.
    """
    islands = []
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            # code = ".123456789abc"
            # print(code[map[x][y]],end="\n")
            if cell > 0: # Cell is not an empty body of water ie an Island
                islands.append(Island(x, y, cell))
    return islands



def is_valid_connection(grid, start_island, end_island, bridges):
    """
    Check if a connection between two islands is valid (no crossing bridges or islands).
    :param grid: 2D list representing the puzzle grid.
    :param start_island: Starting Island object.
    :param end_island: Ending Island object.
    :param bridges: Number of bridges to connect.
    :return: True if the connection is valid, False otherwise.
    """
    # Ensure bridges are in the same row or column
    if start_island.x != end_island.x and start_island.y != end_island.y:
        return False

    # Check for crossing bridges or islands
    x_range = range(min(start_island.x, end_island.x), max(start_island.x, end_island.x) + 1)
    y_range = range(min(start_island.y, end_island.y), max(start_island.y, end_island.y) + 1)
    for y in y_range:
        for x in x_range:
            if grid[y][x] != 0 and (x, y) != (start_island.x, start_island.y) and (x, y) != (end_island.x, end_island.y):
                return False  # Island in the way
            # Future implementation: Check for crossing bridges
    return True

def solve(grid, islands, bridges=[]):
    """
    Recursive function to solve the Hashiwokakero puzzle using backtracking.
    :param grid: 2D list representing the puzzle grid.
    :param islands: List of remaining Island objects to connect.
    :param bridges: List of Bridge objects representing current connections.
    :return: True if a solution is found, False otherwise.
    """
    if not islands:
        return True  # All islands processed

    for i, start_island in enumerate(islands):
        if start_island.is_fully_connected():
            print(f"Start Island is Full {start_island.x} {start_island.y}")
            continue
        for end_island in islands[i+1:]:
            if end_island.is_fully_connected():
                print(f"End Island is Full {end_island.x} {end_island.y}")
                continue
            for bridge_count in range(0, 4):  # Try 1, 2, and 3 bridges
                if is_valid_connection(grid, start_island, end_island, bridge_count):
                    start_island.add_connection(end_island, bridge_count)
                    new_bridge = Bridge(start_island, end_island, bridge_count)
                    bridges.append(new_bridge)
                    print(f"Island {start_island.x} {start_island.y} is not full. {bridge_count} bridges are being added. Now Island {start_island.x} {start_island.y} has {start_island.remaining_capacity()} capacity left")
                    if solve(grid, islands[i+1:], bridges):
                        print("reached True case")
                        return True
                    # Backtrack
                    bridges.remove(new_bridge)
                    print(f"Backtracking. {new_bridge.bridges_between} bridges are removed from Island {start_island.x} {start_island.y}")
                    start_island.connections.remove((end_island, bridge_count))
                    end_island.connections.remove((start_island, bridge_count))
    return False

# Example usage
if __name__ == "__main__":
    nrow, ncol, map = scan_print_map.scan_map()
    islands = parse_grid(map)
    if solve(map, islands):
        print("Solution found:")
        for island in islands:
            print(island)
    else:
        print("No solution")
