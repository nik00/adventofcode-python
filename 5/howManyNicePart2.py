#!/bin/python

# Day five

# 1) pair of any two letters that appear at least twice in the string without overlapping.
# eg. xyxy counts for two pairs of xy. aabcaa counts for two pairs of aa
# aaa doesn't count for two aa because it overlaps

# it contains one letter that repeats with a single letter between them.
# eg xyx, efe or aaa.

import re
import string
niceStrings = 0

with open('input') as myInputFile:
    data = myInputFile.read()

    for line in data.splitlines():

        print line

        
        match=0

        #number one is letter[a-z]letter
        for letter in list(string.ascii_lowercase):
            regex = "{0}[a-z]{0}".format(letter)
            if re.findall(regex,line):
                print "Matched Rule One"
                match=1

        if match==0:
            print "Skipping #1"
            continue
        else:
            match=0

        #number two is pairpair
        for letter1 in list(string.ascii_lowercase):
            for letter2 in list(string.ascii_lowercase):
                regex = str(letter1)+str(letter2)
                if len(re.findall(regex,line)) > 1:
                    match=1                

        if match==0:
            print "Skipping #2"
            continue
        else:
            print "Found Nice String"
            niceStrings+=1
            match=0


    print niceStrings





