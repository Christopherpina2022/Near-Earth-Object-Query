import DictionaryInit as Dict
import numpy as py



def neoName():
    # Iterate all names in NEO API to create a list of all items
    objectName = []
    for i in Dict.CE_dict['near_earth_objects']:
        objectName.append(i.get('name_limited'))
    return objectName

def neoDiameter():
    # Iterate all diameters for all Near Earth Objects
    objectSizeMin = []
    objectSizeMax = []
    for i in Dict.CE_dict['near_earth_objects']:
        try:
            for j in i['estimated_diameter']['meters']:
                if j == 'estimated_diameter_min':
                    objectSizeMin.append(i['estimated_diameter']['meters'][j])
                if j == 'estimated_diameter_max':
                    objectSizeMax.append(i['estimated_diameter']['meters'][j])
        except IndexError:
            break
        return objectSizeMax, objectSizeMin

def neoTimes():
    # Create an array that includes the Name and Date of each NEO's expected CE's
    objectTime = []
    for name in Dict.CE_dict['near_earth_objects']:
        for close_approach_date in Dict.CE_dict['close_approach_data']:
            try:
                objectTime.append([name.get('name_limited'), close_approach_date.get('close_approach_date')])
                return objectTime
            except:
                print('Close Approach Data not available.')
                return objectTime

def neoMissDistance():
    # Create an array that includes the Name and Lunar distance of each NEO's miss distance
    missDistance = []
    for name in Dict.CE_dict['near_earth_objects']:
        for close_approach_data in Dict.CE_dict['near_earth_objects']:
            for miss_distance in close_approach_data:
                try:
                    missDistance.append([name.get('name_limited'), miss_distance.get('miss_distance')])
                except AttributeError:
                    print('Miss Distance not available.')
                    return missDistance