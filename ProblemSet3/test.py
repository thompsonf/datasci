import random

def getProb(n):
    sumTries = 0
    for i in range(10000):
        success = True
        for i in range(n - 1):
            if random.randint(1,6) == 1:
                success = False
                break
        success = success and random.randint(1,6) == 1
        if success:
            sumTries += 1
    return float(sumTries) / 10000

def probTest(limit):
    n = 1
    prob = getProb(n)
    while prob >= limit:
        n += 1
        prob = getProb(n)
    return n
    
print probTest(.1)