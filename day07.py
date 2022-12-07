#import itertools
#import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field


with open('day07.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()]   # 


thedata = testdata
thedata = alldata



# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

class Dir:
    def __init__(self, parent=None, name='') -> None:
        self.files = {}  # filename: size
        self.size = 0
        self.directories = {}  # dirname: Dir
        self.parent = parent
        self.name = name
    def print(self, depth=0):
        for k,v in self.files.items():
            print(' '*(depth*2), end='')
            print(f'- {k} (file, size={v})')
        for k, v in self.directories.items():
            print(' '*(depth*2), end='')
            print(f'- {k} (dir, size={v.size})')
            v.print(depth+1)


def parseDirCommands(thedata) -> Dir:
    root = Dir()
    active = root
    iline = 0
    while iline < len(thedata):
        # parse the next command
        words = thedata[iline].split()
        if words[0] == '$':
            # this is, yes, a command
            if words[1] == 'cd':
                # do something for changing directory
                if words[2] == '/':
                    active = root
                elif words[2] == '..':
                    active = active.parent
                else:
                    active = active.directories[words[2]]
                
                # and move on
                iline += 1

            elif words[1] == 'ls':
                # read the directory listing and do something with the listing
                iline += 1
                while (iline < len(thedata)) and (thedata[iline][0] != '$'):
                    words_ls = thedata[iline].split()
                    if words_ls[0] == 'dir':
                        # this is a new directory
                        active.directories[words_ls[1]] = Dir(active, name=words_ls[1])
                    else:
                        # this is a file
                        active.files[words_ls[1]] = int(words_ls[0])
                    iline += 1
                    # this should end up with iline on a command or done

    return root


def calcDirSize(node: Dir) -> int:
    thesum = 0
    for k,v in node.directories.items():
        thesum += calcDirSize(v)
    for _,v in node.files.items():
        thesum += v
    node.size = thesum
    return thesum
    
def sumAllDirSizesLessThan(node: Dir, sizelimit=100000) -> int:
    thesum = 0
    for _, v in node.directories.items():
        thesum += sumAllDirSizesLessThan(v, sizelimit)
    if node.size <= sizelimit:
        thesum += node.size
    return thesum


if True:

    START = time.perf_counter()

    root = parseDirCommands(thedata)
    calcDirSize(root)

    root.print()

    sumsize = sumAllDirSizesLessThan(root)
    print(f"Sum small dirs={sumsize}")
    

    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

dirsizes = []  # (name, size)

def addDirectoriesGreaterThan(node: Dir, lowerlimit):
    global dirsizes    
    if node.size > lowerlimit:
        dirsizes.append( (node.name, node.size) )
    
    for k,v in node.directories.items():
        addDirectoriesGreaterThan(v, lowerlimit)

totalspace  = 70000000 - root.size
neededspace = 30000000
needtodeleteatleast = neededspace - totalspace

addDirectoriesGreaterThan(root, needtodeleteatleast)

dirsizes = sorted(dirsizes, key=lambda d: d[1])

print(dirsizes)
print(f"Need to delete at least {needtodeleteatleast}")
print(f"Smallest big-enough dir is {dirsizes[0][0]} at {dirsizes[0][1]} size")




END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")