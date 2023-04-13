import DictionaryInit as Dict
import numpy as py

def neoName(objectName):
    # Iterate all names in NEO API to create a list of all items
    objectName = []
    for i in Dict.CE_dict['near_earth_objects']:
        objectName.append(i.get('name_limited'))
    return objectName

def neoDiameterMax(objectSizeMax):
    # Iterate all diameters for all Near Earth Objects
    objectSizeMax = []
    for i in Dict.CE_dict['near_earth_objects']:
        try:
            for j in i['estimated_diameter']['meters']:              
                if j == 'estimated_diameter_max':
                    objectSizeMax.append([i["name_limited"], i['estimated_diameter']['meters'][j]])
        except IndexError:
            break
    return objectSizeMax

def neoDiameterMin(objectSizeMin):
    # Iterate all diameters for all Near Earth Objects
    objectSizeMin = []
    for i in Dict.CE_dict['near_earth_objects']:
        try:
            for j in i['estimated_diameter']['meters']:
                if j == 'estimated_diameter_min':
                    objectSizeMin.append([i["name_limited"], i['estimated_diameter']['meters'][j]])               
        except IndexError:
            break
    return objectSizeMin

def neoMissDistance(missDistance):
    # Create an array that includes the Name, date, and lunar distance of each NEO's miss distance
    missDistance = []
    for i in Dict.CE_dict['near_earth_objects']:
        for j in i['close_approach_data']:
            for k in j['miss_distance']:
                if k == 'lunar':
                    missDistance.append([i["name_limited"], j["close_approach_date"], j['miss_distance'][k]])
    return missDistance

def hazardousNEOS(isNEOHazardous):
    # Create 2 lists for Hazardous and Non-Hazardous Near Earth Objects
    isNEOHazardous = []
    for i in Dict.CE_dict['near_earth_objects']:
        isNEOHazardous.append([i.get('name_limited'), i.get('is_potentially_hazardous_asteroid')])
    return isNEOHazardous

def neoMagnitude(absoluteMagnitude):
    #Find the Absolute Magnitudes of all NEOs
    absoluteMagnitude=[]
    for i in Dict.CE_dict['near_earth_objects']:
        absoluteMagnitude.append([i.get('name_limited'), i.get('absolute_magnitude_h')])
    return absoluteMagnitude
        
def firstObservation(firstObserved):
    # Find the first observed dates for all NEOs
    firstObserved = []
    for i in Dict.CE_dict['near_earth_objects']:
        for j in i ['orbital_data']['first_observation_date']:
            firstObserved.append([i.get('name_limited'), str(i['orbital_data']['first_observation_date'])])
    return firstObserved

def neoEncounterDates(neoEncounters):
    # Find all close approach dates for every NEO
    neoEncounters = []
    for i in Dict.CE_dict['near_earth_objects']:
        for j in i["close_approach_data"]:
            neoEncounters.append([i.get('name_limited'), j["close_approach_date"], float(j['miss_distance']['lunar'])])
    return neoEncounters

def neoRelativeVelocity(relativeVelocity):
    # find the velocity of every NEO relative to earth and include the dates as well
    relativeVelocity = []
    for i in Dict.CE_dict['near_earth_objects']:
        for j in i['close_approach_data']:
            relativeVelocity.append([i.get('name_limited'), j['relative_velocity']['kilometers_per_hour'], j['close_approach_date']])
    return relativeVelocity