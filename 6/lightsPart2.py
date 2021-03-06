#!/bin/python

# Day six
# 1000 x 1000 grid
# lights numbered from 0,0 to 999,999
# instructions to turn on, turn off, or toggle on INCLUSIVE RANGES
# ranges are given as RECTANGLES.
# eg. 0,0 through 2,2 means the 9 lights 0,0 0,1 0,2 1,0 1,1 1,2 2,0 2,1 2,2.

# lights are all off

# eg. turn on 0,0 through 999,999 will turn on every light
# toggle 0,0 through 999,0 would toggle first line of 1000 lights


# PART TWO

# Lights have brightness from 0 to higher
# Turn on increases by 1
# Turn off decreases by 1 - minimum of zero.
# Toggle means increase by 2

# What is TOTAL Brightness

with open('input') as myInputFile:
    data = myInputFile.read()


    lightStatus = {}
    for i in range(0,1000):
        for j in range (0, 1000):
            lightStatus[(i,j)] = 0


    # do double ranges for the difference.
    # eg 0,0 through 20,20
    # for i in 0-20 and for j in 0-20
    # act on light

    for line in data.splitlines():
        splittedLine=line.split(' ')
        start=splittedLine[len(splittedLine)-3]
        end=splittedLine[len(splittedLine)-1]
        action=splittedLine[len(splittedLine)-4]

        startCoords=start.split(',')
        startX=int(startCoords[0])
        startY=int(startCoords[1])

        endCoords=end.split(',')
        endX=int(endCoords[0])
        endY=int(endCoords[1])

        for i in range(startX, endX+1):
            for j in range (startY, endY+1):
                coord = i,j
                if action == "on":
                    lightStatus[coord] += 1
                elif action == "off":
                    lightStatus[coord] = max(0, lightStatus[coord]-1)
                elif action == "toggle":
                    lightStatus[coord] += 2

    lightBrightness = 0
    for i in range(0,1000):
        for j in range (0, 1000):
            lightBrightness += lightStatus[(i,j)]
    print lightBrightness
