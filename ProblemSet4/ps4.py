# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    delays = [300, 150, 75, 0]
    afterDelay = 150
    finalVirusPops = [prob1Helper(delay, afterDelay, numTrials) for delay in delays]
    for num, delayAndTrials in enumerate(zip(delays, finalVirusPops)):
        pylab.subplot(2, 2, num)
        pylab.hist(delayAndTrials[1])
        pylab.title("Delay = %d" % delayAndTrials[0])
        pylab.xlabel("Final Virus Population")
        pylab.ylabel("Num Patients")
        numCured = sum(map(lambda x: x < 51, delayAndTrials[1]))
        print("Num cured with delay %d = %d" % (delayAndTrials[0], numCured))
    pylab.show()

def prob1Helper(delay, afterDelay, numTrials):
    numTimeSteps = delay + afterDelay
    maxPop = 1000
    numViruses = 100
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005

    finalVirusPops = [0 for i in range(numTrials)]
    for i in range(numTrials):
        if i % 5 == 0:
            print("Starting trial %d with delay %d" % (i, delay))
        p = TreatedPatient([ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for v in range(numViruses)], \
            maxPop)
        for timestep in range(delay):
            p.update()
        p.addPrescription("guttagonol")
        for timestep in range(delay, numTimeSteps):
            p.update()
        finalVirusPops[i] = p.getTotalPop()
    return finalVirusPops
    
#simulationDelayedTreatment(200)


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    drug1Delay = 150
    drug2Delays = [300, 150, 75, 0]
    afterDelay = 150
    finalVirusPops = [prob2Helper(drug1Delay, drug2Delay, afterDelay, numTrials) for drug2Delay in drug2Delays]
    
    for num, delayAndTrials in enumerate(zip(drug2Delays, finalVirusPops)):
        pylab.subplot(2, 2, num)
        pylab.hist(delayAndTrials[1])
        pylab.title("drug2Delay = %d" % delayAndTrials[0])
        pylab.xlabel("Final Virus Population")
        pylab.ylabel("Num Patients")
        numCured = sum(map(lambda x: x < 51, delayAndTrials[1]))
        print("Num cured with drug2Delay %d = %d" % (delayAndTrials[0], numCured))
    pylab.show()

def prob2Helper(drug1Delay, drug2Delay, afterDelay, numTrials):
    numTimeSteps = drug1Delay + drug2Delay + afterDelay
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005

    finalVirusPops = [0 for i in range(numTrials)]
    for i in range(numTrials):
        if i % 5 == 0:
            print("Starting trial %d with drug2Delay %d" % (i, drug2Delay))
        p = TreatedPatient([ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for v in range(numViruses)], \
            maxPop)
        for timestep in range(drug1Delay):
            p.update()
        p.addPrescription("guttagonol")
        for timestep in range(drug1Delay, drug1Delay + drug2Delay):
            p.update()
        p.addPrescription("grimpex")
        for timestep in range(drug1Delay + drug2Delay, numTimeSteps):
            p.update()
        finalVirusPops[i] = p.getTotalPop()
    return finalVirusPops
    
simulationTwoDrugsDelayedTreatment(200)