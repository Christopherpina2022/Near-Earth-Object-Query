# This version of the app implements a command line version of the program to help speed up the production of this app until
# I can fully understand a bit more of Front end development.
from getpass import getpass

def menu():
    menuList = [1,2,3]
    keepGoing = True
    print ('Near Earth objet Web Service Query (Command Line version) \nby Chris Pina\n')
    while keepGoing == True:  
        print ('1: List all Near Earth Objects \n2: lookup information about a Near Earth Object \n3: Lookup charts \n4:Quit application')
        optionSelect = input('Please enter an option: \n')
        # Basic validation loop
        match optionSelect:
            case '1':
                # Print out all names of NEOS in groups of Ten
                print ("you selected 1")
            case '2':
                # 
                print ("You selected 2")
            case '3':
                print ("You selected 3")
            case '4':
                print("Goodbye.")
                keepGoing = False
            case _:
                print ('Please select an option by the number assgned to it.')
        

menu()