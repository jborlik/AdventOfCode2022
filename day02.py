#import itertools
#import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field


with open('day02.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """A Y
B X
C Z""".splitlines()]   # 


thedata = testdata
thedata = alldata



# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

rounds = [ x.split() for x in thedata ]

player1 = {'A': 1, 'B': 2, 'C': 3} # rock paper scissors
player2 = {'X': 1, 'Y': 2, 'Z': 3} # rock paper scissors

def scoreRound(p1, p2):
    winstatus = 0
    diff = player1[p1] - player2[p2]

    if (diff == -1) or (diff == 2):
        # player 2 wins
        winstatus = 6
        pass
    elif diff == 0:
        # draw
        winstatus = 3
        pass
    else:
        # player 1 wins
        winstatus = 0    
    return player2[p2] + winstatus


if True:

    START = time.perf_counter()

    total = 0
    for around in rounds:
        val = scoreRound(around[0], around[1])
        print(f"{around[0]} vs {around[1]} -> {val}")
        total += val
    print(f"Total:  {total}")


    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

losedrawwin = {'X': -1, 'Y': 0, 'Z': 1}

def pickChoice(p1, outcome):
    v = player1[p1] + losedrawwin[outcome]
    if v==0:
        v = 3
    elif v==4:
        v = 1
    return [i for i in player2 if player2[i]==v][0]

total = 0
for around in rounds:
    p2 = pickChoice(around[0], around[1])
    val = scoreRound(around[0], p2)
    print(f"{around[0]} vs {p2} (for {around[1]})-> {val}")
    total += val
print(f"Total part 2: {total}")




END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")