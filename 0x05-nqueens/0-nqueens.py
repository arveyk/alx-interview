#!/usr/bin/python3
"""
N-Queens
"""
import sys


argv = sys.argv
if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)

chessDim = (argv[-1])
if chessDim.isdigit():
    chessDim = int(chessDim)
else:
    print("N must be a number")
    exit(1)
if chessDim < 4:
    print("N must be at least 4")
    exit(1)

chessList = []
partList = []
for elem in range(chessDim):
    # part = 0
    # while part < elem:
    partList.append(elem)
    #  part += 1
    chessList.append(partList)

for y in chessList:
    nqueens = []
    nqueens.append(y)
    print("{}".format(nqueens))
