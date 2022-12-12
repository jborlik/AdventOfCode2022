#import itertools
#import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field

worrydivisor = 1  # for part 2
isPartTwo = False

class Monkey():
    def __init__(self, items, op_add=0.0, op_multi=1.0, op_squareit=False, divisibleby=1.0, truemonkey=0, falsemonkey=0) -> None:
        self.items = items
        self.op_adder = op_add
        self.op_multi = op_multi
        self.op_squareit = op_squareit
        self.test_divisibleby = divisibleby
        self.test_truemonkey = truemonkey
        self.test_falsemonkey = falsemonkey
        self.inspectcount = 0

    def __str__(self) -> str:
        return f"holding: {self.items}"

    def inspectItems(self):
        retlist = []
        for item in self.items:
            self.inspectcount += 1

            worrylevel = item
            worrylevel += self.op_adder
            worrylevel *= self.op_multi
            if self.op_squareit:
                worrylevel *= worrylevel

            if isPartTwo:
                boredlevel = int(worrylevel % worrydivisor)
            else:
                boredlevel = int(worrylevel / 3)

            if boredlevel % self.test_divisibleby == 0:
                retlist.append( (self.test_truemonkey, boredlevel) )
            else:
                retlist.append( (self.test_falsemonkey, boredlevel) )
        
        self.items = []
        return retlist


testmonkeys = [
    Monkey([79,98], op_multi=19, divisibleby=23, truemonkey=2, falsemonkey=3),
    Monkey([54, 65, 75, 74], op_add=6, divisibleby=19, truemonkey=2, falsemonkey=0),
    Monkey([79,60,97], op_squareit=True, divisibleby=13, truemonkey=1, falsemonkey=3),
    Monkey([74], op_add=3, divisibleby=17, truemonkey=0, falsemonkey=1)
]

allmonkeys = [
    Monkey([54, 89, 94], op_multi=7, divisibleby=17, truemonkey=5,falsemonkey=3),
    Monkey([66,71], op_add=4, divisibleby=3, truemonkey=0,falsemonkey=3),
    Monkey([76, 55, 80, 55, 55, 96, 78], op_add=2, divisibleby=5, truemonkey=7,falsemonkey=4),
    Monkey([93, 69, 76, 66, 89, 54, 59, 94], op_add=7,divisibleby=7,truemonkey=5,falsemonkey=2),
    Monkey([80,54,58,75,99], op_multi=17,divisibleby=11,truemonkey=1,falsemonkey=6),
    Monkey([69, 70, 85, 83],op_add=8,divisibleby=19,truemonkey=2,falsemonkey=7),
    Monkey([89],op_add=6,divisibleby=2,truemonkey=0,falsemonkey=1),
    Monkey([62, 80, 58, 57, 93, 56],op_squareit=True,divisibleby=13,truemonkey=6,falsemonkey=4)
]


themonkeys = testmonkeys
themonkeys = allmonkeys

for amonkey in themonkeys:
    worrydivisor *= amonkey.test_divisibleby

# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

if False:

    START = time.perf_counter()

    for iround in range(20):
        for amonkey in themonkeys:
            retlist = amonkey.inspectItems()
            # now pass those along
            for aitem in retlist:
                themonkeys[aitem[0]].items.append(aitem[1])

        print(f"After round {iround+1}:")
        for i,amonkey in enumerate(themonkeys):
            print(f"Monkey {i}: {amonkey}")
        print()

    busymonkeys = sorted(themonkeys, key=lambda m: m.inspectcount, reverse=True)
    for i,amonkey in enumerate(busymonkeys):
        print(f"Monkey {i} inspected {amonkey.inspectcount}")
    print(f"Monkeybusiness = {busymonkeys[0].inspectcount * busymonkeys[1].inspectcount}")



    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

isPartTwo = True

for iround in range(10000):
    for amonkey in themonkeys:
        retlist = amonkey.inspectItems()
        # now pass those along
        for aitem in retlist:
            themonkeys[aitem[0]].items.append(aitem[1])


busymonkeys = sorted(themonkeys, key=lambda m: m.inspectcount, reverse=True)
for i,amonkey in enumerate(busymonkeys):
    print(f"Monkey inspected {amonkey.inspectcount}")
print(f"Monkeybusiness = {busymonkeys[0].inspectcount * busymonkeys[1].inspectcount}")






END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")