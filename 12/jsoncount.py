#!/bin/python
# Day 12
import re
import json
def valueOfDict(inDict):
    count = 0
    for line in re.findall("-*[0-9]+", str(inDict)):
        count += int(line)
    return count

def sumOfDictionariesContainingRed(inDict):
    sumValue = 0
    if isinstance(inDict,dict):
        if "red" in inDict.itervalues():
            return valueOfDict(inDict)
        else:
            for key, value in inDict.iteritems():
                sumValue += sumOfDictionariesContainingRed(value)
    else:
        if isinstance(inDict, list):
            for value in inDict:
                sumValue += sumOfDictionariesContainingRed(value)
    return sumValue

def run():
    with open('realinput') as myInputFile:
        data = myInputFile.read()
        count = valueOfDict(data)
        myDict = json.loads(data)
        part2 = sumOfDictionariesContainingRed(myDict)
        print "Part 1: {0}".format(count)
        print "Part 2: {0}".format(count - part2)

if __name__ == '__main__':
    run()