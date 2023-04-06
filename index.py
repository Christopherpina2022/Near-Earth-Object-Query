# This version of the app implements a command line version of the program to help speed up the production of this app until
# I can fully understand a bit more of Front end development.
import ObjectArrays as Arrays
from ObjectArrays import *
import os

def menu():
    menuList = [1,2,3]
    keepGoing = True
    os.system('cls')
    print ('Near Earth objet Web Service Query (Command Line version) \nby Chris Pina\n')
    while keepGoing == True:  
        print ('1: List all Near Earth Objects \n2: lookup information about a Near Earth Object \n3: Lookup charts by selected NEO \n4: Quit application')
        optionSelect = input('Please enter an option: \n')
        # Basic validation loop
        neoNames = neoName(objectName=[])
        neoSelected = ['Init']
        match optionSelect:
            case '1':
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
            case '2':
                os.system('cls')
                # Ask user to input their NEO of choice
                print ("Please enter a NEO (You can find names in option 1)")
                stopSelect = True
                while stopSelect == True:
                    neoSelect = input('Select a name ("quit" to exit option)')
                    for i in neoNames:
                        if neoSelect == i:
                            print ("found an item")
                            # Start using data from Object Logic and Arrays
                            
                            neoSelected[0] = neoSelect
                            input("Press enter to continue:")
                            stopSelect = False
                        elif neoSelect == str('quit'):
                            stopSelect = False
            case '3':
                # Select from various charts
                os.system('cls')
                objectSelected = True
                while objectSelected == True:
                    if neoSelected == ['Init']:
                        print("Please select a NEO before accessing this option")
                        objectSelected = False
                    elif neoSelected != ['Init']:
                        print ("Please Select a chart:")
                        print ("1: Acceleration over time\n 2: Dates observed over time\n 3: Five closest encounters")
            case '4':
                print("Goodbye.")
                keepGoing = False
            case _:
                print ('Please select an option by the number assgned to it.')
        
menu()