import requests
import urllib3
import os
from dotenv import load_dotenv

# Create a get request for the browse feature in the NASA NeoWs API
load_dotenv()
http = urllib3.PoolManager()
neoBrowse = requests.get('https://api.nasa.gov/neo/rest/v1/neo/browse?api_key='+ os.getenv('API_KEY'))

# Define a data Dictionary with parsed information
CE_dict = neoBrowse.json()