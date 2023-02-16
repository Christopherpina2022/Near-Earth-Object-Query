import DictionaryInit as Dict
import numpy as py



def neoName():
    # Iterate all names in NEO API to create a list of all items
    objectName = []
    for i in Dict.CE_dict['near_earth_objects']:
        objectName.append(i.get('name_limited'))
    return objectName

def neoDiameter():
    # Iterate all diameters for all Near Earth Objects, name is included to help identify the object a lot better and to
    # Assist in reducing the amount of times we need to run this script
    objectSizeMin = []
    objectSizeMax = []
    for i in Dict.CE_dict['near_earth_objects']:
        try:
            for j in i['estimated_diameter']['meters']:
                if j == 'estimated_diameter_min':
                    objectSizeMin.append([i["name_limited"], i['estimated_diameter']['meters'][j]])
                if j == 'estimated_diameter_max':
                    objectSizeMax.append([i["name_limited"], i['estimated_diameter']['meters'][j]])
        except IndexError:
            break
    return objectSizeMax, objectSizeMin

def neoMissDistance():
    # Create an array that includes the Name, date, and lunar distance of each NEO's miss distance
    missDistance = []
    for i in Dict.CE_dict['near_earth_objects']:
        for j in i['close_approach_data']:
            for k in j['miss_distance']:
                if k == 'lunar':
                    missDistance.append([i["name_limited"], j["close_approach_date"], j['miss_distance'][k]])
    return missDistance

# add additional information to see if we can look up the magnitude, is it dangerous,
# and maybe the link to more info about that NEO