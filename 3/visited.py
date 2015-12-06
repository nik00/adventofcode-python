#!/bin/python

# Day three
# Four directions <>^v
# After each move he delivers 1 present
# How many houses receive at _least_ one present

# keep x + y coords
# <>^v changes current x+y, check if it has been visited
# if not, increment by 1 and say visited

with open('input') as myInputFile:
    data = myInputFile.read()

    x=0
    y=0
    placesVisited={}
    housesWithLeast1Present=0

    for move in data:
        if move=='<':
            x-=1
        elif move=='>':
            x+=1
        elif move=='^':
            y+=1
        elif move=='v':
            y-=1

        coordSet=(x,y)
        if coordSet in placesVisited:
            continue
        else:
            placesVisited[coordSet]=1
            housesWithLeast1Present+=1

    print housesWithLeast1Present


