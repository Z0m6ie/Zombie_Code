# coding: utf-8

# """
# 8 TILE GAME
# States: location of 8 each tiles in 3x3 grid
# Initial state: Any state
# Actions: Up, Down, Left, Right
# Transition model: Given a state and an action, return resulting state
# Goal test: state matches the goal state?
# Path cost: Total moves, each move costs 1
# Expand: function that given a node, creates all children nodes
# """

# In[3]:
import sys, os, resource
from collections import deque
from math import sqrt
import time
start_time = time.time()
import heapq
# board = 8, 6, 7, 2, 5, 4, 3, 0, 1
# hard 8,6,7,2,5,4,3,0,1


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv

    if not args:
        print('usage: [--script] (bfs, dfs, ast, ida) (board config 1,2,0,..)')
        sys.exit(1)

    board = args[2]
    initialstate = [int(s) for s in board.split(',')]
    board = initialstate

    moveleft = []
    moveright = []
    for i, val in enumerate(board):
        if i == 0 or (i % (sqrt(len(board))) == 0):
            moveleft.append(i)
        if i == 0 or (i % (sqrt(len(board))) == 0):
            moveright.append(i - 1)
            moveright[0] = len(board) - 1

    frontier = deque()
    explored = set()
    h = []

    class Node:

        def __init__(self, state, parent, operator, depth, cost):
            # Contains the current state
            self.state = state
            # Contains the parent
            self.parent = parent
            # Contains the direction that generated node from parent
            self.operator = operator
            # depth of node
            self.depth = depth
            # path cost of node.
            self.cost = cost

    def createnode(state, parent, operator, depth, cost):
        return Node(state, parent, operator, depth, cost)

    def goalTest(state):
        goal = sorted(initialstate)
        if goal == state:
            return 'Success'

    def move(direction, state):
        state = list(state)
        if direction == 'Up':
            a, b = state.index(0), state.index(0) - (int(sqrt(len(board))))
            state[b], state[a] = state[a], state[b]
        elif direction == 'Down':
            x, y = state.index(0), state.index(0) + (int(sqrt(len(board))))
            state[y], state[x] = state[x], state[y]
        elif direction == 'Left':
            state.insert(state.index(0) - 1, state.pop(state.index(0)))
        elif direction == 'Right':
            state.insert(state.index(0) + 1, state.pop(state.index(0)))
        else:
            return 'fail'
        return state

    # location of hole
    def possible_moves(recentstate):
        holeLoc = recentstate.index(0)
        # possible moves
        moveOrder = deque()
        if holeLoc >= sqrt(len(board)):
            moveOrder.append('Up')
        if holeLoc < (len(board) - sqrt(len(board))):
            moveOrder.append('Down')
        if holeLoc not in moveleft:
            moveOrder.append('Left')
        if holeLoc not in moveright:
            moveOrder.append('Right')
        return moveOrder

    def frontieradd(currentstate):
        for i in possible_moves(currentstate.state):
            node = createnode((move(i, currentstate.state)), currentstate.state,
                              currentstate.operator + '%s,' % (i),
                              currentstate.depth + 1, 0)
            if tuple(node.state) not in explored:
                frontier.append(node)
                explored.add(tuple(node.state))
        return frontier

    def reversefrontieradd(currentstate):
        for i in reversed(possible_moves(currentstate.state)):
            node = createnode((move(i, currentstate.state)), currentstate.state,
                              currentstate.operator + '%s,' % (i),
                              currentstate.depth + 1, 0)
            if tuple(node.state) not in explored:
                frontier.append(node)
                explored.add(tuple(node.state))
        return frontier

    def bfs(initialstate):
        god_node = createnode(initialstate, 'none', '', 0, 0)
        explored.add(tuple(god_node.state))
        frontieradd(god_node)
        while frontier != deque([]):
            state = frontier.popleft()
            explored.add(tuple(state.state))
            if goalTest(state.state) == 'Success':
                finalpath = state.operator
                finalpath = finalpath.split(",")
                cost = len(finalpath)
                finaldepth = state.depth
                mem_usage = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)/1000
                text_file = open("output.txt", "w")
                text_file.write("path_to_goal: %r" % (finalpath) + "\n"
                                "cost_of_path: %r" % cost + "\n"
                                "nodes_expanded: %r" % len(explored) + "\n"
                                "fringe_size: %r" % len(frontier) + "\n"
                                "search_depth: %r" % finaldepth + "\n"
                                "running_time: %r" % (time.time() - start_time) + "\n"
                                "max_ram_usage: %r" % mem_usage)
                text_file.close()
                return 'Success'
            else:
                frontieradd(state)
        return 'fail'

    def dfs(initialState):
        god_node = createnode(initialstate, 'none', '', 0, 0)
        explored.add(tuple(god_node.state))
        reversefrontieradd(god_node)
        while frontier != deque([]):
            state = frontier.pop()
            explored.add(tuple(state.state))
            if goalTest(state.state) == 'Success':
                return state.state, state.operator, state.depth
            else:
                reversefrontieradd(state)
        return 'fail'

    # def ast(initialState):
    #     god_node = createnode(initialstate, 'none', '', 0, 0)
    #     explored.add(tuple(god_node.state))
    #     reversefrontieradd(god_node)
    #     # while frontier != deque([]):
    #     #     state = frontier.pop()
    #     #     explored.add(tuple(state.state))
    #     #     if goalTest(state.state) == 'Success':
    #     #         return state.state, state.operator, state.depth
    #     #     else:
    #     #         reversefrontieradd(state)
    #     # return 'fail'

    if args[1] == 'bfs':
        bfs(initialstate)

    elif args[1] == 'dfs':
        dfs(initialstate)


if __name__ == '__main__':
    main()
