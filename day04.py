#import itertools
#import numpy as np
#import copy
import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field


with open('day04.txt') as datafile:
    alldata = [list(map(int,re.split('\W+',x.strip()))) for x in datafile.readlines()]

testdata = [list(map(int,re.split('\W+',x.strip()))) for x in """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()]   # 


thedata = testdata

thedata = alldata


# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

def rangeContained(a0,a1,b0,b1):
    a = set(range(a0,a1+1))
    b = set(range(b0,b1+1))
    #common = a.intersection(b)
    if a.issubset(b):
        return True
    if b.issubset(a):
        return True
    return False

def rangeOverlap(a0,a1,b0,b1):
    a = set(range(a0,a1+1))
    b = set(range(b0,b1+1))
    common = a.intersection(b)    
    if len(common) == 0:
        return False # no overlap
    return True

if True:

    START = time.perf_counter()
    numcontained = 0
    
    for apair in thedata:
        if rangeContained(*apair):
            numcontained += 1
    
    print(f"Num contained={numcontained}")

    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

numoverlap = 0

for apair in thedata:
    if rangeOverlap(*apair):
        numoverlap += 1

print(f"Num numoverlap={numoverlap}")


END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")