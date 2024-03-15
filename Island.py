# Island Class
# x : x-coordinate
# y : y-coordinate
# num_bridges : number of bridges needed to satisfy constraint
# connections : List containing all current connections in the form of (Island, bridges_between)

class Island:
    def __init__(self, x, y, num_bridges):
        self.x = x
        self.y = y
        self.num_bridges = num_bridges
        self.cur_bridges = 0
        self.connections = []

    def add_connection(self, other_island, bridges_between):
        if bridges_between < 0 or bridges_between > 3:
            raise ValueError("Number of bridges must be between 0 and 3.")
        self.connections.append((other_island, bridges_between))
        self.cur_bridges += bridges_between
        other_island.connections.append((self, bridges_between))

    def is_fully_connected(self):
        total_bridges = 0
        for island, bridges_between in self.connections:
            total_bridges += bridges_between
        return total_bridges == self.num_bridges
        # return self.cur_bridges == self.num_bridges

    def remaining_capacity(self):
        total_bridges = 0
        for island, bridges_between in self.connections:
            total_bridges += bridges_between
        return self.num_bridges - total_bridges
        # return self.num_bridges - self.cur_bridges
