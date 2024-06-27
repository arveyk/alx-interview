#!/usr/bin/python3
"""
Second solution
first solve by AlgoMonster
second by prepfortech.io
"""

def validUTF8(data):
    byteCnt = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for elem in data:
        mask = 1 << 7
        if byteCnt == 0:
            while mask & elem:
                print("mask{} anded with elem{} : {}".format(mask, elem, mask & elem))
                byteCnt += 1
                mask >>= 1
            if byteCnt == 0:
                continue
            if byteCnt == 1 or byteCnt > 4:
                return false
        else:
            if not (elem & mask1 and not (elem & mask2)):
                return False
            byteCnt -= 1
    return byteCnt == 0
