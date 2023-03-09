from tkinter import *
from tkinter import ttk
import ObjectArrays as Arrays
import ObjectLogic as Logic

# Create Menu Screen
top = Tk()
top.geometry('500x300')
top.title('Near Earth Object Web Service (NeoWs) Query')

# Creates a menu that will be used later
menubar = Menu(top)
top.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)
menubar.add_command(label='About')
file_menu.add_command(label='Diameters')
file_menu.add_command(label='Close Encounters')
menubar.add_cascade(label='Graphs',menu=file_menu,)

# Declare options from all names in Dictionary
listItems = Arrays.neoName()
clicked = StringVar()

# Declare sizes of all NEOs
sizeMin = 0
sizeMax = 0
#avgDiameter = ObjectLogic.averageDiameter(sizeMin, sizeMax)

# Create all visual items on application
title = Label(top, text="NASA Close Encounter Query").pack()
combo = ttk.Combobox(top, values= listItems).pack()

#These widgets disappear after an item is selected and reappear after nothing is selected
minAvgDiameter = Label(top, text="Average Min Diameter: " + str(sizeMin)).pack()
maxAvgDiameter = Label(top, text="Average Max Diameter: " + str(sizeMax)).pack()

# Creating all the data i want to pull per request, data will by default be hidden
minDiameter = Label(top, text="Min Diameter (meters): " + str(sizeMin)).grid_forget()
maxDiameter = Label(top, text="Max Diameter (meters): " + str(sizeMax)).grid_forget()
firstObservation = Label(top, text="First observed in : " + str(sizeMax)).grid_forget()
neoMagnitude = Label(top, text="Magnitude: " +str(sizeMax)).grid_forget()
nextApproachDate = Label(top, text="Next approach Date: " + str(sizeMax)).grid_forget()
nearestMiss = Label(top, text="The nearest miss for this NEO was in " + str(sizeMax) + " by "+ str(sizeMax) + " Kilometers").pack_forget() # Date and then distance

# Toggle the text to appear when anything is entered through the combobox
def toggleLabels():
    pass
def comboUpdate():
    if combo.get() != "":
        minAvgDiameter.pack_forget()
        maxAvgDiameter.grid_forget()
        
# I found that you can create a default Canvas of Grids, could be useful, might include it for graphs.

# Execute application
top.mainloop()