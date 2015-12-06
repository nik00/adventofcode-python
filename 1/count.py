#!/bin/python

with open('input') as myInputFile:
    data = myInputFile.read()
    numUp = data.count('(')
    numDown = data.count(')')
    print numUp
    print numDown
    print numUp-numDown

