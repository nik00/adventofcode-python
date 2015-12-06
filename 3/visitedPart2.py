#!/bin/python

# Day three
# Four directions <>^v
# After each move he delivers 1 present
# How many houses receive at _least_ one present

# keep x + y coords
# <>^v changes current x+y, check if it has been visited
# if not, increment by 1 and say visited



# PART TWO
# First movement is Santa
# Second movement is Robosanta, etc.
with open('input') as myInputFile:
    data = myInputFile.read()

    santaX=0
    santaY=0
    roboX=0
    roboY=0
    placesVisited={}
    housesWithLeast1Present=0

    actor="Santa"

    for move in data:

        if actor=="Santa":
            if move=='<':
                santaX-=1
            elif move=='>':
                santaX+=1
            elif move=='^':
                santaY+=1
            elif move=='v':
                santaY-=1

            coordSet=(santaX,santaY)
            actor="Robo"

        elif actor=="Robo":
            if move=='<':
                roboX-=1
            elif move=='>':
                roboX+=1
            elif move=='^':
                roboY+=1
            elif move=='v':
                roboY-=1

            coordSet=(roboX,roboY)
            actor="Santa"

        if coordSet in placesVisited:
            continue
        else:
            placesVisited[coordSet]=1
            housesWithLeast1Present+=1

    print housesWithLeast1Present


