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
        self.fn = 0

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

    def calculate_hn(self, goal):
        hn = 0
        for i in range(3):
            for j in range(3):
                if(goal[i][j] != self.matrix[i][j] and self.matrix[i][j] != ' '):
                    hn += 1
        return hn

    def set_right_child(self, grid):
        self.right = grid
    def set_left_child(self, grid):
        self.left = grid
    def set_up_child(self, grid):
        self.left = grid
    def set_down_child(self, grid):
        self.down = grid

    def bfs():
        visited = set()
        visited.add(self.matrix)

    def expand_node(self):
        blankspace_col = self.get_column()
        blankspace_row = self.get_row()
        #generate node for blank space moving right, hence swiping left
        right_grid = self.grid
        if(self.get_column() != 2):
            temp = right_grid[self.get_row()][blankspace_col]
            right_grid[blankspace_row][blankspace_col] = right_grid[blankspace_row][blankspace_col+1]
            right_grid[blankspace_row][blankspace_col+1] = temp
            right_child = Node(right_grid, self, self.gn+1)
            self.set_right_child(right_child)


