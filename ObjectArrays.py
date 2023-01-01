import DictionaryInit as Dict

def neoName():
    # Iterate all names in NEO API to create a list of all items
    objectName = []
    for designation in Dict.CE_dict['near_earth_objects']:
        objectName.append(designation.get('name_limited'))
    return objectName

def neoDiameter():
    #Iterate all Diameters for all objects and then find the average diameter of all NEOs
    objectSizeMin = []
    objectSizeMax = []
    for estimated_diameter in Dict.CE_dict['near_earth_objects']:
        for meters in estimated_diameter:
            try:
                objectSizeMax.append(meters.get('estimated_diameter_min'))
                objectSizeMin.append(meters.get('estimated_diameter_max'))
                print(objectSizeMax, objectSizeMin)
                return objectSizeMin, objectSizeMax
            except:
                print("Diameter Data could not be found, try again")
                return objectSizeMin, objectSizeMax

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