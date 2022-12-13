#import itertools
#import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field
from typing import *


import astar
from astar import Location


with open('day12.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".splitlines()]   # 


thedata = testdata
thedata = alldata


class HeightGraph:

    def __init__(self, thedata) -> None:
        self.layout = thedata
        self.startpt = None
        self.endpt = None
        self.edges = {}

        for irow, arow in enumerate(thedata):
            for icol, achar in enumerate(arow):
                myedges = []
                if achar == 'S':
                    self.startpt = (irow,icol)
                    achar = 'a'
                if achar == 'E':
                    self.endpt = (irow,icol)
                    achar = 'z'

                checks = [(-1,0),(0,1),(1,0),(0,-1)]
                for acheck in checks:
                    anei = (irow+acheck[0],icol+acheck[1])
                    if anei[0]>=0 and (anei[0]<len(thedata)) and anei[1]>=0 and anei[1]<len(arow):
                        checkchar = thedata[anei[0]][anei[1]]
                        if checkchar == 'E':
                            checkchar = 'z'
                        if checkchar == 'S':
                            checkchar = 'a'
                        if ord(achar) + 1 >= ord(checkchar):
                            myedges.append(anei) 

                self.edges[(irow,icol)] = myedges
        pass

    def neighbors(self, id: Location) -> List[Location]:
        return self.edges[id]

    def cost(self, from_id: Location, to_id: Location) -> float:
        return 1.0


# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

if True:

    START = time.perf_counter()

    mygraph = HeightGraph(thedata)
    came_from, cost_so_far = astar.dijkstra_search(mygraph,start=mygraph.startpt,
                                                    goal=mygraph.endpt)
    thepath = astar.reconstruct_path(came_from, start=mygraph.startpt, goal=mygraph.endpt)
#    print(thepath)
    print(len(thepath)-1)

    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

mygraph = HeightGraph(thedata)

startpts = []
for irow, arow in enumerate(thedata):
    for icol, achar in enumerate(arow):
        if achar == 'a' or achar=='S':
            startpts.append((irow,icol))

costs = []
for startpt in startpts:
    try:
        came_from, cost_so_far = astar.dijkstra_search(mygraph,start=startpt,
                                                        goal=mygraph.endpt)
        thepath = astar.reconstruct_path(came_from, start=startpt, goal=mygraph.endpt)
        costs.append( (startpt,len(thepath)-1) )
    except:
        pass

costs = sorted(costs, key=lambda s: s[1], reverse=False)
print(costs)





END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")