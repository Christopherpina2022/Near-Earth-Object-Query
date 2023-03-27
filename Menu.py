from tkinter import *
from tkinter import ttk
import ObjectArrays as Arrays
import ObjectLogic as Logic
from ObjectLogic import *

# Create Root window
top = Tk()
top.geometry('850x400')
top.title('Near Earth Object Web Service (NeoWs) Query')

# Going to replace this file since it's kind of cluttered and horribly unoptimized
# Define event functions, these need to be at the top to be called by other items
def clearData():
    pass

def revealInfo(displayFrame, event):
    minAvgDiameter.grid_forget()
    maxAvgDiameter.grid_forget()
    closestMiss.grid(column=0, row=0)
    minDiameter.grid(column=0, row=1)
    maxDiameter.grid(column=0, row=2)
    firstObservation.grid(column=0, row=3)
    neoMagnitude.grid(column=0, row=4)
    nextApproachDate.grid(column=0, row=5)
    nearestMiss.grid(column=0, row=6)
    
def hideInfo(eventObject):
    minAvgDiameter.grid(column=0, row=0)
    maxAvgDiameter.grid(column=0, row=2)
    closestMiss.grid_forget()
    minDiameter.grid_forget()
    maxDiameter.grid_forget()
    firstObservation.grid_forget()
    neoMagnitude.grid_forget()
    nextApproachDate.grid_forget()
    nearestMiss.grid_forget()

# Create Menu
menubar = Menu(top)
top.config(menu=menubar)
graphMenu = Menu(menubar, tearoff=False)
absoMagnitudeGraphs = Menu(menubar, tearoff=False)

# Top level menu options
menubar.add_command(label='About')#, command=aboutTopLevel)
menubar.add_cascade(label='Graphs', menu=graphMenu)

def aboutTopLevel():
    # About Toplevel Widget
    aboutMenu = Toplevel()
    aboutMenu.geometry("300x150")
    aboutMenu.title('About')
    aboutText = Label(aboutMenu, text="This is a Program written using the NASA Near Earth Object Web Service and Python with Tkinter's UI.")
    aboutText.grid()

# Magnitude Menu items

absoMagnitudeGraphs.add_command(label='By name')
absoMagnitudeGraphs.add_command(label='By diameters(Min)')
absoMagnitudeGraphs.add_command(label='By diameters(Max)')

# Other Graphs
graphMenu.add_command(label='Acceleration of NEOs by date')
graphMenu.add_cascade(label='Magnitude of NEOS', menu=absoMagnitudeGraphs)
graphMenu.add_command(label='Miss Distance of NEOs by date')

# Retrieve all the data needed to output to UI
listItems = Arrays.neoName()
clicked = StringVar()
avgDiameter = averageDiameter(avgDiameter=[])
lowestCE = closestEncounter(lowestCE=[])

# Create all visual items on application
displayFrame= Frame(top, borderwidth=5, relief=RIDGE, width=300, height=150)

title = Label(top, text="NASA Close Encounter Query")
combo = ttk.Combobox(top, values= listItems, state='readonly')

currentTime = Label(top, text ="It is currently " + str(datetime.now()) + ".")

minAvgDiameter = Label(displayFrame, text="Average Min Diameter: " + str(avgDiameter[0]) + " Meters")
maxAvgDiameter = Label(displayFrame, text="Average Max Diameter: " + str(avgDiameter[1]) + " Meters")
closestMiss = Label(displayFrame, text="The closest Object to miss the earth was "+ lowestCE[0] +' by ' + lowestCE[2] + ' Lunar Units (400k Kilometers/Unit)')
minDiameter = Label(displayFrame, text="Min Diameter (meters): " + '')
maxDiameter = Label(displayFrame, text="Max Diameter (meters): " + '')
firstObservation = Label(displayFrame, text="First observed in : " + '')
neoMagnitude = Label(displayFrame, text="Magnitude: " )
nextApproachDate = Label(displayFrame, text="Next approach Date: " )
nearestMiss = Label(displayFrame, text="The nearest miss for this NEO was in "   " Kilometers") # Date and then distance


confirmButton = Button(top, text="Find Info about NEO", command=revealInfo(displayFrame, Event))
clearButton = Button(top, text="Clear input", command=clearData)

# Position all the widgets for this app
top.grid_columnconfigure(0, weight=3)
top.grid_columnconfigure(1, weight=1)

displayFrame.grid(column=0, row=0)
displayFrame.columnconfigure(0, weight=1)

title.grid(column=1, row=0, sticky=N)
combo.grid(column=1, row=0, sticky=S)
confirmButton.grid(column=1, row=1, sticky=W)
clearButton.grid(column=1, row=1, sticky=E)

minAvgDiameter.grid(column=0, row=0)
maxAvgDiameter.grid(column=0, row=2)
currentTime.grid(column=0, row=1)

# Execute application
top.mainloop()