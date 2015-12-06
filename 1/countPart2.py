#!/bin/python

# Day One Part Two
import sys
with open('input') as myInputFile:
    data = myInputFile.read()
    floor = 0
    for i in range(0,len(data)-1):
        print i
        if data[i] == '(':
            floor+=1
        elif data[i] == ')':
            floor-=1
        if floor == -1:
            print i+1
            sys.exit("Found it!")
        
    #numUp = data.count('(')
    #numDown = data.count(')')
    #print numUp
    #print numDown
    #print numUp-numDown

