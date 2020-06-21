import requests
import json
from functions import get_file_contents
from database_funcs import *
from Location import get_lat_long

class Data:
    #Dictionary mapping location to current lines
    BUSINESS_ID = 'c6QaDLAu9T3ge_DZ7w4Sig'
    API_KEY = get_file_contents('yelp_api_key.txt')

    #Constructor method
    def __init__(self):
        pass

    @staticmethod
    #Getter method for lines
    def getLines(address):
        return getQueueETA(address)

    @staticmethod
    #Setting method for lines
    def setLines(address, queue, eta):
        entry = {"address" : address,
                 address : [queue, eta]
                }      
        updateDatabase(entry)

    @staticmethod
    #Allows user to filter their search.
    def search(keywords, radius, location):
        ''' 
        Radius is defaulted to 10000 m
        Location is defaulted to current location (when None)
        '''
        ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
        HEADERS = {'Authorization': 'bearer %s' % Data.API_KEY}
        if location == None:
            latitude, longitude = get_lat_long()
            #print(latitude, longitude)
            PARAMETERS = {'term': keywords,
              'limit': 20,
              'radius': radius,
              'latitude': latitude,
              'longitude': longitude}
        else:
            PARAMETERS = {'term': keywords,
                'limit': 20,
                'radius': radius,
                'location': location}

        response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)
        business_data = response.json()

        return business_data
        #for biz in business_data['businesses']:
        #    print(biz['name'])

