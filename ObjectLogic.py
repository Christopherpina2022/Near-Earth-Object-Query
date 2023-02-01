import DictionaryInit as Dict
import Menu as Menu
import ObjectArrays as Arrays
from datetime import datetime

def averageDiameter():
    #Find Average Min and Max Diameter of NEOs
    sizeMin = sum(Arrays.neoDiameter.objectSizeMin)/len(Arrays.neoDiameter.objectSizeMin)
    sizeMax = sum(Arrays.neoDiameter.objectSizeMax)/len(Arrays.neoDiameter.objectSizeMax)

    print(sizeMax, sizeMin)
    return(sizeMin, sizeMax)

# Test Avg Diameter
#averageDiameter()

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