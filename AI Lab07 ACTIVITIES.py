from _collections import deque


class Graph:

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function values for all nodes
    def h(self, n):
        H = {
            'A': 10,
            'B': 8,
            'C': 5,
            'D': 7,
            'E': 3,
            'F': 6,
            'G': 5,
            'H': 3,
            'I': 1,
            'J': 0

        }

        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = {start_node}
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None


adjacency_list = {
    'A': [('B', 6), ('F', 3)],
    'B': [('D', 2), ('C', 3)],
    'C': [('D', 1), ('E', 5)],
    'D': [('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('J', 3)],
    'J': []

}
graph1 = Graph(adjacency_list)
graph1.a_star_algorithm('A', 'J')


##########################################
##########################################

import math

class Node:
    def __init__ (self, state, parent, actions, heuristic, totalCost ):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost
        self.heuristic = heuristic
        
def findMin(frontier):
    minValue = math.inf
    node = ''
    for i in frontier:
        if minValue > frontier[i][1]:
            minValue = frontier[i][1]
            node = i
    return node

def actionSequence(graph, initialState, goalState):
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent != None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution

def Astar():
    initialState = 'A'
    goalState = 'Y'
    
    graph = {'A': Node('A', None, [('F',1)], (0,0), 0),
             'B': Node('B', None, [('G',1), ('C',1)], (2,0), 0),
             'C': Node('C', None, [('B',1), ('D',1)], (3,0), 0),
             'D': Node('D', None, [('C',1), ('E',1)], (4,0), 0),
             'E': Node('E', None, [('D',1)], (5,0), 0),
             'F': Node('F', None, [('A',1), ('H',1)], (0,1), 0),
             'G': Node('G', None, [('B',1), ('J',1)], (2,1), 0),
             'H': Node('H', None, [('F',1), ('I',1), ('M',1)], (0,2), 0),
             'I': Node('I', None, [('H',1), ('J',1), ('N',1)], (1,2), 0),
             'J': Node('J', None, [('G',1), ('I',1)], (2,2), 0),
             'K': Node('K', None, [('L',1), ('P',1)], (4,2), 0),
             'L': Node('L', None, [('K',1), ('Q',1)], (5,2), 0),
             'M': Node('M', None, [('H',1), ('N',1), ('R',1)], (0,3), 0),
             'N': Node('N', None, [('I',1), ('M',1), ('S',1)], (1,3), 0),
             'O': Node('O', None, [('P',1), ('U',1)], (3,3), 0),
             'P': Node('P', None, [('O',1), ('Q',1)], (4,3), 0),
             'Q': Node('Q', None, [('L',1), ('P',1), ('V',1)], (5,3), 0),
             'R': Node('R', None, [('M',1), ('S',1)], (0,4), 0),
             'S': Node('S', None, [('N',1), ('R',1), ('T',1)], (1,4), 0),
             'T': Node('T', None, [('S',1), ('U',1), ('W',1)], (2,4), 0),
             'U': Node('U', None, [('O',1), ('T',1)], (3,4), 0),
             'V': Node('V', None, [('Q',1), ('Y',1)], (5,4), 0),
             'W': Node('W', None, [('T',1)], (2,5), 0),
             'X': Node('X', None, [('Y',1)], (4,5), 0),
             'Y': Node('Y', None, [('V',1), ('X',1)], (5,5), 0)}
    
    
    frontier = dict()
    heuristicCost = math.sqrt(((graph[goalState].heuristic[0]- graph[initialState].heuristic[0])**2)\
                              +((graph[goalState].heuristic[1]-graph[initialState].heuristic[1])**2))
    
    frontier[initialState] = (None, heuristicCost)
    explored = dict()
    
    while len(frontier) != 0:
        currentNode = findMin(frontier)
        print(currentNode)
        del frontier[currentNode]
        if graph[currentNode].state == goalState:
            return actionSequence(graph, initialState, goalState)
        
        heuristicCost = math.sqrt(((graph[goalState].heuristic[0]-graph[currentNode].heuristic[0])**2)\
                                  +((graph[goalState].heuristic[1]-graph[currentNode].heuristic[1])**2))
        currentCost = graph[currentNode].totalCost
        explored[currentNode] = (graph[currentNode].parent, heuristicCost+currentCost)
        
        for child in graph[currentNode].actions:
            currentCost = child[1] + graph[currentNode].totalCost
            heuristicCost = math.sqrt(((graph[goalState].heuristic[0]-graph[child[0]].heuristic[0])**2)\
                                      +((graph[goalState].heuristic[1]-graph[child[0]].heuristic[1])**2))
            
            if child[0] in explored:
                if graph[child[0]].parent == currentNode or child[0]==initialState or explored[child[0]][1] <= currentCost + heuristicCost:
                    continue
            if child[0] not in frontier:
                graph[child[0]].parent = currentNode
                graph[child[0]].totalCost = currentCost
                frontier[child[0]] = (graph[child[0]].parent, currentCost + heuristicCost)
            else:
                if frontier[child[0]][1] < currentCost + heuristicCost:
                    graph[child[0]].parent = frontier[child[0]][0]
                    graph[child[0]].totalCost = frontier[child[0]][1] - heuristicCost
                else:
                    frontier[child[0]] = (currentNode, currentCost + heuristicCost)
                    graph[child[0]].parent = frontier[child[0]][0]
                    graph[child[0]].totalCost = currentCost
                    

sol = Astar()
print(sol)
