#import itertools
#import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field


with open('day10.txt') as datafile:
    alldata = [x.strip().split() for x in datafile.readlines()]

with open('day10_sample.txt') as datafile:
    testdata = [x.strip().split() for x in datafile.readlines()]

testdata2 = [x.strip().split() for x in """noop
addx 3
addx -5""".splitlines()]   # 


thedata = testdata
#thedata = testdata2
thedata = alldata



# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

if True:

    START = time.perf_counter()

    x = 1
    cycle = 1

    xhistory = [1]
    for aline in thedata:
        #print(aline)
        if aline[0] == "noop":
            cycle += 1
            xhistory.append(x)
        elif aline[0] == "addx":
            cycle += 2
            xhistory.append(x)
            x += int(aline[1])
            xhistory.append(x)
        #if cycle >= 200:
        #    break

    sumsignal = 0
    for icycle in [20,60,100,140,180,220]:
        thissignal = icycle * xhistory[-1]
        if icycle < len(xhistory):
            thissignal = icycle * xhistory[icycle-1]
            print(f"cycle {icycle}:  x={xhistory[icycle]}")
        else:
            print(f"cycle {icycle}:  at max x={xhistory[-1]} (len={len(xhistory)})")

        sumsignal += thissignal

    print(f"sum = {sumsignal}")
    print(xhistory)

    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

icycle = 0
for irow in range(6):
    for icol in range(40):
        icycle += 1
        #print(f'irow={irow} icol={icol} x={xhistory[icycle-1]}')
        spritepos = xhistory[icycle-1]
        if (spritepos - icol) in [-1,0,1]:
            print('#',end='')
        else:
            print('.', end='')
    print()



END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")