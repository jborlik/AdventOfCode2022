#import itertools
#import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field


with open('day01.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""".splitlines()]   # 


thedata = testdata
thedata = alldata



# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

if True:

    START = time.perf_counter()
    elves = []
    elves_count = []
    thiself = []
    thiscount = 0

    def addelf():
        global elves, elves_count, thiself, thiscount
        elves = elves + [thiself]
        elves_count = elves_count + [thiscount]
        thiself = []
        thiscount = 0

    for line in thedata:
        if line == "":
            addelf()
        else:
            val = int(line)
            thiself.append(val)
            thiscount += val
    else:
        addelf()
    
    mostcalories = max(elves_count)

    print(f"Most calories = {mostcalories}")



    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

ordered = sorted(elves_count, reverse=True)
topthree = ordered[0] + ordered[1] + ordered[2]
print(f"Sum of top three: {topthree}")



END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")

