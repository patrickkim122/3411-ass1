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