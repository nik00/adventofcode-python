#!/bin/python
# Day 11
from string import lowercase

def hasOnePair(inputString):
	for char in lowercase:
		regex = char+char
		if regex in inputString:
			return True
	return False

def hasTwoPairs(inputString):
	count=0 
	for char in lowercase:
		if count > 2:
			break
		regex = char+char
		if regex in inputString:
			count +=1
	if count == 2:
		return True
	return False

def hasOneStraight(inputString):
	for idx, char in enumerate(lowercase):
		if char == 'y' or char == 'z':
			continue
		regex = char+lowercase[idx+1]+lowercase[idx+2]
		if regex in inputString:
			return True

def incrementString(inputString):
	if inputString[-1] == 'z':
		inputString = incrementString(inputString[:-1]) + 'a'
	else:
		newLastChar = chr(ord(inputString[-1]) + 1)
		inputString = inputString[:-1] + newLastChar
	return inputString

def findNextPassword(inputPassword):
    while True:
        inputPassword = incrementString(inputPassword)
        if 'o' in inputPassword or 'i' in inputPassword or 'l' in inputPassword:
            continue
        if hasTwoPairs(inputPassword):
            if hasOneStraight(inputPassword):
                return inputPassword

def run():
    inputString = 'hepxcrrq'
    nextPassword = findNextPassword(inputString)
    print "Part 1: {0}".format(nextPassword)
    nextNextPassword = findNextPassword(nextPassword)
    print "Part 2: {0}".format(nextNextPassword)
if __name__ == '__main__':
    run()
