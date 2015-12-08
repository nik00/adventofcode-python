#!/bin/python

# Day 7
# each wire has identifier and carries 16 bit signal from 0 - 65535
# no signal from gate until all inputs have signal
# wire can only have signal from one source

# " "
# \\
#\" and \x plus TWO hex char
# disregard whitespace

#number of characters of code for string literals 
 # eg "abc" is 5 code but 3 literal
# in memory for values of literals

# eg: "" is 2, 0
# "abc" is 5,3 
# "aaa\"aaa" is 10,7
# "\x27" is 6, 1 (hex ') - ALWAYS ONE CHARACTER
#2+5+10+6 - 0+3+7+1
# 23 - 11 = 12
import re
def run():
    with open('input') as myInputFile:
        data = myInputFile.read()

        totalCodeDiff = 0
        for code in data.splitlines():
            #code
            print code
            codeLength = len(code)
            print codeLength
            #literal

            # minus two for starting eand ending ""
            literalLength = len(code)-2

            # \\ is 1 and \" is 1
            for escaped in re.findall(r'\\\\', code):
                literalLength -= 1
            code = re.sub(r'\\\\','', code)

            for escaped in re.findall(r'\\"', code):
                literalLength -= 1

            for hexascii in re.findall(r'\\x', code):
                literalLength -= 3
            print literalLength

            print codeLength - literalLength
            totalCodeDiff +=  codeLength - literalLength


        
        print totalCodeDiff

if __name__ == '__main__':
	run()