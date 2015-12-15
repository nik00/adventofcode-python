#!/bin/python

# Day 15
# I am the cookiemonster

import itertools
def parseData():
    ingredient = {}
    ingredientList = []
    with open('realinput') as myInputFile:
        data = myInputFile.read()
        for line in data.splitlines():
            line = line.split(" ")
            ingredientName = line[0].rstrip(':')
            capacity = line[2].rstrip(',')
            durability = line[4].rstrip(',')
            flavor = line[6].rstrip(',')
            texture = line[8].rstrip(',')
            calories = line[10].rstrip(',')

            ingredient[ingredientName] = {'ingredientName':ingredientName, 'capacity':int(capacity), 'durability':int(durability), 'flavor':int(flavor), 'texture':int(texture), 'calories':int(calories)}
            ingredientList.append(ingredientName)
    return ingredient, ingredientList

def scoreOfCookie(possible, ingredient, ingredientList, calorieCounting = False):
    capScore = 0
    durScore = 0
    flavorScore = 0
    textureScore = 0
    calorieScore = 0

    for item in ingredientList:
        num = possible.count(item)
        capScore += num * ingredient[item]['capacity']
        durScore += num * ingredient[item]['durability']
        flavorScore += num * ingredient[item]['flavor']
        textureScore += num * ingredient[item]['texture']
        calorieScore += num * ingredient[item]['calories']

    if capScore < 0 or durScore < 0 or flavorScore < 0 or textureScore < 0:
        return 0
    if calorieCounting and calorieScore != 500:
        return 0
    totalScore = max(0,capScore * durScore * flavorScore * textureScore)
    return totalScore

def run():
    ingredient, ingredientList = parseData()

    #Part 1
    maxScore = 0
    for possible in itertools.combinations_with_replacement(ingredientList, 100):
        maxScore = max(scoreOfCookie(possible,ingredient, ingredientList), maxScore)
    print "Pt1. Best Cookie Score is {0}".format(maxScore)

    #Part 2
    maxScore = 0
    for possible in itertools.combinations_with_replacement(ingredientList, 100):
        maxScore = max(scoreOfCookie(possible,ingredient, ingredientList, True), maxScore)
    print "Pt2. Best Cookie Score is {0}".format(maxScore)

if __name__ == '__main__':
    run()