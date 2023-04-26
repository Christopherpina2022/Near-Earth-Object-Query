# Near-Earth-Object-Query
Uses the NeoWs API from NASA to show information about Near Earth Objects and other various information in a python GUI

There really isn't a purpose for this application, i'm just trying to learn APIs with the Nasa Near Earth Object Web Service since it was free to use.
I'm mainly just making an app with Tkinter's GUI to visualize data pulled straight out of the API and some other calculations that are dependent on the JSON file.

to recieve your API key to use this application, go to https://api.nasa.gov/ and fill out the form below which will generate your key. the API this
app uses on NASA's site is called Asteroids NeoWs. the Dictionary init python script will automatically find your key if you name your .env variable:
API_KEY = {Your API here}.

Packages used for this app: numpy, requests, urllib3, dotenv
The GUI build on the Test-Branch uses Tkinter and on later commits was replaced by PysimpleGui, but for now is a scrapped concept.