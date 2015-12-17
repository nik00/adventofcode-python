#!/bin/python

# Day 17
# Recursively generate possibilities both including and skipping each bucket.
import itertools
from collections import defaultdict
match = {}
match = defaultdict(lambda:0, match)

def parseData():
    containers = []
    with open('realinput') as myInputFile:
        data = myInputFile.read()
        for line in data.splitlines():
            containers.append(int(line))
    return containers

def checkSize(inQueue, targetSize, lenSoFar):
    # Each queue splits into two calls:
    #   one consuming the first item
    #   one skipping the first item
    startSize = 0
    numCombos = 0

    if len(inQueue) > 1:
        numCombos += checkSize(inQueue[1:], targetSize,lenSoFar)
        startSize += inQueue[0]
        if startSize > targetSize:
            return numCombos
        elif startSize == targetSize:
            match[lenSoFar+1] += 1
            return numCombos+1
        numCombos += checkSize(inQueue[1:], targetSize-startSize, lenSoFar+1)
    else:
        startSize += inQueue[0]
        if startSize == targetSize:
            match[lenSoFar+1] += 1
            return 1
        else:
            return 0
    return numCombos



def run():
    fitting = 150
    containers = []
    containers = parseData()
    checkSize(containers, fitting, 0)

    totalCount = 0
    for each in match:
        totalCount += match[each]
    print "Pt.1 count of combinations is: {0}".format(totalCount)

    for each in sorted(match):
        firstLevel = match[each]
        if firstLevel > 0:
            print "Pt.2 number of combos at min # of containers is {0}".format(firstLevel)
            break
    return None

if __name__ == '__main__':
    run()