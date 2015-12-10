#!/bin/python

# Day 9

import re
import sys
from collections import deque
from sets import Set

# Wrote BFS that theoretically generates infinite possibilities.
# This is due to including multiple visits (eg. ABAC) if cheaper.
# Prevents infinite iterations by throwing out all unfit paths,
# costToBeHere is key - knowing lowest cost to achieve the same 
# visited set + current location protects against cycles.
dontAllowBacktracking = True

# For Part 2
findHighestCost = False

def bfsAllNeighbours(locations, simpleLocations, visited, origin):
    bestPath = None

    pathQueue = deque() 
    visitedSet = Set()
    visitedSet.add(origin)
    pathInfo = [visitedSet, 0, origin, [origin]]
    pathQueue.append(pathInfo)

    costToBeHere = {} # path, weAt

    while len(pathQueue) > 0:
        pathInfoTuple = pathQueue.popleft()
        inPath, cost, weAt, order = pathInfoTuple
        myFrozenSet=frozenset(inPath)

        # For each place, remember minimum cost to get there.
        if (myFrozenSet,weAt) in costToBeHere:
            if costToBeHere[(myFrozenSet,weAt)] < cost:
                continue

        costToBeHere[(myFrozenSet,weAt)] = cost

        # Have we completed our visit?
        if simpleLocations.issubset(inPath):
            # If we have, is it better?
            if bestPath is None or bestPath[1] > cost:
                bestPath = [inPath,cost, order]

            # Done with this path.
            continue

        # Don't pursue paths that are already more expensive.
        if bestPath is not None and cost > bestPath[1]:
            continue

        # Add ALL Neighbours - including visited.
        for hops in locations[weAt]:
            path = Set(inPath)
            path.add(hops)
            newCost = cost + int(locations[weAt][hops])
            newOrder = list(order)
            newOrder.append(hops)

            if dontAllowBacktracking and hops in inPath:
                continue
            
            # Dont queue up paths worse than best.
            if bestPath is None or newCost < bestPath[1]:
                pathQueue.append([path, newCost, hops, newOrder])

    return bestPath


def run():
    with open('realinput') as myInputFile:
        data = myInputFile.read()

        locations = {}
        distance = {}
        simpleLocations = Set()
        for costInput in data.splitlines():
            place1, place2, distance = re.split(" to | = ", costInput)

            if place1 not in locations:
                locations[place1] = {}
                simpleLocations.add(place1)
            if place2 not in locations:
                locations[place2] = {}
                simpleLocations.add(place2)

            if findHighestCost:
                distance = '-' + distance

            locations[place1][place2] = distance
            locations[place2][place1] = distance

    possibleLowestCost = sys.maxint
    for origin in locations:
        visited = Set()
        visited.add(origin) 
        cost = bfsAllNeighbours(locations, simpleLocations, visited, origin)[1]
        possibleLowestCost = min(cost, possibleLowestCost)

        if findHighestCost:
            cost = -cost
        print "Cost to go everywhere from {0} is {1}".format(origin,cost)

    # For Part 2
    output = "Highest" if findHighestCost else "Lowest"
    if findHighestCost:
        possibleLowestCost = -possibleLowestCost

    print "{0} Cost Path is {1}".format(output, possibleLowestCost)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "2":
        findHighestCost=True
    run()