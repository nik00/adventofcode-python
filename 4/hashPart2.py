#!/bin/python

# Day four
# Advent coins
# md5 hashes which start with hexadecimal 0x00000 (5 zeroes)
# input to md5 hash is secret key + decimal number.
# find the LOWEST number decimal that when appended to your secret key gives you 5 zeroes.


# Part Two
# HOLD ON TO YOUR HAT PYTHON WE'RE GOING IN
import hashlib
import sys
prependKey="iwrupvqb"
decimal=0

while True:
    hashOut = hashlib.md5(prependKey+str(decimal)).hexdigest()

    #if hashOut starts with 5 zeroes:
    if hashOut.startswith("000000"):
        print hashOut
        print decimal
        sys.exit("Done!")
    else:
        decimal +=1
