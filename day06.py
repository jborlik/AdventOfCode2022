import itertools
#import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field


with open('day06.txt') as datafile:
    alldata = datafile.readline().strip()

testdata=[
'mjqjpqmgbljsphdztnvjfqwrcgsmlb',  # jpqm -> 7
'bvwbjplbgvbhsrlpgdmjqwftvncz', # 5
'nppdvjthqldpwncqszvftbrmjlhg', # 6
'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', # 10, 29
'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw' # 11, 26
]


thedata = testdata[4]
thedata = alldata

def findStart(amess, iNum) -> int:
    for ii in range(iNum,len(amess)):
        four = amess[ii-iNum:ii]
        counter = collections.Counter(four)
        duplicates = [k for k,v in counter.items() if v > 1]
        if len(duplicates)==0:
            return ii
    else:
        print("NOT FOUND!")


# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

if True:

    START = time.perf_counter()

    istart = findStart(thedata, 4)
    print(f"Found unique four at: {istart}")

    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

istart = findStart(thedata, 14)
print(f"Found unique four at: {istart}")



END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")