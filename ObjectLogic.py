#import DictionaryInit as Dict
#import Menu 
import ObjectArrays as Arrays
from ObjectArrays import *
from datetime import datetime

def averageDiameter():
    #Find Average Min and Max Diameter of NEOs
    objectSizeMin = []
    objectSizeMax = []
    #neoDiameterMin(objectSizeMin)
       
    sizeMin = sum(neoDiameterMin(objectSizeMin))/len(neoDiameterMin(objectSizeMin))
    print (sizeMin)
    #sizeMax = sum(neoDiameter.objectSizeMax)/len(neoDiameter.objectSizeMax)

    #print(sizeMax, sizeMin)
    #return(sizeMin, sizeMax)

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