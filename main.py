from search import *
import Queue

#initialize goal and default start state
goal_state = [['1', '2','3'],['4', '5','6'],['7', '8',' ']]
start_state = [['1', '3',' '],['4', '2','6'],['7', '5','8']]

#recursive function to print parent -> solution node steps
def print_lineage(node):
    gn = node.gn
    hn = node.hn
    #base case once we reach the adam/eve parent node
    if node.parent == None:
        print "The best state to expand with g(n) = ", gn,"and h(n) = ", hn ," is... \n"
        node.print_grid()
        return
    #recursive statement to print the grid and gn, hn values
    print_lineage(node.parent)
    print "The best state to expand with g(n) = ", gn,"and h(n) = ", hn ," is... \n"
    node.print_grid()

#UNIFORM COST SEARCH
def bfs(root):
    #initialize queue size, nodes, explored set variables
    #we could use a set here to make checking for duplicates easier, but not too well versed in it
    max_queue_size = 0
    nodes_expanded = 0
    explored = []
    #initialize our parent
    j = Node(root, None, 0)
    q = Queue.PriorityQueue()
    q.put((j.fn, j))
    while not q.empty():
    # g(n) should increase and h(n) should decrease
        temp = q.get()
        node = temp[1]
        # goal state reached
        if(node.grid == goal_state):
            print_lineage(node)
            print "To solve this problem the search algorithm expanded a total of ", nodes_expanded, " nodes."
            print "The maximum number of nodes in the queue at any one time: ", max_queue_size
            return node.grid
        # add to explored set, will keep expanding expanding
        explored.append(node.grid)
        l = node.expand_node()
        nodes_expanded+=1
        #add node to frontier if not seen before
        for n in l:
            if n.grid not in explored:
                q.put((n.fn, n))
        # cannot use .qsize function so convert queue to list and find length
        l = list(q.queue)
        if(len(l) > max_queue_size):
                max_queue_size = len(l)


# MISPLACED HEURISITC
def misplaced(root):
    max_queue_size = 0
    nodes_expanded = 0
    explored = []
    j = Node(root, None, 0)
    q = Queue.PriorityQueue()
    q.put((j.fn, j))
    print(j.fn)
    while not q.empty():

        temp = q.get()
        node = temp[1]

        if(node.grid == goal_state):
            print_lineage(node)
            print "To solve this problem the search algorithm expanded a total of", nodes_expanded, "nodes."
            print "The maximum number of nodes in the queue at any one time: ", max_queue_size
            return node.grid
        l = node.expand_node()
        nodes_expanded+=1

        for n in l:
            if n not in explored:
                # calculate misplaced heuristic
                n.misplaced_heuristic(goal_state)
                q.put((n.fn, n))

        l = list(q.queue)
        if(len(l) > max_queue_size):
                max_queue_size = len(l)

# EUCLIDEAN HEURISTIC
def euclidean(root):
    max_queue_size = 0
    nodes_expanded= 0
    explored = []
    j = Node(root, None, 0)
    q = Queue.PriorityQueue()
    q.put((j.fn, j))

    e=0
    while not q.empty():

        temp = q.get()
        node = temp[1]
        if(node.grid == goal_state):
            print_lineage(node)
            print "To solve this problem the search algorithm expanded a total of ", nodes_expanded, " nodes."
            print "The maximum number of nodes in the queue at any one time: ", max_queue_size
            return node.grid
        l = node.expand_node()
        nodes_expanded+=1
        for n in l:
            if n not in explored:
                # calculate euclidean heuristic
                n.euclidean_heuristic(goal_state)
                q.put((n.fn, n))

        l = list(q.queue)
        if(len(l) > max_queue_size):
                max_queue_size = len(l)

def input_grid():
    grid = []
    puzzle_type = raw_input("Type 1 to use a default puzzle, or 2 to enter your own puzzle: ")
    if puzzle_type == '1':
        print("We are using the default puzzle.")
        grid = temp_state
        return grid

    elif puzzle_type == '2':
        print("Enter your puzzle, use a zero to represent the blank")

        row_one = raw_input("Enter the first row, use space or tabs between numbers: ")
        row_one = row_one.split(' ')
        if row_one.count('0') == 1:
            row_one[row_one.index('0')] = ' '
        grid.append(row_one)

        row_two = raw_input("Enter the second row, use space or tabs between numbers: ")
        row_two = row_two.split(' ')
        if row_two.count('0') == 1:
            row_two[row_two.index('0')] = ' '
        grid.append(row_two)

        row_three = raw_input("Enter the third row, use space or tabs between numbers: ")
        row_three = row_three.split(' ')
        if row_three.count('0') == 1:
            row_three[row_three.index('0')] = ' '
        grid.append(row_three)

        return grid

    elif puzzle_type == '3':
        sys.exit(0)

def main():
    print "Welcome to 862169589's 8 puzzle solver."
    initial_node = Node(input_grid(), None, 0)

    print "Enter you choice of algorithm \n"
    print "Uniform Cost Search"
    print "A* with the Misplaced Tile heuristic"
    print "A* with the Eucledian distance heuristic"
    algorithm_type = raw_input("Type 1 for Uniform Cost Search, 2 for Misplaced Tile, 3 for Euclidean distance: ")
    nodes_expanded = 0
    if algorithm_type == '1':
        nodes_expanded = bfs(initial_node.grid)
    elif algorithm_type == '2':
        nodes_expanded = misplaced(initial_node.grid)
    elif algorithm_type == '3':
        nodes_expanded = euclidean(initial_node.grid)

if __name__ == "__main__":
    main()
