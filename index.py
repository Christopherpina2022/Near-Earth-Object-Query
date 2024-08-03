# This version of the app implements a command line version of the program to help speed up the production of this app until
# I can fully understand a bit more of Front end development.
import ObjectArrays
from ObjectArrays import *
import os
import ObjectLogic
from ObjectLogic import *

def menu():
    keepGoing = True
    neoSelected = 'Init'
    while keepGoing == True:  
        os.system('cls')
        print ('Near Earth object Web Service Query (Command Line version) \nby Chris Pina\n')
        print ('1: List all Near Earth Objects \n2: lookup information about a Near Earth Object \n3: Lookup charts by selected NEO \n4: Quit application')
        optionSelect = input('Please enter an option: \n')
        neoNames = neoName(objectName=[])
        match optionSelect:
            case '1':
                neoList(neoNames)
            case '2':
                neoSelected = neoLookup(neoNames, neoSelected = [])
            case '3':
                neoCharts(neoSelected)
            case '4':
                print("Goodbye.")
                keepGoing = False
            case _:
                print ('Please select an option by the number assigned to it.')
                input()
        
def neoLookup(neoNames , neoSelected):
    os.system('cls')
    # Ask user to input their NEO of choice
    print ("Entering a NEO provides various information about your selection and")
    print ("allows you to lookup charts for our selection. (You can find names in option 1)")
    stopSelect = True
    while stopSelect == True:
        neoSelect = input('Select a name (Enter nothing to exit option)')
        for i in neoNames:
            if neoSelect == i:
                # Declare variables and constants
                selectedMinDiameter = singleMinDiameter(selectedMinDiameter = '', selection = neoSelect)
                selectedMaxDiamater = singleMaxDiameter(selectedMaxDiameter = '', selection = neoSelect)
                selectedAbsoluteMagnitude = singleAbsoluteMagnitude(selectedAbsoluteMagnitude = '', selection = neoSelect)
                selectedFirstObservation = firstObserved(selectedFirstObserved = '', selection = neoSelect)
                selectedIsItHazardous = singleHazardousNEO(selectedIsItHazardous = '', selection = neoSelect)
                selectedNearestMiss = singleNearestMiss(selectedNearestMiss = [] , selection = neoSelect)
                selectedNextEncounter = singleNextEncounter(selectedNextEncounter = [], selection = neoSelect)
                CONST_LUNAR_CONVERT = 384399 # Distance between the surface of Earth to the Moon

                # Start using data from Object Logic and Arrays
                os.system('cls')
                print ("Selected NEO: " + i + ", first discovered in " + selectedFirstObservation + ".")
                print("The minimum diameter of this NEO is " + selectedMinDiameter + ".")
                print("The maximum diameter of this NEO is " + selectedMaxDiamater + ".")
                print(selectedIsItHazardous)
                print("The absolute magnitude for this NEO is " + selectedAbsoluteMagnitude + ".")
                # Convert Lunar to Kilometers (384,399 Kilometers/Unit)
                lunarNearestMiss = selectedNearestMiss[1] * CONST_LUNAR_CONVERT
                lunarNextEncounter = selectedNextEncounter[1] * CONST_LUNAR_CONVERT
                print("The nearest miss for this NEO is observed to be in " + selectedNearestMiss[0], "and will miss by " + str(selectedNearestMiss[1]),"Lunar units (" + str(lunarNearestMiss), "Kilometers).")
                print("The next close encounter will be in " + selectedNextEncounter[0], "and will miss by " + str(selectedNextEncounter[1]), "Lunar units (" + str(lunarNextEncounter), "Kilometers).")
                neoSelected = neoSelect
                input("Press enter to continue:")
                stopSelect = False
            elif neoSelect == str(''):
                stopSelect = False
            elif stopSelect == False:
                break
    return neoSelected

def neoCharts(neoSelected):
    # Select from various charts
    objectSelected = True
    chartSelected = True
    while objectSelected == True:
        if neoSelected == 'Init':
            os.system('cls')
            print("Please select a NEO before accessing this option")
            input("Press enter to continue...")
            objectSelected = False
        else:
            while chartSelected == True:
                os.system('cls')
                print ("Charts available to see for selected object: ")
                print ("1: Acceleration over time\n2: miss distance over time\n3: Five closest encounters\n4: Back to main menu")
                chartChosen = input ("Please select a chart:")
                match chartChosen:
                    case '1':
                        # Iterate every acceleration of selected Neo over time
                        chartAcceleration(neoSelected)
                        pass
                    case '2':
                        # Iterate every observed date of a NEO
                        chartDates(neoSelected = neoSelected)
                        pass
                    case '3':
                        # Showcase the five closest encounters of a selected NEO
                        chartClosestEncounters(neoSelected = neoSelected)
                        pass
                    case '4':
                        chartSelected = False
                        break
                    case _:
                        pass
            objectSelected = False
                                
def neoList(neoNames):
    os.system('cls')
    # Print out all names of NEOS in groups of five
    print ("List of all Near Earth Objects (Press any key to continue List)")
    itemLimiter=0
    for i in neoNames:
        print (i)
        itemLimiter+=1
        if itemLimiter == 10:
            input("Press any key to continue:")
            os.system('cls')
            print ("List of all Near Earth Objects (Press any key to continue List)")
            itemLimiter = 0

def chartAcceleration(neoSelected):
    # Iterate accelleration over time for selected NEO (also add iterable Delta Time as a third row ignoring the first row)
    os.system('cls')
    singleAcceleration = singleRelativeVelocity(singleAcceleration = [], selection = neoSelected)
    itemIterator = 0
    print("Acceleration over time for " + neoSelected + " from last observed date onward:")
    print("Date observed    Velocity of NEO (km/h)")
    for i in singleAcceleration:
        if itemIterator == 0:
            print (i[1] + "       " + i[0])
            lastDate = i[0]
            itemIterator += 1
        elif itemIterator >= 1:
            deltaVelocity = float(i[0]) - float(lastDate)
            print (i[1] + "       " + i[0] + " (Delta V = " + str(round(deltaVelocity)) + " km/h.)")
            lastDate = i[0]
    input("Press enter to return to chart menu:")

def chartDates(neoSelected):
    os.system('cls')
    neoEncounters = neoEncounterDates(neoEncounters=[])
    CONST_CHART_LIMIT = 10
    chartIterator = 0
    print("Miss distance of " + neoSelected + " over time")
    print("Date observed    Miss distance (Lunar units)")
    for i in neoEncounters:
        if i[0] == neoSelected:
                print (i[1] + '       ' + str(i[2]))
                chartIterator += 1
                if chartIterator >= CONST_CHART_LIMIT:
                    input("Press enter to continue:")
                    os.system('cls')
                    print("Miss distance of " + neoSelected + " over time")
                    print("Date observed    Miss distance (Lunar units)")
                    chartIterator = 0
    input("Press enter to return to chart menu:")

def chartClosestEncounters(neoSelected):
    # List off the five closest encounters for a NEO
    os.system('cls')
    chartNearestMisses = topNearestMisses(chartNearestMisses = [], selection = neoSelected)
    print ("Top Five nearest encounters for " + neoSelected + ":")
    print ("Date observed     Distance Missed (Lunar)")
    for i in chartNearestMisses:
        print (i[0] +'        ' + i[1])
    input("Press enter to continue:")

def seriousRoom():
    while True:
        print ("This is the serious room, it's where all the bad people go when they try to cheat.")
        input()
    
menu()