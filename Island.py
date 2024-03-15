class Island:
    """
    Represents an island in the Hashiwokakero puzzle.

    Attributes:
    - x (int): x-coordinate of the island.
    - y (int): y-coordinate of the island.
    - num_bridges (int): Number of bridges needed to satisfy the constraint.
    - cur_bridges (int): Number of bridges currently connected to this island.
    - connections (list): List containing all current connections in the form of tuples (Island, bridges_between).
    """

    def __init__(self, x, y, num_bridges):
        """
        Initializes an Island object.

        Args:
        - x (int): x-coordinate of the island.
        - y (int): y-coordinate of the island.
        - num_bridges (int): Number of bridges needed to satisfy the constraint.
        """
        self.x = x
        self.y = y
        self.num_bridges = num_bridges
        self.cur_bridges = 0
        self.connections = []

    def add_connection(self, other_island, bridges_between):
        """
        Adds a connection between this island and another island.

        Args:
        - other_island (Island): The other island to connect to.
        - bridges_between (int): Number of bridges between this island and the other island.
        
        Raises:
        - ValueError: If the number of bridges is not between 0 and 3.
        """
        if bridges_between < 0 or bridges_between > 3:
            raise ValueError("Number of bridges must be between 0 and 3.")
        self.connections.append((other_island, bridges_between))
        self.cur_bridges += bridges_between
        other_island.connections.append((self, bridges_between))

    def is_fully_connected(self):
        """
        Checks if the island is fully connected.

        Returns:
        - bool: True if the island is fully connected, False otherwise.
        """
        total_bridges = 0
        for island, bridges_between in self.connections:
            total_bridges += bridges_between
        return total_bridges == self.num_bridges

    def remaining_capacity(self):
        """
        Calculates the remaining capacity of the island.

        Returns:
        - int: Remaining capacity of the island.
        """
        total_bridges = 0
        for island, bridges_between in self.connections:
            total_bridges += bridges_between
        return self.num_bridges - total_bridges
