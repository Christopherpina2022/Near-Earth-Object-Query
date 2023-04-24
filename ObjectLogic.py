#import DictionaryInit as Dict
import ObjectArrays as Arrays
from ObjectArrays import *
from datetime import datetime, timedelta
     
def singleMinDiameter(selectedMinDiameter, selection):
    # Find the Min and Max Diameter for a selected Item
    objectSizeMin = neoDiameterMin(objectSizeMin = [])
    for i in objectSizeMin:
        if i[0] == selection:
            selectedMinDiameter = str(i[1])
    return selectedMinDiameter

def singleMaxDiameter(selectedMaxDiameter, selection):
    # Find the Min and Max Diameter for a selected Item
    objectSizeMax = neoDiameterMax(objectSizeMax = [])
    for i in objectSizeMax:
        if i[0] == selection:
            selectedMaxDiameter = str(i[1])
    return selectedMaxDiameter

def singleAbsoluteMagnitude(selectedAbsoluteMagnitude, selection):
    # Determine Absolute magnitude based off selected NEO
    absoluteMagnitude = neoMagnitude(absoluteMagnitude=[])
    for i in absoluteMagnitude:
        if i[0] == selection:
            selectedAbsoluteMagnitude = str(i[1])
    return selectedAbsoluteMagnitude

def firstObserved(selectedFirstObserved, selection):
    # Identify what the first observed date is based off selected NEO
    firstObserved = firstObservation(firstObserved=[])
    for i in firstObserved:
        if i[0] == selection:
            selectedFirstObserved = str(i[1])
    return selectedFirstObserved

def singleHazardousNEO(selectedIsItHazardous, selection):
    # Determine if selected NEO is Hazardous
    selectedIsItHazardous = ''
    isNEOHazardous = hazardousNEOS(isNEOHazardous=[])
    for i in isNEOHazardous:
        if i[0] == selection:
            if i[1] == True:
                selectedIsItHazardous = "This object is hazardous."
            elif i[1] == False:
                selectedIsItHazardous = "This object is not hazardous."
    return selectedIsItHazardous

def singleNearestMiss(selectedNearestMiss, selection):
    # find the smallest miss distance for a selected object
    # Declare local variables and constants
    selectedNearestMiss = []
    selectedTempList = []
    CONST_PLACEHOLDER = 999
    neoEncounters = neoEncounterDates(neoEncounters=[])
    for i in neoEncounters:
        if i[0] == selection:
            selectedTempList.append([i[1], i[2]])
    x = CONST_PLACEHOLDER
    for i in selectedTempList:
        tempMissDistance = i[1]
        if tempMissDistance < x:
            selectedNearestMiss = [i[0], i[1]]
            x = i[1]
    return selectedNearestMiss

def singleNextEncounter(selectedNextEncounter, selection):
    # establish the current time in YYYY-MM-DD Format
    # Declare local variables and constants
    currentTime = datetime.now()
    tempEncounterTimes = []
    neoEncounters = neoEncounterDates(neoEncounters = [])
    CONST_PLACEHOLDER = 99
    CONST_DELTA_PLACEHOLD = timedelta(days=9999999)
    CONST_DELTA_MIN = timedelta(days=0)
    # Convert String to Date time format then append into a Temp list
    for i in neoEncounters:
        if i[0] == selection:
            fixedDate = datetime.strptime(i[1], '%Y-%m-%d')
            tempEncounterTimes.append([fixedDate, i[2], CONST_PLACEHOLDER])
    # Find the smallest difference of all items in Temp list by subtracting the time with the current date
    closestTimeDelta = CONST_DELTA_PLACEHOLD
    for i in tempEncounterTimes:
        nextEncounterDifference = lambda x: x - currentTime
        itemDifference = nextEncounterDifference(i[0])
        if itemDifference >= CONST_DELTA_MIN:
            if  itemDifference < closestTimeDelta:
                # Declare current value as the next encounter and format date time back to string to be read by index
                closestTimeDelta = itemDifference
                fixedDateFromString = datetime.strftime(i[0], '%Y-%m-%d')
                selectedNextEncounter = [fixedDateFromString, i[1]]
    return selectedNextEncounter

def singleRelativeVelocity(singleAcceleration, selection):
    # Iterate velocity and Dates of a selected NEO
    relativeVelocity = neoRelativeVelocity(relativeVelocity=[])
    tempSelectedVelocity = []
    sortVelocity = []
    singleAcceleration = []
    currentTime = datetime.now()
    for i in relativeVelocity:
        if i[0] == selection:
            # convert strings to date time format
            dateTimeConvert = datetime.strptime(i[2], '%Y-%m-%d')
            tempSelectedVelocity.append([i[1], dateTimeConvert, timedelta(days=0)])
    # I want to make the data start from last date from Current day and also be in order from Newest to Oldest
    # First I want to only include data that has a Negative Time Delta when compared with a Time Delta Lambda Function
    # and then order by string 
    for i in tempSelectedVelocity:
        timedifference = lambda x: x - currentTime
        if timedifference(i[1]) < timedelta(days=0):
            # Convert date time back to string
            dateTimeToString = datetime.strftime(i[1], '%Y-%m-%d')
            deltaConvert = float(timedifference(i[1]).days)
            sortVelocity.append([i[0], dateTimeToString, deltaConvert])
    singleAcceleration = sortVelocity
    singleAcceleration = sorted(sortVelocity, key= lambda x: x[2], reverse=True)
    return singleAcceleration

def topNearestMisses(chartNearestMisses, selection):
    # Find the top 5 nearest Misses after sorting in ascending order of distance
    selectedNEOList = []
    neoEncounters = neoEncounterDates(neoEncounters=[])
    x = 0
    chartNearestMisses = []
    for i in neoEncounters:
        if i[0] == selection:
            selectedNEOList.append([i[1], i[2]])
    sortedMisses = sorted(selectedNEOList, key = lambda x: x[1])  
    for i in sortedMisses:
        if x < 5:
            chartNearestMisses.append([i[0], i[1]])
            x += 1
        else:
            break
    return chartNearestMisses