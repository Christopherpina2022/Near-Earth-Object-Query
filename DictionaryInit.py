import requests
import urllib3
import os

# Create a get request for the browse feature in the NASA NeoWs API
http = urllib3.PoolManager()
neoBrowse = requests.get('https://api.nasa.gov/neo/rest/v1/neo/browse?api_key='+ os.getenv('API_KEY'))

# Define a data Dictionary with parsed information
CE_dict = neoBrowse.json()