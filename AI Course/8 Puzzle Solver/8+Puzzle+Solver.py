
# coding: utf-8

# Begin by writing a class to represent the state of the game at a given turn, including parent and child nodes. We suggest writing a separate solver class to work with the state class. Feel free to experiment with your design, for example including a board class to represent the low-level physical configuration of the tiles, delegating the high-level functionality to the state class.
#
# """
# DEFINITIONS
#
# Initial state: state in which agent starts
#
# States s: All states reachable from initial state by any sequence of actions
# (State space)
#
# Actions a: Possible actions available to the agent at current state Actions(s)
# this is Action space
#
# Transitional model: A description of what each action does Results(s,a)
#
# Goal Test: determins if a given state is a goal state
#
# Path cost: function that assigns a numeric cost to a path w.r.t. performance
# measure
# """
#
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

# """
# BFS Breadth-First-Search
#
# def Breadth-First-Search(initialState, goalTest):
#     frontier = Queue.new(initialState)
#     explored = Set.new()
#     while not frontier.isEmpty():
#         state = frontier.dequeue()
#         explored.add(state)
#         if goalTest(state):
#             return Success(state)
#         for neighbor in state.neighbors():
#             if neighbor not in frontier U explored:
#                 frontier.enqueue(state)
#     return Failure
# """
# """
# DFS Depth-First-Search
#
# def Depth-First-Search(initialState, goalTest):
#     frontier = Stack.new(initialState)
#     explored = Set.new()
#     while not frontier.isEmpty():
#         state = frontier.pop()
#         explored.add(state)
#         if goalTest(state):
#             return Success(state)
#         for neighbor in state.neighbors():
#             if neighbor not in frontier U explored:
#                 frontier.push(state)
#     return Failure
# """

# In[3]:

from collections import deque
from math import sqrt
import timeit
import heapq
board = 8, 6, 7, 2, 5, 4, 3, 0, 1
# hard 8,6,7,2,5,4,3,0,1
frontier = deque()
explored = set()
initialstate = list(board)
path_to_node = set()
h = []

moveleft = []
moveright = []
for i, val in enumerate(board):
    if i == 0 or (i % (sqrt(len(board))) == 0):
        moveleft.append(i)
    if i == 0 or (i % (sqrt(len(board))) == 0):
        moveright.append(i-1)
        moveright[0] = len(board)-1


# In[4]:

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


# In[5]:

def createnode(state, parent, operator, depth, cost):
    return Node(state, parent, operator, depth, cost)


# In[6]:

def goalTest(state):
    goal = sorted(initialstate)
    if goal == state:
        return 'Success'


# In[ ]:

# if goalTest(initialstate) == 'Success':
#     print ("Success")
# else:
#     explored.add(tuple(initialstate))


# In[7]:

# Move

def move(direction, state):
    state = list(state)
    if direction == 'Up':
        a, b = state.index(0), state.index(0)-(int(sqrt(len(board))))
        state[b], state[a] = state[a], state[b]
    elif direction == 'Down':
        x, y = state.index(0), state.index(0)+(int(sqrt(len(board))))
        state[y], state[x] = state[x], state[y]
    elif direction == 'Left':
        state.insert(state.index(0) - 1, state.pop(state.index(0)))
    elif direction == 'Right':
        state.insert(state.index(0) + 1, state.pop(state.index(0)))
    else:
        return 'fail'
    return state


# In[8]:

# location of hole
def possible_moves(recentstate):
    holeLoc = recentstate.index(0)
    # possible moves
    moveOrder = deque()
    if holeLoc > sqrt(len(board)):
        moveOrder.append('Up')
    if holeLoc < (len(board)-sqrt(len(board))):
        moveOrder.append('Down')
    if holeLoc not in moveleft:
        moveOrder.append('Left')
    if holeLoc not in moveright:
        moveOrder.append('Right')
    return moveOrder


# In[18]:

def frontieradd(currentstate):
    for i in possible_moves(currentstate.state):
        node = createnode((move(i, currentstate.state)), currentstate.state,
                          currentstate.operator + '%s, ' % (i),
                          currentstate.depth+1, 0)
        if tuple(node.state) not in explored:
            frontier.append(node)
            explored.add(tuple(node.state))
    return frontier


# In[ ]:

# def frontieradd(currentstate):
#     for i in possible_moves(currentstate.state):
#         node = createnode((move(i, currentstate.state)), currentstate.state, currentstate.operator + '%s, ' %(i), currentstate.depth+1, 0 )
#         if node.state not in frontier and tuple(node.state) not in explored:
#             frontier.append(node)
#             explored.add(tuple(node.state))
#     return frontier


# In[9]:

def reversefrontieradd(currentstate):
    for i in reversed(possible_moves(currentstate.state)):
        node = createnode((move(i, currentstate.state)), currentstate.state,
                          currentstate.operator + '%s, ' % (i),
                          currentstate.depth+1, 0)
        if tuple(node.state) not in explored:
            frontier.append(node)
            explored.add(tuple(node.state))
    return frontier


# In[19]:

def bfs(initialstate):
    god_node = createnode(initialstate, 'none', '', 0, 0)
    explored.add(tuple(god_node.state))
    frontieradd(god_node)
    while frontier != deque([]):
        state = frontier.popleft()
        explored.add(tuple(state.state))
        if goalTest(state.state) == 'Success':
            return state.state, state.operator, state.depth
        else:
            frontieradd(state)
    return 'fail'
bfs(initialstate)


# In[10]:

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
dfs(initialstate)


# In[ ]:

def ast(initialState):
    god_node = createnode(initialstate, 'none', '', 0, 0)
    explored.add(tuple(god_node.state))


# In[ ]:

# #END OF TEST
# for i in frontier:
#     if tuple(i) not in explored:
#         print('true')
#     else:
#         print('false')


# In[20]:

len(explored)
