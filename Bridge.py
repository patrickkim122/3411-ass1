class Bridge:
    """
    Represents a bridge between two islands.
    
    Attributes:
        start_island (Island): The island from which the bridge starts.
        end_island (Island): The island at which the bridge ends.
        bridges_between (int): The number of bridges connecting the two islands.
    """
    def __init__(self, start_island, end_island, bridges_between):
        """
        Initializes a Bridge object.

        Args:
            start_island (Island): The island from which the bridge starts.
            end_island (Island): The island at which the bridge ends.
            bridges_between (int): The number of bridges connecting the two islands.
        
        Raises:
            ValueError: If bridges_between is not between 0 and 3.
        """
        if bridges_between < 0 or bridges_between > 3:
            raise ValueError("Number of bridges must be between 0 and 3.")
        self.start_island = start_island
        self.end_island = end_island
        self.bridges_between = bridges_between

    def getTiles(self):
        """
        Gets the tiles occupied by the bridge.

        Returns:
            list: A list of tiles occupied by the bridge.
        """
        tiles = []
        i = 0
        if self.start_island.x - self.end_island.x < 0:
            while self.start_island.x + i < self.end_island.x:
                tiles.append([self.start_island.x + i, self.start_island.y])
                i += 1
        elif self.start_island.x - self.end_island.x > 0:
            while self.start_island.x - i > self.end_island.x:
                tiles.append([self.start_island.x - i, self.start_island.y])
                i += 1
        elif self.start_island.y - self.end_island.y < 0:
            while self.start_island.y + i < self.end_island.y:
                tiles.append([self.start_island.x, self.start_island.y + 1])
                i += 1
        elif self.start_island.y - self.end_island.y > 0:
            while self.start_island.y - i > self.end_island.y:
                tiles.append([self.start_island.x, self.start_island.y - 1])
                i += 1
        return tiles
    
    def getType(self):
        """
        Gets the type of the bridge.

        Returns:
            str: The type of the bridge.
        """
        if self.bridges_between == 0:
            return ' '
        elif self.start_island.x != self.end_island.x: # Horizontal Bridge
            if self.bridges_between == 1:
                return '-'
            elif self.bridges_between == 2:
                return '='
            else:
                return 'E'
        else:
            if self.bridges_between == 1:
                return '|'
            elif self.bridges_between == 2:
                return '\"'
            else:
                return '#'
