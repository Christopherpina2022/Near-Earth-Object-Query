# Near-Earth-Object-Query
Uses the NeoWs API from NASA to show information about Near Earth Objects. Was originally purposed to learn how to work with APIs.

## Installation
After cloning the repo, you will need to add a .env file and enter in your API key as described in the below documentation. Afterwards, you will
then execute the **RepoInit.ps1** Powershell file in the root folder which will automatically build your Virtual environment and install all
dependencies; do note that the environment will not build and leave a warning redirecting to this README if it does not find the .env file.

## Getting the NASA API Key
to recieve your API key to use this application, go to https://api.nasa.gov/ and fill out the form requesting your full 
name and Email (the reason for the key is optional). the API this app uses on NASA's site is called Asteroids NeoWs. 
the Dictionary init python script will automatically find your key if you name your .env variable:

```
API_KEY = {Your API here}.
```