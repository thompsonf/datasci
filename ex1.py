import pylab
import numpy as np

def loadFile():
    inFile = open('julyTemps.txt')
    high = []
    low = []
    for line in inFile:
        fields = line.strip().split()
        if len(fields) == 3 and fields[0].isdigit():
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return low, high
            
def producePlot(lowTemps, highTemps):
    diffTemps = list(np.array(highTemps) - np.array(lowTemps))
    pylab.plot(range(1,32), diffTemps)
    pylab.title("Day by Day Ranges in Temperature in Boston in July 2012")
    pylab.xlabel("Days")
    pylab.ylabel("Temperature Ranges")
    pylab.show()

producePlot(*loadFile())