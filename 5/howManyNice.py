#!/bin/python

# Day five

# string is NICE only if all of the properties are true:
# at LEAST having three vowels (aeiou)
    # or # vowels > 3
# at LEAST one letter that appears twice in a row (eg. aa)
# does NOT contain (ab, cd, pq or xy)

import re
import string
niceStrings = 0 
found = 0

with open('input') as myInputFile:
    data = myInputFile.read()

    for line in data.splitlines():

        print line
        # if line contains ab, cd, pq, or xy, continue
        # if line has < 3 vowels, continue
        # if line has a double letter, we are gooood

        if re.findall('ab', line) or re.findall('cd', line) or re.findall('pq', line) or re.findall('xy', line):
            print "Skipping due to ab,cd,pq,xy"
            #raw_input()
            continue

        vowelCount = len(re.findall('[aeiou]', line))
        if vowelCount < 3:
            print "Skipping due to not many vowels"
            #raw_input()
            continue

        for letter in list(string.ascii_lowercase):
            regex = str(letter)+str(letter)
            if re.findall(regex,line):
                if not found:
                    niceStrings+=1
                    print "This string is nice"
                found=1

        if not found:
            print "Skipping due to no consecutives"
        found=0

    print niceStrings





