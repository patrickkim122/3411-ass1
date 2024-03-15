"""
COMP3411 Term 1 2024 Assignment 1
"""
from Island import Island
from Bridge import Bridge
import scan_print_map

def parse_grid(grid):
    """
    Parse the input grid to identify islands and initialize Island objects.

    Args:
    - grid (list): 2D list representing the puzzle grid, where 0 indicates water, and positive integers represent islands with their bridge requirements.

    Returns:
    - list: A list of Island objects.
    """
    islands = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell > 0: # Cell is not an empty body of water, i.e., an Island
                islands.append(Island(x, y, cell))
    return islands

def is_valid_connection(grid, start_island, end_island, new_bridge, bridges):
    """
    Check if a connection between two islands is valid (no crossing bridges or islands).

    Args:
    - grid (list): 2D list representing the puzzle grid.
    - start_island (Island): Starting Island object.
    - end_island (Island): Ending Island object.
    - new_bridge (Bridge): Bridge object representing the potential new connection.
    - bridges (list): List of Bridge objects representing current connections.

    Returns:
    - bool: True if the connection is valid, False otherwise.
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
    
    for bridge in bridges:
        if bridge.start_island == start_island and bridge.end_island == end_island:
            return False
    
    for tile in new_bridge.getTiles():
        for bridge in bridges:
            if tile in bridge.getTiles():
                return False
    return True

def solve(grid, islands, bridges, original_islands=[]):
    """
    Recursive function to solve the Hashiwokakero puzzle using backtracking.

    Args:
    - grid (list): 2D list representing the puzzle grid.
    - islands (list): List of remaining Island objects to connect.
    - bridges (list): List of Bridge objects representing current connections.
    - original_islands (list): List of original Island objects.

    Returns:
    - bool: True if a solution is found, False otherwise.
    """
    if all(island.is_fully_connected() for island in original_islands):
        return True  # All islands processed
    
    if not islands:
        return True

    for i, start_island in enumerate(islands):
        if start_island.is_fully_connected():
            continue
        for end_island in islands:
            if start_island != end_island and end_island.is_fully_connected():
                continue
            for bridge_count in range(0, 4):  # Try 1, 2, and 3 bridges
                new_bridge = Bridge(start_island, end_island, bridge_count)
                if is_valid_connection(grid, start_island, end_island, new_bridge, bridges) and start_island.remaining_capacity() >= bridge_count and end_island.remaining_capacity() >= bridge_count:
                    start_island.add_connection(end_island, bridge_count)
                    bridges.append(new_bridge)
                    if solve(grid, islands, bridges, original_islands=original_islands):
                        return True

                    # Backtrack
                    bridges.remove(new_bridge)
                    start_island.connections.remove((end_island, bridge_count))
                    start_island.cur_bridges -= bridge_count
                    end_island.connections.remove((start_island, bridge_count))
                    end_island.cur_bridges -= bridge_count
    return False

def print_solution(nrow, ncol, grid, islands, bridges):
    """
    Print the solution to the Hashiwokakero puzzle.

    Args:
    - nrow (int): Number of rows in the puzzle grid.
    - ncol (int): Number of columns in the puzzle grid.
    - grid (list): 2D list representing the puzzle grid.
    - islands (list): List of Island objects.
    - bridges (list): List of Bridge objects representing connections.
    """
    code = ".123456789abc"
    for row in range(nrow):
        for col in range(ncol):
            if code[grid[row][col]] != '.':
                print(code[grid[row][col]], end="")
            else:
                is_bridge = False
                for bridge in bridges:
                    if [col, row] in bridge.getTiles():
                        print(bridge.getType(), end="")
                        is_bridge = True
                        break
                if not is_bridge:
                    print(" ", end="")
        print()
                
# Example usage
if __name__ == "__main__":
    nrow, ncol, grid = scan_print_map.scan_map()
    islands = parse_grid(grid)
    bridges = []
    if solve(grid, islands, bridges, original_islands=islands):
        print_solution(nrow, ncol, grid, islands, bridges)
    else:
        print("No solution")
