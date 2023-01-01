#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self,state,parent,actions,totalCost):
        self.state=state
        self.parent=parent
        self.actions=actions

        self.totalCost=totalCost


def DFS():
    initialState='Arad'
    goalState='Bucharest'
    graph = {
         'Arad':Node ('Arad',None['Sibiu','Timisoara','Zerind'],[140,118,75]),
         'Sibiu':Node ('Sibiu',None['Arad','Oradea','Fagaras','Rimnicu'],[140,151,99,80]),
         'Timisoara':Node ('Timisoara',None['Arad','Lugoj'],[118,111]),
         'Zerind':Node ('Zerind',None['Arad','Oradea'],[75,71]),
         'Oradea':Node ('Oradea',None['Zerind','Sibiu'],[71,151]),
         'Fagaras':Node ('Fagaras',None['Sibiu','Bucharest'],[99,211]),
         'Rimnicu':Node ('Rimnicu',None['Sibiu','Craivo','Pitesti'],[80,146,97]),
         'Lugoj':Node ('Lugoj',None['Timisoara','Mehadia'],[111,70]),
         'Bucharest':Node ('Bucharest',None['Giurgiu','Urziceni','Pitesti','Fagaras'],[90,85,101,211]),
         'Craivo':Node ('Craivo',None['Dobreta','Pitesti','Rimnicu'],[120,138,146]),
         'Pitesti':Node ('Pitesti',None['Rimnicu','Craivo','Bucharest'],[97,138,101]),
         'Mehadia':Node  ('Mehadia',None['Dobreta','Lugoj'],[75,70]),
         'Giurgiu':Node ('Giurgiu',None['Bucharest'],[90]),
         'Urziceni':Node ('Urziceni',None['Bucharest','Hirsova','Vaslui'],[85,98,142]), 
         'Dobreta':Node ('Dobreta',None['Mehadia','Craivo'],[75,120]),
         'Hirsova' :Node ('Hirsova',None['Eforie','Urziceni'],[86,98]),
         'Vaslui' :Node ('Vaslui',None['Urziceni','Lasi'],[142,92]),
         'Eforie' :Node  ('Eforie',None['Hirsova'],[86]), 
         'Lasi':Node ('Lasi',None['Neamt','Vaslui'],[87,92]),
         'Neamt':Node ('Neamt',None['Lasi'],[87])
}
    frontier=[initialState]
    explored=[]
    while len(frontier)!=0:
        currentNode=frontier.pop(len(frontier)-1)
        print(currentNode)
        explored.append(currentNode)
        currentChildren=0
        for child in graph[currentNode].actions:
            if child not in frontier and child not  in explored:
                graph[child].parent=currentNode
                if graph[child].state==goalState:
                    print(explored)
                    return  actionSequence(graph,initialState,goalState)
                currentChildren=currentChildren+1
                frontier.append(child)
        if currentChildren==0:
            del  explored[len(explored)-1]


def actionSequence(graph, initialState,goalState):
    solution=[goalState]
    currentParent=graph[goalState].parent
    while currentParent!=None:
        solution.append(currentParent)
        currentParent=graph[currentParent].parent
    solution.reverse()
    return  solution
solution=DFS()
print(solution)


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

    words = ['NOTE', 'SAND', 'STONE']

    validWords = searchInBoggle(board, words)
    print(validWords)


# In[10]:


class Node:
    def __init__(self,state,parent,actions,totalCost):
        self.state=state
        self.parent=parent
        self.actions=actions

        self.totalCost=totalCost

graph={'A': Node('A', None,['B','E','C'], None),
       'B': Node('B', None, ['D','E','A'],None),
       'C': Node('C', None,['A','F','G'],None),
       'D': Node('D',None,['B','E'],None),
       'E': Node('E',None,['A','B','D'],None),
       'F': Node('F',None,['C'],None),
       'G': Node('G',None,['C'],None)
}

def DFS():
    initialState='A'
    goalState='D'
    graph = {'A': Node('A', None, ['B', 'E', 'C'], None),
             'B': Node('B', None, ['D', 'E', 'A'], None),
             'C': Node('C', None, ['A', 'F', 'G'], None),
             'D': Node('D', None, ['B', 'E'], None),
             'E': Node('E', None, ['A', 'B', 'D'], None),
             'F': Node('F', None, ['C'], None),
             'G': Node('G', None, ['C'], None)
             }
    frontier=[initialState]
    explored=[]
    while len(frontier)!=0:
        currentNode=frontier.pop(len(frontier)-1)
        print(currentNode)
        explored.append(currentNode)
        currentChildren=0
        for child in graph[currentNode].actions:
            if child not in frontier and child not  in explored:
                graph[child].parent=currentNode
                if graph[child].state==goalState:
                    print(explored)
                    return  actionSequence(graph,initialState,goalState)
                currentChildren=currentChildren+1
                frontier.append(child)
        if currentChildren==0:
            del  explored[len(explored)-1]


def actionSequence(graph, initialState,goalState):
    solution=[goalState]
    currentParent=graph[goalState].parent
    while currentParent!=None:
        solution.append(currentParent)
        currentParent=graph[currentParent].parent
    solution.reverse()
    return  solution
solution=DFS()
print(solution)


# In[ ]:




