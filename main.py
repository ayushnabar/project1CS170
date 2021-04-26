from search import *

goal_state = [['1', '2','3'],['4', '5','6'],['7', '8',' ']]
start_state = [['1', ' ','3'],['4', '2','6'],['7', '5','8']]


def main():
    j = Node(start_state, None, 0)
    j.expand_node()
    print(j.right.grid)
main()
