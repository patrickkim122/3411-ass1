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



def is_valid_connection(grid, start_island, end_island, new_bridge, bridges):
    """
    Check if a connection between two islands is valid (no crossing bridges or islands).
    :param grid: 2D list representing the puzzle grid.
    :param start_island: Starting Island object.
    :param end_island: Ending Island object.
    :param bridges: Number of bridges to connect.
    :return: True if the connection is valid, False otherwise.
    """
    if start_island.x == end_island.x and start_island.y == end_island.y:
        return False
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
    for bridge in bridges:
        if bridge.start_island == start_island and bridge.end_island == end_island:
            return False
    
    for tile in new_bridge.getTiles():
        for bridge in bridges:
            if tile in bridge.getTiles():
                return False
    return True

def solve(grid, islands, bridges=[], original_islands=[]):
    """
    Recursive function to solve the Hashiwokakero puzzle using backtracking.
    :param grid: 2D list representing the puzzle grid.
    :param islands: List of remaining Island objects to connect.
    :param bridges: List of Bridge objects representing current connections.
    :return: True if a solution is found, False otherwise.
    """
    island_bruh = []
    for island in islands:
        island_bruh.append([island.x, island.y])
    print(f"Islands array: {island_bruh}")
    if all(island.is_fully_connected() for island in original_islands):
        return True  # All islands processed
    
    if not islands:
        return True

    for i, start_island in enumerate(islands):
        if start_island.is_fully_connected():
            print(f"Start Island is Full {start_island.x} {start_island.y}")
            continue
        for end_island in islands:
            if start_island != end_island and end_island.is_fully_connected():
                print(f"End Island is Full {end_island.x} {end_island.y}")
                continue
            for bridge_count in range(0, 4):  # Try 1, 2, and 3 bridges
                new_bridge = Bridge(start_island, end_island, bridge_count)
                if is_valid_connection(grid, start_island, end_island, new_bridge, bridges) and start_island.remaining_capacity() >= bridge_count and end_island.remaining_capacity() >= bridge_count:
                    start_island.add_connection(end_island, bridge_count)
                    bridges.append(new_bridge)
                    print(f"{bridge_count} bridges are being connected from Island {start_island.x} {start_island.y} to Island {end_island.x} {end_island.y}. Now Island {start_island.x} {start_island.y} has {start_island.remaining_capacity()} capacity left and Island {end_island.x} {end_island.y} has {end_island.remaining_capacity()} capacity left")
                    if solve(grid, islands, bridges, original_islands=original_islands):
                        print("reached True case")
                        return True
                    # Backtrack
                    bridges.remove(new_bridge)
                    print(f"Backtracking. {new_bridge.bridges_between} bridges are removed from Island {start_island.x} {start_island.y} and Island {end_island.x} {end_island.y}")
                    start_island.connections.remove((end_island, bridge_count))
                    end_island.connections.remove((start_island, bridge_count))
    return False

def print_solution(map, islands):
    


# Example usage
if __name__ == "__main__":
    nrow, ncol, map = scan_print_map.scan_map()
    islands = parse_grid(map)
    if solve(map, islands, original_islands=islands):
        print("Solution found:")
        for island in islands:
            print(f"{island.x} {island.y} {island.connections}")
        # return print_solution(map, islands)
    else:
        print("No solution")
