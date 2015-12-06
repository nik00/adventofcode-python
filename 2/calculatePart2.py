#!/bin/python

# Day two
# list of lxwxh of each present
# every present is box
# surface area is 2*l*w+2*w*h+2*h*l plus the area of the SMALLEST SIDE

# eg. 2x3x4 is 2*2*3 + 2*3*4 + 2*2*4 plus area of smallest side which is 2*3



# side1 = l*w
# side2 = w*h
# side3=  h*l
# sa = (side1+side2+side3)*2 + min(side1,side2,side3)


# Part two
# Ribbon is all same width
# They want exact length
# Shortestdistance around its sides
 # This is the smallest perimeter of any one face???
# Plus a ribbon, which is equal to volume ni cubic feet.

with open('input') as myInputFile:
    data = myInputFile.read()

    totalRibbon = 0

    for string in data.splitlines():
        fields=string.split("x")
        l=int(fields[0])
        w=int(fields[1])
        h=int(fields[2])


        side1P = 2*(l+w)
        side2P = 2*(w+h)    
        side3P = 2*(h+l)

        volume = l*h*w

        ribbonLength = volume + min(side1P,side2P,side3P)
        totalRibbon += ribbonLength

    print totalRibbon
