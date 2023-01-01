import json
import urllib3
import os
from dotenv import load_dotenv

# Creates the Data Dictionary that is called throughout the program.

# Create a get request for the browse feature in the NASA NeoWs API
load_dotenv()
http = urllib3.PoolManager()
NeoBrowse = http.request('GET', "https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=" + os.getenv('API_KEY'))

# Define a data Dictionary with decrypted JSON
CE_dict = json.loads(NeoBrowse.data.decode('UTF-8'))