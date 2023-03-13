#import DictionaryInit as Dict
#import Menu 
import ObjectArrays as Arrays
from ObjectArrays import *
from datetime import datetime

def averageDiameter():
    #Find Average Min and Max Diameter of NEOs
    
    # list is also returning the name, so we need to only use the 2nd list item from a bigger list, which
    # could be done by creating a new list that only has the data from the 2nd list item per value.
    
    # For now all i want to do is create a function that lists the name and the diameter like Name, Diameter which
    # can be used later when i want that data printed on the screen in the menu
    
    objectSizeMin = neoDiameterMin(objectSizeMin = [])
    objectSizeMax = neoDiameterMax(objectSizeMax = [])
    
    minDiameter = []
    maxDiameter = []
    avgMinDiameter = 0
    avgMaxDiameter = 0
    
    for i in (objectSizeMin):
        minDiameter.append(i[1])
    for i in (objectSizeMax):
        maxDiameter.append(i[1])

    print(minDiameter, maxDiameter)
    
# Test Avg Diameter
averageDiameter()

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

def closestEncounter():
    # Find the lowst number by Lunar units from how far a NEO missed Earth
    lowestCE = min(Arrays.neoMissDistance.missDistance[1])
    return lowestCE