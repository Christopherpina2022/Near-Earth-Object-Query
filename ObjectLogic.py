#import DictionaryInit as Dict
#import Menu 
import ObjectArrays as Arrays
from ObjectArrays import *
from datetime import datetime


def averageDiameter(avgDiameter):
    # Find Average Min and Max Diameter of NEOs
    
    # Declare lists and setup to convert to average number
    objectSizeMin = neoDiameterMin(objectSizeMin = [])
    objectSizeMax = neoDiameterMax(objectSizeMax = [])
    minDiameter = []
    maxDiameter = []
    
    for i in (objectSizeMin):
        minDiameter.append(i[1])
    for i in (objectSizeMax):
        maxDiameter.append(i[1])
    
    # Average number is Sum of all numbers / number of all items listed
    avgDiameter = []
    avgDiameter.append(round(sum(minDiameter)/len(minDiameter)))
    avgDiameter.append(round(sum(maxDiameter)/len(maxDiameter)))
    return (avgDiameter)
    
# Test Avg Diameter

def nextEncounter():
    # Determine the amount of time until the next Close Encounter and what object it is
    now = datetime.now()
    currentTime = now.strftime('%Y-%m-%d')
    print(currentTime)

    # Use Lambda function to find the closest date from current time
    res = min(Arrays.neoTimes.objectTime[1], key=lambda sub: abs(sub - currentTime))
    for i in Arrays.neoTimes.objectTime():
        if Arrays.neoTimes.objectTime[1] == str(res):
            nextEncounterTime = Arrays.neoTimes.objectTime(i)
            return nextEncounterTime

def closestEncounter(lowestCE):
    # Find the lowest number by Lunar units from how far a NEO missed Earth
    lowestCE = ['name', 'date', 999]
    listMissDistance = neoMissDistance(missDistance=[])
    for i in listMissDistance:
        if float(i[2]) < float(lowestCE[2]):
            lowestCE = i  
    return lowestCE

def isNEOHazardous():
    # create logic that Prints out Yes or No as a string determined by the input given
    Neos = hazardousNEOS(isNEOHazardous=[])
    
    for i in Neos:
        if i[0] == testNEO:
            print (i)
        
        
#isNEOHazardous()