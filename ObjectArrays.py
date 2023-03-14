import DictionaryInit as Dict
import numpy as py



def neoName():
    # Iterate all names in NEO API to create a list of all items
    objectName = []
    for i in Dict.CE_dict['near_earth_objects']:
        objectName.append(i.get('name_limited'))
    return objectName

def neoDiameterMax(objectSizeMax):
    # Iterate all diameters for all Near Earth Objects, name is included to help identify the object a lot better and to
    # Assist in reducing the amount of times we need to run this script
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
    # Iterate all diameters for all Near Earth Objects, name is included to help identify the object a lot better and to
    # Assist in reducing the amount of times we need to run this script
    objectSizeMin = []
    for i in Dict.CE_dict['near_earth_objects']:
        try:
            for j in i['estimated_diameter']['meters']:
                if j == 'estimated_diameter_min':
                    objectSizeMin.append([i["name_limited"], i['estimated_diameter']['meters'][j]])               
        except IndexError:
            break
    return objectSizeMin

def neoMissDistance():
    # Create an array that includes the Name, date, and lunar distance of each NEO's miss distance
    missDistance = []
    for i in Dict.CE_dict['near_earth_objects']:
        for j in i['close_approach_data']:
            print (i['close_approach_data'])
            for k in j['miss_distance']:
                if k == 'lunar':
                    missDistance.append([i["name_limited"], j["close_approach_date"], j['miss_distance'][k]])
                    print([i["name_limited"], j["close_approach_date"], j['miss_distance'][k]])
    #print (missDistance)
    return missDistance

neoMissDistance()
# add additional information to see if we can look up the magnitude, relative velocity, is it dangerous,
# and maybe the link to more info about that NEO

def hazardousNEOS():
    # Create 2 lists for Hazardous and Non-Hazardous Near Earth Objects
    hazardousNEO = []
    nonHazardousNEO = []
    for i in Dict.CE_dict['near_earth_objects']:
        for j in i['is_potentially_hazardous_asteroid']:   
                print (j)  
                #nonHazardousNEO.append(i['name_limited'])
    print (hazardousNEO, nonHazardousNEO)
    
#hazardousNEOS()