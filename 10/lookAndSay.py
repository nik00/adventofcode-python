#!/bin/python
# Day 10
# LookAndSay
from collections import deque

problemInput = '1113122113'

def lookAndSay(myInput):
    newString=''
    myQueue = deque(myInput)
    while myQueue:
        first = myQueue.popleft()
        count = 1
        while myQueue and myQueue[0] == first:
            myQueue.popleft()
            count +=1
        newString += str(count) + first
    return newString

def run():
    iterate = lookAndSay(problemInput)
    for i in range(49):
        iterate = lookAndSay(iterate)
    print len(iterate)

if __name__ == '__main__':
    run()

# For 40 Loops, str = str + count + first -  7.578 seconds
# str += count + first - 0.781 seconds
# 38720199 function calls in 14.850 seconds List for 50
# 16808233 function calls in 10.946 seconds str += for 50
