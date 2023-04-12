#import DictionaryInit as Dict
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
    absoluteMagnitude = neoMagnitude(absoluteMagnitude=[])
    for i in absoluteMagnitude:
        if i[0] == selection:
            selectedAbsoluteMagnitude = str(i[1])
    return selectedAbsoluteMagnitude

def firstObserved(selectedFirstObserved, selection):
    firstObserved = firstObservation(firstObserved=[])
    for i in firstObserved:
        if i[0] == selection:
            selectedFirstObserved = str(i[1])
    return selectedFirstObserved

def singleHazardousNEO(selectedIsItHazardous, selection):
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
    selectedNearestMiss = []
    selectedTempList = []
    neoEncounters = neoEncounterDates(neoEncounters=[])
    for i in neoEncounters:
        if i[0] == selection:
            selectedTempList.append([i[1], i[2]])
    x = 999
    for i in selectedTempList:
        tempMissDistance = i[1]
        if tempMissDistance < x:
            selectedNearestMiss = [i[0], i[1]]
            x = i[1]
    return selectedNearestMiss

def singleNextEncounter(selectedNextEncounter, selection):
    # establish the current time in YYYY-MM-DD Format
    currentTime = datetime.now()
    tempEncounterTimes = []
    neoEncounters = neoEncounterDates(neoEncounters = [])
    # Convert String to Date time format then append into a Temp list
    for i in neoEncounters:
        if i[0] == selection:
            fixedDate = datetime.strptime(i[1], '%Y-%m-%d')
            #fixedDateFromString = datetime.strftime(fixedDate, '%Y-%m-%d')
            tempEncounterTimes.append([fixedDate, i[2]])
    # Find the smallest difference of all items in Temp list by subtracting the time with the current date
    # Maybe run this for every item per list and append a new parameter at the end to find the smallest number?
    nextEncounter = min(tempEncounterTimes[0], key=lambda x: abs(x - currentTime))
    selectedNextEncounter = [nextEncounter.strftime('%Y-%m-%d'), ]
    print(selectedNextEncounter)
    return selectedNextEncounter

singleNextEncounter(selectedNextEncounter = [], selection = 'Eros')