from tkinter import *
from tkinter import ttk
import ObjectArrays as Arrays
import ObjectLogic as Logic
from ObjectLogic import *

# Create Menu Screen
top = Tk()
top.geometry('500x300')
top.title('Near Earth Object Web Service (NeoWs) Query')
menubar = Menu(top)
top.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)
menubar.add_command(label='About')
file_menu.add_command(label='Absolute Magnitude of NEOs by diameters(Min)')
file_menu.add_command(label='Absolute Magnitude of NEOs by diameters(Max)')
file_menu.add_command(label='Miss Distance of NEOs by date')
file_menu.add_command(label='Acceleration of NEOs by date')
menubar.add_cascade(label='Graphs',menu=file_menu,)

# Retrieve all the data needed to output to UI
listItems = Arrays.neoName()
clicked = StringVar()
avgDiameter = averageDiameter(avgDiameter=[])

# Create all visual items on application
displayFrame= Frame(top, borderwidth=5, relief=RIDGE, width=250, height=100)
title = Label(top, text="NASA Close Encounter Query")
combo = ttk.Combobox(top, values= listItems)
minAvgDiameter = Label(top, text="Average Min Diameter: " + str(avgDiameter[0]) + " Meters")
maxAvgDiameter = Label(top, text="Average Max Diameter: " + str(avgDiameter[1]) + " Meters")
currentTime = Label(top, text ="It is currently " + str(datetime.now()) + ".")
closestMiss = Label(top, text="The closest Object to miss the earth was "+ '' + ' by ' + '' + 'Lunar Units (400k Kilometers/Unit)')
minDiameter = Label(top, text="Min Diameter (meters): " + '')
maxDiameter = Label(top, text="Max Diameter (meters): " + '')
firstObservation = Label(top, text="First observed in : " + '')
neoMagnitude = Label(top, text="Magnitude: " )
nextApproachDate = Label(top, text="Next approach Date: " )
nearestMiss = Label(top, text="The nearest miss for this NEO was in "   " Kilometers") # Date and then distance
confirmButton = Button(top, text="Enter")
# I found that you can create a default Canvas of Grids, could be useful, might include it for graphs.

# Position all the widgets for this app
displayFrame.grid(column=0, row=0)
title.grid(column=1, row=0, sticky=NW)
combo.grid(column=1, row=1, columnspan=2)
minAvgDiameter.grid(column=0, row=0)
maxAvgDiameter.grid(column=0, row=0)
currentTime.grid(column=0, row=0)
confirmButton.grid(column=1, row=1)
closestMiss.grid_forget()
minDiameter.grid_forget()
maxDiameter.grid_forget()
firstObservation.grid_forget()
neoMagnitude.grid_forget()
nextApproachDate.grid_forget()
nearestMiss.grid_forget()

# Execute application
top.mainloop()