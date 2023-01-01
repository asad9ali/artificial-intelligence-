#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

class Maze:
    def __init__(self,mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazeFile = open(mazeFileName,'r')
        rowsInMaze = 0
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze/2
        self.yTranslate = rowsInMaze/2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-(columnsInMaze-1)/2-.5,-(rowsInMaze-1)/2-.5,(columnsInMaze-1)/2+.5,(rowsInMaze-1)/2+.5)

    def drawMaze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x] == OBSTACLE:
                    self.drawCenteredBox(x+self.xTranslate,-y+self.yTranslate,'orange')
        self.t.color('black')
        self.t.fillcolor('blue')
        self.wn.update()
        self.wn.tracer(1)

    def drawCenteredBox(self,x,y,color):
        self.t.up()
        self.t.goto(x-.5,y-.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def moveTurtle(self,x,y):
        self.t.up()
        self.t.setheading(self.t.towards(x+self.xTranslate,-y+self.yTranslate))
        self.t.goto(x+self.xTranslate,-y+self.yTranslate)

    def dropBreadcrumb(self,color):
        self.t.dot(10,color)

    def updatePosition(self,row,col,val=None):
        if val:
            self.mazelist[row][col] = val
        self.moveTurtle(col,row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.dropBreadcrumb(color)

    def isExit(self,row,col):
        return (row == 0 or
                row == self.rowsInMaze-1 or
                col == 0 or
                col == self.columnsInMaze-1 )

    def __getitem__(self,idx):
        return self.mazelist[idx]


def searchFrom(maze, startRow, startColumn):
   


    maze.updatePosition(startRow, startColumn)
    if maze[startRow][startColumn] == OBSTACLE :
        return False

    
    if maze[startRow][startColumn] == TRIED or maze[startRow][startColumn] == DEAD_END:
        return False

    
    if maze.isExit(startRow,startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startColumn, TRIED)
    
    
    found = searchFrom(maze, startRow-1, startColumn) or             searchFrom(maze, startRow+1, startColumn) or             searchFrom(maze, startRow, startColumn-1) or             searchFrom(maze, startRow, startColumn+1)
    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found


myMaze = Maze('textfile.txt')
myMaze.drawMaze()
myMaze.updatePosition(myMaze.startRow,myMaze.startCol)

searchFrom(myMaze, myMaze.startRow, myMaze.startCol)


# In[1]:


d = {
         'Arad': [('Sibiu', 140), ('Timisoara', 118), ('Zerind', 75)],
         'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu', 80)],
         'Timisoara': [('Arad', 118), ('Lugoj', 111)],
         'Zerind': [('Arad', 75), ('Oradea', 71)],
         'Oradea': [('Zerind', 71), ('Sibiu', 151)],
         'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
         'Rimnicu': [('Sibiu', 80), ('Craivo', 146), ('Pitesti', 97)],
         'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
         'Bucharest': [('Giurgiu', 90), ('Urziceni', 85), ('Pitesti', 101), ('Fagaras', 211)],
         'Craivo': [('Dobreta', 120), ('Pitesti', 138), ('Rimnicu', 146)],
         'Pitesti': [('Rimnicu', 97), ('Craivo', 138), ('Bucharest', 101)],
         'Mehadia': [('Dobreta', 75), ('Lugoj', 70)],
         'Giurgiu': [('Bucharest', 90)],
         'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
         'Dobreta': [('Mehadia', 75), ('Craivo', 120)],
         'Hirsova' : [('Eforie', 86), ('Urziceni', 98)],
         'Vaslui' : [('Urziceni', 142), ('Lasi', 92)],
         'Eforie' : [('Hirsova', 86)],
         'Lasi': [('Neamt', 87), ('Vaslui', 92)],
         'Neamt': [('Lasi', 87)],
}

total_nodes = list(d.keys())

total_nodes

h_n_ = {
         'Arad': 366,
         'Sibiu':  253,
         'Timisoara': 329,
         'Zerind': 374,
         'Oradea': 380,
         'Fagaras': 178,
         'Rimnicu': 193,
         'Lugoj': 244,
         'Bucharest': 0,
         'Craivo': 160,
         'Pitesti': 98,
         'Mehadia': 241,
         'Giurgiu': 77,
         'Urziceni': 80,
         'Dobreta': 242,
         'Hirsova' : 151,
         'Vaslui' : 199,
         'Eforie' : 161,
         'Lasi': 226,
         'Neamt': 234
}



def my(x):
    return x[1]

def build_dcit(lis):
    di  = {}

    for i in lis:
        name = i[0]
        cost = i[1]
        di[name] = cost
    return di

def GBFS(start,goal):
    
    q = []
    start_val = h_n_.get(start)
    q.append((start,start_val))
    explored = []
    expanded = []
    
    while len(q)>0:


        node = q.pop(0)

        if node[0] not in explored:
            explored.append(node[0])
        
        if node[0] == goal:
            print('Result :',explored,expanded,len(expanded))
            return

        child = d.get(node[0])
 
        for i in child:
            n_key = i[0]
            n_val = (h_n_.get(n_key))+i[1]
            n_tuple = n_key,n_val

            if i[0] not in explored and i[0] not in build_dcit(q):
                q.append(n_tuple)
        expanded.append(node[0])
            
        q = sorted(q,key= my)
    return explored,expanded,len(expanded)
        
    
GBFS('Arad','Bucharest')


# In[ ]:




