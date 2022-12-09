#import itertools
#import numpy as np
import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
import math
import time
#import pprint
#from dataclasses import dataclass, field


with open('day09.txt') as datafile:
    alldata = [x.strip().split() for x in datafile.readlines()]

testdata = [x.strip().split() for x in """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines()]   # 


thedata = testdata
thedata = alldata

directions = {'U': (0,1), 'R': (1,0), 'D': (0,-1), 'L': (-1,0)}

sign = lambda a: 1 if a>0 else -1 if a<0 else 0
clamp = lambda n, minn, maxn: max(min(maxn, n), minn)
# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

def moveHead(dir):
    """Make one move in dir
        Returns the new headpos,tailpos"""
    newhead = ( headpos[0] + dir[0], headpos[1] + dir[1] )
    newtail = moveRelativeTo(newhead, tailpos)
    return newhead,newtail

def moveRelativeTo(newhead, oldknot):
    """Returns an updated position for the knot originally at oldknot, given a new position
        for its linked head"""
    difftotail = (newhead[0]-oldknot[0], newhead[1]-oldknot[1])
    dx = (0,0)
    if max(difftotail)==2 or min(difftotail)==-2:
        # we are going to move
        # first x
        dx_0 = sign(difftotail[0]) * clamp(abs(difftotail[0]), 0, 1)
        # then y
        dx_1 = sign(difftotail[1]) * clamp(abs(difftotail[1]), 0, 1)
        dx = (dx_0,dx_1)

    newtail = (oldknot[0] + dx[0], oldknot[1] + dx[1])
    return newtail



if True:

    START = time.perf_counter()

    headpos = (0,0)
    tailpos = (0,0)
    tailhistory = {tailpos: 1}
    
    for amove in thedata:
        
        for _ in range(int(amove[1])):
            headpos,tailpos = moveHead(directions[amove[0]])
            tailhistory[tailpos] = tailhistory.get(tailpos,0)
            #print(f"After Move {amove[0]}: {headpos},{tailpos}")

    uniquepositions = len(tailhistory)
    print(f"Unique tail positions = {uniquepositions}")




    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

rope = [ (0,0) for _ in range(10) ]
tailhistory = {rope[9]: 1}

def moveHeadForRope(dir):
    """Make one move in dir
        Returns the new headpos,tailpos"""
    
    newrope = copy.deepcopy(rope)
    newrope[0] = ( rope[0][0] + dir[0], rope[0][1] + dir[1] )

    for i in range(1,len(rope)):
        newrope[i] = moveRelativeTo(newrope[i-1], rope[i])
    
    return newrope

print(rope)
for amove in thedata:
    
    for _ in range(int(amove[1])):
        rope = moveHeadForRope(directions[amove[0]])
        tailhistory[rope[9]] = tailhistory.get(rope[9],0)
        print(f"After Move {amove[0]}: {rope}")

uniquepositions = len(tailhistory)
print(f"Unique tail positions = {uniquepositions}")


END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")