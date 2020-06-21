
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








    

