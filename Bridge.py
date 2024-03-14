# Bridge Class
# island_1 : the island that called the bridge_connect function
# island_2 : the other island
# bridges_between : the number of bridges that connect the two islands

class Bridge:
    def __init__(self, start_island, end_island, bridges_between):
        if bridges_between < 0 or bridges_between > 3:
            raise ValueError("Number of bridges must be between 0 and 3.")
        self.start_island = start_island
        self.end_island = end_island
        self.bridges_between = bridges_between

    def getTiles(self):
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
    