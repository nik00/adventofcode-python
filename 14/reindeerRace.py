#!/bin/python

# Day 14

def parseData():
    reindeer = {}
    with open('realinput') as myInputFile:
        data = myInputFile.read()
        for line in data.splitlines():
            line = line.split(" ")
            name = line[0]
            maxSpeed = line[3]
            maxSpeedTime = line[6]
            restTime = line[-2]
            reindeer[name] = {'maxSpeed':maxSpeed, 'maxSpeedTime':maxSpeedTime, 'restTime':restTime, 'curDist':0, 'points':0}
    return reindeer

def reindeerDistAt(time, reindeer):
    maxSpeed = int(reindeer['maxSpeed'])
    maxSpeedTime = int(reindeer['maxSpeedTime'])
    restTime = int(reindeer['restTime'])

    cyclesDone = time/(maxSpeedTime + restTime)
    finishedCycleDistance = cyclesDone*maxSpeed*maxSpeedTime
    timeInCurrentCycle = time%(maxSpeedTime+restTime)
    currentCycleDistance = min(timeInCurrentCycle, maxSpeedTime)*maxSpeed
    totalDistance = finishedCycleDistance + currentCycleDistance

    return totalDistance

def run():
    reindeer = parseData()
    time = 2503
    maxDist = 0

    #Part 1
    for key, val in reindeer.iteritems():
        distAtTime = reindeerDistAt(time, val)
        maxDist = max(maxDist, distAtTime)
    print "Pt1. Furthest distance travelled in {0}s is {1}".format(time, maxDist)

    #Part 2
    for s in range(1,time+1):
        maxDistAfterSecond = 0
        for key, val in reindeer.iteritems():
            distAtTime = reindeerDistAt(s, val)
            reindeer[key]['curDist'] = distAtTime
            maxDistAfterSecond=max(maxDistAfterSecond, distAtTime)
        for name, val in reindeer.iteritems():
            if val['curDist'] == maxDistAfterSecond:
                val['points'] += 1
            val['curDist'] = 0

    maxPoints = 0
    for key, val in reindeer.iteritems():
        maxPoints = max(maxPoints, val['points'])
    print "Pt2. Maximum points after {0}s is {1}".format(time, maxPoints)




if __name__ == '__main__':
    run()