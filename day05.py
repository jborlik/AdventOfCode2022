#import itertools
#import numpy as np
import copy
import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field


with open('day05.txt') as datafile:
    alldata = [x for x in datafile.readlines()]  # leave the ending whitespace

testdata = [x for x in """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".splitlines()]   # 


thedata = testdata
thedata = alldata

# ----------------
# processing input
#-----------------
def readInitialState(thedata):
    numstacks = int((len(thedata[0])+1)/4)
    maxheight = 0
    for ibreak,aline in enumerate(thedata):
        if aline.strip() == '':
            maxheight = ibreak - 1
            break
    
    print(f"numstacks={numstacks}, maxheight={maxheight}")

    stacks = [ [] for _ in range(0,numstacks) ]
    for aline in thedata[0:maxheight]:
        for iq, c in enumerate(aline[1::4]):
            if c != ' ':
                stacks[iq].insert(0,c)
    
    return stacks, ibreak


stacks, ibreak = readInitialState(thedata)

print(stacks)

def readInstructions(thelines):
    instructions = [  list(map(int,x.split()[1::2])) for x in thelines ]
    return instructions


instructions = readInstructions(thedata[ibreak+1:])

basestacks = copy.deepcopy(stacks)

# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

def moveOneFromStack(ifrom, ito):
    global stacks
    aval = stacks[ifrom].pop()
    stacks[ito].append(aval)

if True:

    START = time.perf_counter()

    for ins in instructions:

        for _ in range(0,ins[0]):
            moveOneFromStack(ins[1]-1, ins[2]-1)


    # okay, now stacks are in final state
    for astack in stacks:
        print(astack[-1], end='')
    print("")




    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

stacks = copy.deepcopy(basestacks)

for ins in instructions:
    ifrom = ins[1]-1
    ito = ins[2]-1
    inum = ins[0]
    movelist = stacks[ifrom][len(stacks[ifrom])-inum:]
    stacks[ito].extend(movelist)
    stacks[ifrom] = stacks[ifrom][0:-inum]

# okay, now stacks are in final state
for astack in stacks:
    print(astack[-1], end='')
print("")



END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")