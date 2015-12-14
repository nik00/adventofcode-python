#!/bin/python

# Day 13

from sets import Set
import itertools
import re

def costOf(possible, happiness):
    cost = 0
    idx = 0
    while idx+1 < len(possible):
        cost += happiness[possible[idx]][possible[idx+1]]
        cost += happiness[possible[idx+1]][possible[idx]]
        idx +=1
    cost += happiness[possible[idx]][possible[0]]
    cost += happiness[possible[0]][possible[idx]]
    return cost

def optimizeTableHappiness(listOfPeople, happinessMatrix):
    maxHappiness = 0
    allPermutations=list(itertools.permutations(listOfPeople))
    for possibleArrangement in allPermutations:
        cost = costOf(possibleArrangement, happinessMatrix)
        maxHappiness = max(maxHappiness, cost)
    return maxHappiness

def run():
    listOfAllPeople = Set()
    happiness = {}

    # 1 - Parse Data
    with open('realinput') as myInputFile:
        data = myInputFile.read()
        for line in data.splitlines():
            line = re.sub('\.', '', line)
            spaceSplit = line.split(" ")
            person1 = spaceSplit[0]
            person2 = spaceSplit[-1]
            positive = 'g' in spaceSplit[2]
            value =spaceSplit[3]

            if person1 not in listOfAllPeople:
                listOfAllPeople.add(person1)
                happiness[person1] = {}
            if person2 not in listOfAllPeople:
                listOfAllPeople.add(person2)
                happiness[person2] = {}

            if positive:
                happiness[person1][person2] = int(value)
            else:
                happiness[person1][person2] = -int(value)

    # 2 - Permute Max Happiness
    part1 = optimizeTableHappiness(listOfAllPeople, happiness)
    print "Pt1. Overall Table Happiness is {0}".format(part1)

    # 3 - Add self
    listOfAllPeople.add("me")
    happiness["me"] = {}
    for person in listOfAllPeople:
        happiness["me"][person] = 0
        happiness[person]["me"] = 0

    # 4 - Permute Max Happiness
    part2 = optimizeTableHappiness(listOfAllPeople, happiness)
    print "Pt2. Overall Table Happiness is {0}".format(part2)

if __name__ == '__main__':
    run()