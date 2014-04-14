import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    numSuccess = 0
    for i in range(numTrials):
        balls = ['r','r','r','g','g','g']
        random.shuffle(balls)
        if balls[0] == balls[1] and balls[1] == balls[2]:
            numSuccess += 1
    return float(numSuccess)/numTrials
    
print noReplacementSimulation(1000000)