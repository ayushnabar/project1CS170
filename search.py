import queue, copy

class Node:

    def __init__(self, matrix, parent, gn):
        self.grid = matrix
        self.parent = None
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.hn = 0
        self.gn = 0
        self.fn = self.gn + self.hn

    def __lt__(self, other):
        return self.fn < other.fn
    def __le__(self, other):
        return self.fn <= other.fn
    def __eq__(self, other):
        return self.fn == other.fn
    def __ne__(self, other):
        return self.fn != other.fn
    def __gt__(self, other):
        return self.fn > other.fn
    def __ge__(self, other):
        return self.fn >= other.fn

    def set_right_child(self, child):
        self.right = child

    def set_left_child(self, child):
        self.left = child

    def set_up_child(self, child):
        self.up = child

    def set_down_child(self, child):
        self.down = child

    def get_fn(self):
        return self.hn + self.gn

    def get_column(self):
        for i in range(3):
            for j in range(3):
                if(self.grid[i][j] == ' '):
                    return j

    def get_row(self):
        for i in range(3):
            for j in range(3):
                if(self.grid[i][j] == ' '):
                    return i

    def update_heuristic(self, goal):
        h = 0
        for i in range(3):
            for j in range(3):
                if(goal[i][j] != self.grid[i][j] and self.grid[i][j] != ' '):
                    h += 1
        self.hn = h
        self.fn = h + self.gn

    # def set_right_child(self, grid):
    #     self.right = grid
    # def set_left_child(self, grid):
    #     self.left = grid
    # def set_up_child(self, grid):
    #     self.left = grid
    # def set_down_child(self, grid):
    #     self.down = grid

    def expand_node(self):
        frontier = []
        blank_col = self.get_column()
        blank_row = self.get_row()
        #generate node for blank space moving right, hence swiping the tile to the left
        right_grid = copy.deepcopy(self.grid)
        if(self.get_column() != 2):
            temp = right_grid[blank_row][blank_col]
            right_grid[blank_row][blank_col] = right_grid[blank_row][blank_col+1]
            right_grid[blank_row][blank_col+1] = temp
            right_child = Node(right_grid, self, self.gn+1)
            self.set_right_child(right_child)
            frontier.append(right_child)

        #generate node for blank space moving to the left, hence swiping the tile to the right
        left_grid = copy.deepcopy(self.grid)
        if(self.get_column() != 0):
            temp = left_grid[blank_row][blank_col]
            left_grid[blank_row][blank_col] = left_grid[blank_row][blank_col-1]
            left_grid[blank_row][blank_col-1] = temp
            left_child = Node(left_grid, self, self.gn+1)
            self.set_left_child(left_child)
            frontier.append(left_child)

        #generate node for blank space moving up, hence swiping the tile down
        up_grid = copy.deepcopy(self.grid)
        if(self.get_row() != 0):
            temp = up_grid[blank_row][blank_col]
            up_grid[blank_row][blank_col] = up_grid[blank_row-1][blank_col]
            up_grid[blank_row-1][blank_col] = temp
            up_child = Node(up_grid, self, self.gn+1)
            self.set_up_child(up_child)
            frontier.append(up_child)

        #generate node for blank space moving down, hence swiping the tile up
        down_grid = copy.deepcopy(self.grid)
        if(self.get_row() != 2):
            temp = down_grid[blank_row][blank_col]
            down_grid[blank_row][blank_col] = down_grid[blank_row+1][blank_col]
            down_grid[blank_row+1][blank_col] = temp
            down_child = Node(down_grid, self, self.gn+1)
            self.set_down_child(down_child)
            frontier.append(down_child)

        return frontier




