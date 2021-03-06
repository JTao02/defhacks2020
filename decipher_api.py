# print out info in better way
def unpack_api(business_data):

    for biz in business_data['businesses']:
        print("NAME " + biz['name'])
        print("Rating " + str(biz['rating']))
        print("Phone " + str(biz['phone']))
        print("ID " + biz['id'])
        print("is_closed " + str(biz['is_closed']))
        print("Distance " + str(biz['distance']))
        print("Coordinates " + str(biz['coordinates']))
        print("Location " + str(biz['location']))
        print("\n\n")

# key = business name, value = coordinates
def assign_business_coordinates(business_data):
    results = {}
    for biz in business_data['businesses']:
        results[biz['name']] = biz['coordinates']
    return results


def get_names(business_data):
    results=[]
    for biz in business_data['businesses']:
        results.append(biz['name'])
    return results 

def get_ratings(business_data):
    results=[]
    for biz in business_data['businesses']:
        results.append(biz['rating'])
    return results 

def get_phonenums(business_data):
    results=[]
    for biz in business_data['businesses']:
        results.append(biz['phone'])
    return results 

def get_isclosed(business_data):
    results=[]
    for biz in business_data['businesses']:
        results.append(biz['is_closed'])
    return results 

def get_coordinates(business_data):
    results=[]
    for biz in business_data['businesses']:
        results.append(biz['coordinates'])
    return results 

def get_distance(business_data):
    results=[]
    for biz in business_data['businesses']:
        results.append(biz['distance'])
    return results 

def get_location(business_data):
    results=[]
    for biz in business_data['businesses']:
        results.append(biz['location'])
    return results 

def get_addresses(business_data):
    results=[]
    for biz in business_data['businesses']:
        current = biz['location'] #current is dictionary
        results.append(current['address1'])
    return results

def get_latitude_list(business_data):
    results=[]
    for biz in business_data['businesses']:
        current = biz['coordinates'] #current is dictionary
        results.append(current['latitude'])
    return results

def get_longitude_list(business_data):
    results=[]
    for biz in business_data['businesses']:
        current = biz['coordinates'] #current is dictionary
        results.append(current['longitude'])
    return results

def get_region_latitude(business_data):
    return business_data['region']['center']['latitude']

def get_region_longitude(business_data):
    return business_data['region']['center']['longitude']

def get_aliases(business_data):
    result=[]
    for biz in business_data['businesses']:
         current = biz['categories'] #current is list of one dict
         result.append(current[0]['alias'])
    return result

def get_unique_aliases(business_data):
    result=[]
    for biz in business_data['businesses']:
        current = biz['categories'] #current is list of one dict
        if current not in result:
            result.append(current[0]['alias'])
    return result
