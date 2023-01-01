import math


class Node:
    def __init__(self, state, parent, actions, totalCost, heuristic ):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost
        self.heuristic = heuristic

def hillClimbing():

    graph = {'A' : Node('A', None,[('F',1)],0,(0,0)),
        'B' : Node('B', None,[('C',1),('G',1)],0,(2,0)),
        'C' : Node('C', None,[('B',1),('D',1)],0,(3,0)),
        'D' : Node('D', None,[('C',1),('E',1)],0,(4,0)),
        'E' : Node('E', None,[('D',1)],0,(5,0)),
        'F' : Node('F', None,[('A',1),('H',1)],0,(0,1)),
        'G' : Node('A', None,[('B',1),('J',1)],0,(2,1)),
        'H' : Node('H', None,[('F',1),('I',1),('M',1)],0,(0,2)),
        'I' : Node('I', None,[('H',1),('J',1),('N',1)],0,(1,2)),
        'J' : Node('J', None,[('G',1),('I',1)],0,(2,2)),
        'K' : Node('K', None,[('L',1),('P',1)],0,(4,2)),
        'L' : Node('L', None,[('K',1),('Q',1)],0,(5,2)),
        'M' : Node('M', None,[('H',1),('N',1),('R',1)],0,(0,3)),
        'N' : Node('N', None,[('I',1),('M',1),('S',1)],0,(1,3)),
        'O' : Node('O', None,[('P',1),('U',1)],0,(3,3)),
        'P' : Node('P', None,[('K',1),('O',1),('Q',1)],0,(4,3)),
        'Q' : Node('Q', None,[('L',1),('P',1),('V',1)],0,(5,3)),
        'R' : Node('R', None,[('M',1),('S',1)],0,(0,4)),
        'S' : Node('S', None,[('N',1),('R',1),('T',1)],0,(1,4)),
        'T' : Node('T', None,[('S',1),('W',1),('U',1)],0,(2,4)),
        'U' : Node('U', None,[('O',1),('T',1)],0,(3,4)),
        'V' : Node('V', None,[('Q',1),('Y',1)],0,(5,4)),
        'W' : Node('W', None,[('T',1)],0,(2,5)),
        'X' : Node('X', None,[('Y',1)],0,(4,5)),
        'Y' : Node('Y', None,[('X',1),('Y',1)],0,(5,5))}
        

        

        
    initialState = 'A'
    goalState ='Y'
    parentNode=initialState
    parentCost=math.sqrt((graph[goalState].heuristic[0] - graph[initialState].heuristic[0])**2+(graph[goalState].heuristic[1] - graph[initialState].heuristic[1])**2)
    explored=[]
    solution=[]
    minChildCost = parentCost - 1
    while parentNode!=goalState:
      bestNode=parentNode
      minChildCost=parentCost
      explored.append(parentNode)
      for child in graph[parentNode].actions:
        if child[0] not in explored:
            childCost= math.sqrt((graph[goalState].heuristic[0] \
                     - graph[child[0]].heuristic[0])**2\
                    +(graph[goalState].heuristic[1] \
                     - graph[child[0] ].heuristic[1])**2)
            if childCost<minChildCost:
                bestNode=child[0]
                minChildCost=childCost
      if bestNode==parentNode:
        break
      else:
              parentNode=bestNode
              parentCost=minChildCost
              solution.append(parentNode)
    return solution

solution = hillClimbing()
print(solution)

####################Task####################
############Using Reg No####################

import math
class Node:
    def __init__(self,state,parent,actions,totalCost,heuristic):
        self.state=state
        self.parent=parent
        self.actions = actions
        self.totalCost=totalCost
        self.heuristic=heuristic

def hillClimbing():
    graphNode = {'A': Node('A', None, [('G', 1)], 0, (8,9)),
             'B': Node('B', None, [('J', 1), ('C', 1)], 0, (8,13)),
             'C': Node('C', None, [('B', 1), ('K', 1), ('D', 1)], 0, (8,14)),
             'D': Node('D', None, [('C', 1), ('L', 1)], 0, (8,15)),
             'E': Node('E', None, [('N', 1)], 0, (8,17)),
             'F': Node('F', None, [('O', 1), ('G', 1)], 0, (9,8)),
             'G': Node('G', None, [('F', 1), ('A', 1), ('H', 1)], 0, (9,9)),
             'H': Node('H', None, [('G', 1)], 0, (9,10)),
             'I': Node('I', None, [('P', 1), ('J', 1)], 0, (9,12)),
             'J': Node('J', None, [('I', 1), ('B', 1), ('K', 1), ('Q',1)], 0, (9,13)),
             'K': Node('K', None, [('J', 1), ('C', 1), ('L', 1), ('R',1)], 0, (9,14)),
             'L': Node('L', None, [('K', 1), ('D', 1), ('M', 1), ('S',1)], 0, (9,15)),
             'M': Node('M', None, [('L', 1), ('N', 1), ('T', 1)], 0, (9,16)),
             'N': Node('N', None, [('E', 1), ('M', 1), ('U', 1)], 0, (9,17)),
             'O': Node('O', None, [('F', 1)], 0, (10,8)),
             'P': Node('P', None, [('I', 1), ('Q', 1)], 0, (10,12)),
             'Q': Node('Q', None, [('P', 1), ('J', 1), ('R', 1)], 0, (10,13)),
             'R': Node('R', None, [('Q', 1), ('K', 1), ('S', 1), ('X', 1)], 0, (10,14)),
             'S': Node('S', None, [('R', 1), ('L', 1), ('T', 1), ('Y', 1)], 0, (10,15)),
             'T': Node('T', None, [('S', 1), ('M', 1), ('U', 1), ('Z', 1)], 0, (10,16)),
             'U': Node('U', None, [('T', 1), ('N', 1), ('AA', 1),], 0, (10,17)),
             'V': Node('V', None, [('W', 1)], 0, (11,9)),
             'W': Node('W', None, [('V', 1), ('AC', 1)], 0, (11,10)),
             'X': Node('X', None, [('R', 1), ('Y', 1)], 0, (11,14)),
             'Y': Node('Y', None, [('X', 1), ('S', 1), ('Z', 1), ('AE', 1)], 0, (11,15)),
             'Z': Node('Z', None, [('Y', 1), ('T', 1), ('AA', 1)], 0, (11,16)),
             'AA': Node('AA', None, [('Z', 1), ('U', 1)], 0, (11,17)),
             'AB': Node('AB', None, [('AF', 1)], 0, (12,8)),
             'AC': Node('AC', None, [('W', 1), ('AD', 1)], 0, (12,10)),
             'AD': Node('AD', None, [('AC', 1), ('AG', 1)], 0, (12,11)),
             'AE': Node('AE', None, [('Y', 1), ('AK', 1)], 0, (12,15)),
             'AF': Node('AF', None, [('AB', 1), ('AN', 1)], 0, (13,8)),
             'AG': Node('AG', None, [('AD', 1), ('AH', 1), ('AP', 1)], 0, (13,11)),
             'AH': Node('AH', None, [('AG', 1), ('AI', 1)], 0, (13,12)),
             'AI': Node('AI', None, [('AH', 1), ('AJ', 1), ('AQ', 1)], 0, (13,13)),
             'AJ': Node('AJ', None, [('AI', 1), ('AK', 1), ('AR',1)], 0, (13,14)),
             'AK': Node('AK', None, [('AE', 1), ('AJ', 1), ('AL', 1), ('AS', 1)], 0, (13,15)),
             'AL': Node('AL', None, [('AK', 1), ('AM', 1)], 0, (13,16)),
             'AM': Node('AM', None, [('AL', 1)], 0, (13,17)),
             'AN': Node('AN', None, [('AF', 1), ('AU', 1)], 0, (14,8)),
             'AP': Node('AP', None, [('AW', 1), ('AQ', 1)], 0, (14,10)),
             'AQ': Node('AQ', None, [('AP', 1), ('AG', 1)], 0, (14,11)),
             'AR': Node('AR', None, [('AI', 1), ('AY', 1), ('AS', 1)], 0, (14,13)),
             'AS': Node('AS', None, [('AR', 1), ('AT', 1), ('AJ', 1)], 0, (14,14)),
             'AT': Node('AT', None, [('AS', 1), ('AK', 1)], 0, (14,15)),
             'AU': Node('AU', None, [('AN', 1), ('BA', 1), ('AV', 1)], 0, (15,8)),
             'AV': Node('AV', None, [('AU', 1), ('AW', 1), ('BB', 1)], 0, (15,9)),
             'AW': Node('AW', None, [('AP', 1), ('AV', 1)], 0, (15,10)),
             'AX': Node('AX', None, [('BD', 1), ('AY', 1)], 0, (15,12)),
             'AY': Node('AY', None, [('AX', 1), ('BE', 1), ('AR', 1)], 0, (15,13)),
             'AZ': Node('AZ', None, [('BF', 1)], 0, (15,16)),
             'BA': Node('BA', None, [('AU', 1), ('BH', 1), ('BB', 1)], 0, (16,8)),
             'BB': Node('BB', None, [('AV', 1), ('BA', 1), ('BI', 1)], 0, (16,9)),
             'BC': Node('BC', None, [('BK', 1), ('BD', 1)], 0, (16,11)),
             'BD': Node('BD', None, [('BC', 1), ('AX', 1), ('BE', 1)], 0, (16,12)),
             'BE': Node('BE', None, [('BD', 1), ('AY', 1), ('BL', 1)], 0, (16,13)),
             'BF': Node('BF', None, [('BO', 1), ('AZ', 1), ('BG', 1)], 0, (16,16)),
             'BG': Node('BG', None, [('BF', 1), ('BW', 1)], 0, (16,17)),
             'BH': Node('BH', None, [('BA', 1), ('BI', 1)], 0, (17,8)),
             'BI': Node('BI', None, [('BH', 1), ('BB', 1), ('BJ', 1)], 0, (17,9)),
             'BJ': Node('BJ', None, [('BI', 1), ('BK', 1)], 0, (17,10)),
             'BK': Node('BK', None, [('BJ', 1), ('BC', 1)], 0, (17,11)),
             'BL': Node('BL', None, [('BE', 1), ('BM', 1)], 0, (17,13)),
             'BM': Node('BM', None, [('BL', 1), ('BN', 1)], 0, (17,14)),
             'BN': Node('BN', None, [('BM', 1), ('BO', 1)], 0, (17,15)),
             'BO': Node('BO', None, [('BN', 1), ('BF', 1), ('BW', 1)], 0, (17,16)),
             'BP': Node('BP', None, [('BO', 1), ('BG', 1)], 0, (17,17))}

    initialState='E'
    goalState='BH'
    parentNode = initialState
    parentCost = math.sqrt((graphNode[goalState].heuristic[0] - \
                            graphNode[initialState].heuristic[0]) ** 2 + \
                           (graphNode[goalState].heuristic[1] - \
                            graphNode[initialState].heuristic[1]) ** 2)
    explored = []
    solution = []
    minChildCost = parentCost - 1

    while parentNode != goalState:
        bestNode = parentNode
        minChildCost = parentCost
        explored.append(parentNode)

        for child in graphNode[parentNode].actions:
            if child[0] not in explored:
                childCost = math.sqrt((graphNode[goalState].heuristic[0] \
                                       - graphNode[child[0]].heuristic[0]) ** 2 \
                                      + (graphNode[goalState].heuristic[1] \
                                         - graphNode[child[0]].heuristic[1]) ** 2)
                if childCost < minChildCost:
                    bestNode = child[0]
                    minChildCost = childCost
        if bestNode == parentNode:
            break
        else:
            parentNode = bestNode
            parentCost = minChildCost
            solution.append(parentNode)
    return solution


sol = hillClimbing()
print(sol)
