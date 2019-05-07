import numpy
import sys

def precision (depth):
    return 1/(10.0**depth)

depth = int(sys.argv[1])

prec = precision(depth)

#if sys.argv[1]:
#    depth = sys.argv[1]

setList = numpy.arange(0, 1.001, prec)

for x in range(0, len(setList)):
    setList[x] = format(setList[x], '.'+str(depth)+'f')

def splice(setList, depth):
    # print('serlist', setList)
    third = (setList[-1] - setList[0]) / 3 + setList[0]
    doublethird = ( (setList[-1] - setList[0]) * 2.0 ) / 3.0 + setList[0]
    #print(doublethird)
    left = filter(lambda x: x<third, setList)
    right = filter(lambda x: x>doublethird, setList)
    #print(right)
    if depth > 1:
        return splice(left,depth-1) + splice(right,depth-1)
    else:
        return [left, right]

print(splice(setList, depth))