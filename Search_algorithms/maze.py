from PyMaze import *
from BFS import BFS

m=maze()
m.CreateMaze(saveMaze=False,loopPercent=100)
a=agent(m,10,10)
b=agent(m)
path2=BFS(m)
m.tracePath({a:m.path})
m.tracePath({b:path2})
textLabel(m,"Total BFS:",len(path2)+1)
textLabel(m,"Total 3ada:",len(m.path)+1)
m.run()