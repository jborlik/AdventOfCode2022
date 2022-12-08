#import itertools
#import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field


with open('day08.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """30373
25512
65332
33549
35390""".splitlines()]   # 


thedata = testdata
thedata = alldata

width = len(thedata[0])
height = len(thedata)

# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

def treeVisible(ix,iy): # -> bool,bool,bool,bool:
    v = thedata[iy][ix]
    isvisible = [False,False,False,False] # north east south west
    # check north
    for i in range(0,iy):
        if thedata[i][ix] >= v:
            break
    else:
        isvisible[0] = True
    # check east
    for i in range(ix+1,width):
        if thedata[iy][i] >= v:
            break
    else:
        isvisible[1] = True
    # check south
    for i in range(iy+1,height):
        if thedata[i][ix] >= v:
            break
    else:
        isvisible[2] = True
    # check west
    for i in range(0,ix):
        if thedata[iy][i] >= v:
            break
    else:
        isvisible[3] = True
    
    return isvisible

if True:

    START = time.perf_counter()

    countvisible = width*2 + (height-2)*2
    print(f"Visible on exterior = {countvisible}")
    for iy in range(1,height-1):
        for ix in range(1,width-1):
            isvisible = treeVisible(ix,iy)
            if sum(isvisible) > 0:
                #print(f'{ix},{iy} ({thedata[iy][ix]}) = {sum(isvisible)}')
                countvisible += 1

    print(f"count of visible = {countvisible}")

    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

def calcViewScore(ix,iy):
    # checking:  north,         east,                   south,              west
    ranges = [ (True,iy-1,-1,-1), (False,ix+1,width,1), (True,iy+1,height,1),  (False,ix-1,-1,-1)]
    v = thedata[iy][ix]
    fullscore = 1
    for adir in ranges:
        dirscore = 0
        for i in range( adir[1], adir[2], adir[3]):
            t = thedata[i][ix]
            if not adir[0]:
                t = thedata[iy][i]
            dirscore += 1
            if t >= v:
                break
        fullscore *= dirscore
    return fullscore



START = time.perf_counter()

maxscore = 0
maxloc = None
for iy in range(1,height-1):
    for ix in range(1,width-1):
        thescore = calcViewScore(ix,iy)
        print(f"({ix},{iy}) viewscore is {thescore}")
        if thescore > maxscore:
            maxscore = thescore
            maxloc = (ix,iy)

print(f"Max viewscore is {maxscore} at ({ix},{iy})")

END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")