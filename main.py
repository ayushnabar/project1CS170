from search import *
import queue

goal_state = [['1', '2','3'],['4', '5','6'],['7', '8',' ']]
start_state = [['1', '3',' '],['4', '2','6'],['7', '5','8']]
temp_state = [['1', '2','3'],['4', '5','6'],['7', ' ', '8']]

def bfs(root):
        explored = []
        j = Node(root, None, 0)
        q = queue.PriorityQueue()
        q.put((j.fn, j))
        e=0
        while not q.empty() and e < 10:

            temp = q.get()
            node = temp[1]
            print(node.grid)
            print("dfsafsdafasd")
            if(node.grid == goal_state):
                return node.grid

            l = node.expand_node()
            for n in l:
                print(n.grid)
                if n not in explored:
                    q.put((n.fn, n))
            e+=1

def misplaced(root):
        explored = []
        j = Node(root, None, 0)
        q = queue.PriorityQueue()
        q.put((j.fn, j))
        e=0
        while not q.empty():

            temp = q.get()
            node = temp[1]
            if(node.grid == goal_state):
                return node.grid
            print(node.grid)
            l = node.expand_node()
            for n in l:
                if n not in explored:
                    n.update_heuristic(goal_state)
                    q.put((n.fn, n))


def main():
    print(misplaced(start_state))

main()
