from PyMaze import *
from queue import PriorityQueue

def heuristicCost(cell1, cell2):
    # manhattan distance
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)


def gbfs(inputMaze, startCell, goalCell):
    h_score = {cell: float("inf") for cell in m.grid}
    h_score[startCell] = heuristicCost(startCell, goalCell)

    cellPriorityQueue = PriorityQueue()
    cellPriorityQueue.put((heuristicCost(startCell, goalCell), startCell))
    pathWithReservedArrows = {}
    searchPath = [startCell]
    while not cellPriorityQueue.empty():
        currCell = cellPriorityQueue.get()[1]
        searchPath.append(currCell)
        if currCell == goalCell:
            break
        for direction in 'ESNW':
            if m.maze_map[currCell][direction] == True:
                if direction == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif direction == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                elif direction == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif direction == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                tempHScore = heuristicCost(childCell, goalCell)

                if tempHScore < h_score[childCell]:
                    h_score[childCell] = tempHScore
                    cellPriorityQueue.put((tempHScore, childCell))
                    pathWithReservedArrows[childCell] = currCell

    path = {}
    cell = goalCell
    while cell != startCell:
        path[pathWithReservedArrows[cell]] = cell
        cell = pathWithReservedArrows[cell]
    return searchPath, path




m=maze()
m.CreateMaze(loadMaze='maze--2022-04-25--16-30-10.csv')
search,path=gbfs(m,(8,8),(1,1))
a=agent(m,footprints=True)
b=agent(m,footprints=True,color="red")
m.tracePath({a:path})
m.tracePath({b:search})
l1=textLabel(m,'GBFS Path Length',len(path)+1)
l=textLabel(m,'GBFS Search Length',len(search))
m.run()