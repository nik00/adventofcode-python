#!/bin/python

# Day 7
# each wire has identifier and carries 16 bit signal from 0 - 65535
# no signal from gate until all inputs have signal
# wire can only have signal from one source

# eg x AND y -> z means x and y connect to AND, which then connect to Z
# 123 -> x means that x has signal 123
# x AND y -> z means that wire Z has value of x AND y
# p LSHIFT 2 -> q means that q has value from p left-shifted by 2
# NOT e -> f means that f gets bitwise NOT of e
# OR and RSHIFT

# test input
# so you have some object and it has a signal.. and you find it
import sys

def getValue(structure, values, equation):

    # Do I want to recurse this? Value could call value for all previous
    #Inputs can be:
    #123
    # lx
    # x AND y
    #x OR y
    #x LSHIFT 2 
    #y RSHIFT 2 
    #NOT x 

    # Missed that input to OR/AND can also just be number.

    equation = equation.split(' ')
    #print equation
    if equation[0].isdigit() and len(equation) == 1:
        #We have just a value
        return int(equation[0])
    elif equation[0] == "NOT":

        value = equation[1]
        if not value.isdigit():
           # if equation
            value = values[value]

        if value != None:
            return ~ int(value)

        return None

    elif len(equation) == 1:
        #We have bare wire
        if values[equation[0]] != None:
            return int(values[equation[0]])
        else:
            return None

    elif equation[1] == "LSHIFT":

        value = equation[0]
        if not value.isdigit():
            value = values[value]

        if value != None:
            return int(value) << int(equation[2])

        return None

    elif equation[1] == "RSHIFT":

        value = equation[0]
        if not value.isdigit():
            value = values[value]

        if value != None:
            return int(value) >> int(equation[2])

        return None

    elif equation[1] == "AND":
        
        leftValue = equation[0]
        if not leftValue.isdigit():
            leftValue = values[leftValue]

        rightValue = equation[2]
        if not rightValue.isdigit():
            rightValue = values[rightValue]

        if leftValue != None and rightValue != None:
            return int(leftValue) & int(rightValue)
        
        return None

    elif equation[1] == "OR":

        leftValue = equation[0]
        if not leftValue.isdigit():
            leftValue = values[leftValue]

        rightValue = equation[2]
        if not rightValue.isdigit():
            rightValue = values[rightValue]

        if leftValue != None and rightValue != None:
            return int(leftValue) | int(rightValue)
        
        return None

    sys.exit("Really bad")

def run():
    with open('input') as myInputFile:
        data = myInputFile.read()

        # Make some structure:

        # Name, value of the signal, and what it is built from.


        # Iterate? Or wire it all up then calculate once? I think wire up.
        structure = {}
        values = {}

        for line in data.splitlines():

            # Parse the command
            #print line

            line = line.split('->')
            lhs = line[0].rstrip()
            rhs = line[1].lstrip()

            #print lhs
            #print rhs

            #Storing the value into rhs
            # LHS is the operation
            # What is the value of the operation?
            #value(rhs)

            structure[rhs] = lhs


            # Find the value on left side

            # Assign it to right side

            # Update everything?

            #print structure

        needRetry=1
        while needRetry:
            needRetry=0
            for wire, equation in structure.iteritems():
                try:
                    #print values
                    #print equation
                    #print "Getting value of {0} to put into {1}".format(equation, wire)
                    value = getValue(structure, values, equation)
                    value = value & 65535
                    #if value != False:
                        #value = value & 65535
                    if wire in values:
                        if values[wire] != value:
                            values[wire] = value
                            print "updating {0} to {1}".format(wire, value)
                    else:
                        values[wire] = value
                        print "setting {0} to {1}".format(wire, value)

                    #print values["a"]
                    #raw_input()
                except KeyError:
                    #raw_input()
                    # going to need a retry
                    needRetry=1
                    pass

        print values["a"]
        structure["b"]=str(values["a"])

        values = {}

        needRetry=1
        while needRetry:
            needRetry=0
            for wire, equation in structure.iteritems():
                try:
                    #print values
                    #print equation
                    #print "Getting value of {0} to put into {1}".format(equation, wire)
                    value = getValue(structure, values, equation)
                    value = value & 65535
                    #if value != False:
                        #value = value & 65535
                    if wire in values:
                        if values[wire] != value:
                            values[wire] = value
                            print "updating {0} to {1}".format(wire, value)
                    else:
                        values[wire] = value
                        print "setting {0} to {1}".format(wire, value)

                    #print values["a"]
                    #raw_input()
                except KeyError:
                    #raw_input()
                    # going to need a retry
                    needRetry=1
                    pass
        #@print values[b]
        #print structure[b]
        print values["a"]
        #print structure[a]



if __name__ == '__main__':
    run()