from tkinter import *
import ObjectArrays as Arrays
import ObjectLogic as Logic

# Create Menu Screen
top = Tk()
top.geometry('500x300')
top.title('Near Earth Object Web Service (NeoWs) Query')

# Declare options from all names in Dictionary
listItems = Arrays.neoName()
clicked = StringVar()

# Declare sizes of all NEOs
sizeMin = 0
sizeMax = 0
#avgDiameter = ObjectLogic.averageDiameter(sizeMin, sizeMax)

# Create all visual items on application
title = Label(top, text="NASA Close Encounter Query").pack()
encounterRequest = Label(top, text="Find an encounter: ").pack()
drop = OptionMenu(top, clicked, *listItems).pack()
minAvgDiameter = Label(top, text="Average Min Diameter: " + str(sizeMin)).pack()
maxAvgDiameter = Label(top, text="Average Max Diameter: " + str(sizeMax)).pack()
# nextCE = Label(top, text="Next Close Encounter: "+ str(??).pack())

# Execute application
top.mainloop()