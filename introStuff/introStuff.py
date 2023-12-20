import random
import pandas as pd
import numpy as np
from scipy.stats import norm

qbData = pd.read_csv("QBStats_all.csv")

## variable for selected quarterback
qbSelected = 'Michael VickM. Vick' 

## mixed key is column of qbSelected 
qbRows = qbData.loc[(qbData["qb"] == qbSelected)]

qbCmp = np.average(qbRows['cmp'])
qbAtt = np.average(qbRows['att'])
qbProb = qbCmp/qbAtt

# hypothetical defensive completion rate 
defense = .673

bayesResult = (qbProb * defense) / ((qbProb * defense) + ((1 - qbProb)*(1 - defense)))

# probability of completion
print(qbProb)
# bayes stats probability with hypothetical defensive completion rate
print(bayesResult)



# print(qbCmp)
# print(qbAtt)
# print(qbProb)



## variable for total yards attempt 
qbTotalYA = np.sum(qbRows['yds'])
qbSTDYA = np.std(qbRows['yds'])

print('Selected qb yards per career ' + str(qbTotalYA))

qbAvgYds = np.average(qbRows['yds'])

# list of the simulated numebers 
simmedNumbers = []


for i in range(0, 10000):
    rP = random.uniform(0, 1)
# percent point function; inverse of the CDF 
    # Tells you the value below which the random variable will fall with that probability
    ydsSim = norm.ppf(rP, loc=qbAvgYds, scale=qbSTDYA)
    simmedNumbers.append(ydsSim)

avgSimmedGames = np.average(simmedNumbers)

# print (str(avgSimmedGames))

