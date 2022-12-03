#import itertools
#import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
from collections import Counter
#import math
import time
#import pprint
#from dataclasses import dataclass, field


with open('day03.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines()]   # 


thedata = testdata
thedata = alldata



# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

def findCommon(asack):
    ilen = int(len(asack)/2)
    set1 = set(asack[0:ilen])
    set2 = set(asack[ilen:])
    common = set1.intersection(set2)
    return list(common)[0]

def findPriority(achar):
    val = ord(achar) - ord('a') + 1
    if val < 0:
        val = ord(achar) - ord('A') + 27
    return val




if True:

    START = time.perf_counter()

    thesum = 0

    for asack in thedata:
        common = findCommon(asack)
        priority = findPriority(common)
        print(f"{asack}: {common} -> {priority}")
        thesum += priority

    print(f"total: {thesum}")

    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

thesum = 0
for istart in range(0,len(thedata),3):
    common = set(thedata[istart]) & set(thedata[istart+1]) & set(thedata[istart+2])
    common = list(common)[0]
    priority = findPriority(common)
    print(f"{istart} -> {common} -> {priority}")
    thesum += priority

print(f"total: {thesum}")




END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")