""" A weighted A* implementation, from https://www.redblobgames.com/pathfinding/a-star/implementation.html

Example:
    thedata = np.array([list(map(int,x.strip())) for x in \"\"\"116
    138
    213
    369
    746\"\"\".splitlines()],dtype=int)
    start, goal = (0,0),(thedata.shape[0]-1, thedata.shape[1]-1)
    grid = astar.GridWithWeights(width=thedata.shape[0], height=thedata.shape[1])
    grid.weights = thedata
    came_from, cost_so_far = astar.dijkstra_search(grid,start,goal)

    print(f"Cost so far: {cost_so_far[goal]}")
    
    path = astar.reconstruct_path(came_from, start=start, goal=goal)
    print(path)
"""

from typing import *
import collections
import heapq

import numpy as np  # for weighted graph weights

#--------------- Graphs

Location = TypeVar('Location')

class Graph(Protocol):
    def neighbors(self, id: Location) -> List[Location]: pass

class SimpleGraph:
    def __init__(self):
        self.edges: Dict[Location, List[Location]] = {}
    
    def neighbors(self, id: Location) -> List[Location]:
        return self.edges[id]

class WeightedGraph(Graph):
    def cost(self, from_id: Location, to_id: Location) -> float: pass


GridLocation = Tuple[int, int]

class SquareGrid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.walls: List[GridLocation] = []
    
    def in_bounds(self, id: GridLocation) -> bool:
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, id: GridLocation) -> bool:
        return id not in self.walls
    
    def neighbors(self, id: GridLocation) -> Iterator[GridLocation]:
        (x, y) = id
        neighbors = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)] # E W N S
        # see "Ugly paths" section for an explanation:
        if (x + y) % 2 == 0: neighbors.reverse() # S N W E
        results = filter(self.in_bounds, neighbors)
        results = filter(self.passable, results)
        return results

class GridWithWeights(SquareGrid):
    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        #self.weights: Dict[GridLocation, float] = {}
        self.weights: np.typing.ArrayLike = {}
    
    def cost(self, from_node: GridLocation, to_node: GridLocation) -> float:
        #return self.weights.get(to_node, 1)
        return self.weights[to_node[0],to_node[1]]


#--------------- Queue

T = TypeVar('T')

class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self) -> bool:
        return not self.elements
    
    def put(self, x: T):
        self.elements.append(x)
    
    def get(self) -> T:
        return self.elements.popleft()



class PriorityQueue:
    def __init__(self):
        self.elements: List[Tuple[float, T]] = []
    
    def empty(self) -> bool:
        return not self.elements
    
    def put(self, item: T, priority: float):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self) -> T:
        return heapq.heappop(self.elements)[1]

#----------------------------------------------------

def dijkstra_search(graph: WeightedGraph, start: Location, goal: Location):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from: Dict[Location, Optional[Location]] = {}
    cost_so_far: Dict[Location, float] = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current: Location = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far


def reconstruct_path(came_from: Dict[Location, Location],
                     start: Location, goal: Location) -> List[Location]:
    current: Location = goal
    path: List[Location] = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) # optional
    path.reverse() # optional
    return path

