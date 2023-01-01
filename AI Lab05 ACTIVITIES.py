#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Python program to print DFS traversal from a given
# given graph
from collections import defaultdict

# This class represents a directed graph using adjacency
# list representation
class Graph:

    def __init__(self,vertices):

        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # A function to perform a Depth-Limited search
    # from given source 'src'
    def DLS(self,src,target,maxDepth):

        if src == target : return True

        # If reached the maximum depth, stop recursing.
        if maxDepth <= 0 : return False

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[src]:
                if(self.DLS(i,target,maxDepth-1)):
                    return True
        return False

    # IDDFS to search if target is reachable from v.
    # It uses recursive DLS()
    def IDDFS(self,src, target, maxDepth):

        # Repeatedly depth-limit search till the
        # maximum depth
        for i in range(maxDepth):
            if (self.DLS(src, target, i)):
                return True
        return False

# Create a graph given in the above diagram
g = Graph (7);
g.addEdge('Arad', 'Sibiu')
g.addEdge('Arad', 'Timisoara')
g.addEdge('Arad', 'Zerind')
g.addEdge('Sibiu', 'Arad')
g.addEdge('Sibiu', 'Fagaras')
g.addEdge('Sibiu', 'Oradea')
g.addEdge('Sibiu', 'Rimnicu Vilcea')
g.addEdge('Fagaras', 'Sibiu')
g.addEdge('Fagaras', 'Bucharest')
g.addEdge('Rimnicu Vilcea', 'Craiova')
g.addEdge('Rimnicu Vilcea', 'Pitesti')
g.addEdge('Rimnicu Vilcea', 'Sibiu')
g.addEdge('Pitesti', 'Bucharest')
g.addEdge('Pitesti', 'Craiova')
g.addEdge('Pitesti', 'Rimnicu Vilcea')

target = 'Bucharest'; maxDepth = 4; src = 'Arad'

if g.IDDFS(src, target, maxDepth) == True:
    print ("Target is reachable from source " +
        "within max depth")
else :
    print ("Target is NOT reachable from source " +
        "within max depth")



# In[8]:



row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]



def isSafe(x, y, processed):
    return (0 <= x < len(processed)) and (0 <= y < len(processed[0]))            and not processed[x][y]



def searchBoggle(board, words, result, processed, i, j, path=''):

    processed[i][j] = True


    path += board[i][j]


    if path in words:
        result.add(path)


    for k in range(len(row)):

        if isSafe(i + row[k], j + col[k], processed):
            searchBoggle(board, words, result, processed, i + row[k], j + col[k], path)

    processed[i][j] = False


def searchInBoggle(board, words):

    result = set()


    if not board or not len(board):
        return


    (M, N) = (len(board), len(board[0]))


    processed = [[False for x in range(N)] for y in range(M)]


    for i in range(M):
        for j in range(N):

            searchBoggle(board, words, result, processed, i, j)

    return result


if __name__ == '__main__':
    board = [
        ['M', 'S', 'E', 'F'],
        ['R', 'A', 'T', 'D'],
        ['L', 'O', 'N', 'E'],
        ['k', 'A', 'F', 'B']
    ]

    words = ['START','NOTE', 'SAND', 'STONED']

    validWords = searchInBoggle(board, words)
    print(validWords)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




