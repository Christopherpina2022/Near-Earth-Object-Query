#import DictionaryInit as Dict
import ObjectArrays as Arrays
from ObjectArrays import *
from datetime import datetime, timedelta

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
    encounterTimes = []
    neoEncounters = neoEncounterDates(neoEncounters = [])
    CONST_PLACEHOLDER = 99
    CONST_DELTA_PLACEHOLD = timedelta(days=9999999)
    # Convert String to Date time format then append into a Temp list
    for i in neoEncounters:
        if i[0] == selection:
            fixedDate = datetime.strptime(i[1], '%Y-%m-%d')
            #fixedDateFromString = datetime.strftime(fixedDate, '%Y-%m-%d')
            tempEncounterTimes.append([fixedDate, i[2], CONST_PLACEHOLDER])
    # Find the smallest difference of all items in Temp list by subtracting the time with the current date
    # I am aware that this logic is due to have a bug, but this took like 3 hours to get working
    closestTimeDelta = CONST_DELTA_PLACEHOLD
    for i in tempEncounterTimes:
        nextEncounterDifference = lambda x: abs(x - currentTime)
        itemDifference = nextEncounterDifference(i[0])
        if itemDifference >= timedelta(days=0):
            if  itemDifference < closestTimeDelta:
                # Declare current value as the next encounter and format date time back to string to be read by index
                closestTimeDelta = itemDifference
                fixedDateFromString = datetime.strftime(i[0], '%Y-%m-%d')
                selectedNextEncounter = [fixedDateFromString, i[1]]
    return selectedNextEncounter