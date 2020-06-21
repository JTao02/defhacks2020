import requests
from get_api_key import get_file_contents
from decipher_api import *
# Business Search - https://api.yelp.com/v3/businesses/search
#

# define a business ID
business_id = 'zZ-ytyY5R_KGk1tJCE2f2g'

API_KEY = get_file_contents('apikey')
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

# define the parameters
PARAMETERS = {'term': 'Starbucks',
              'limit': 50,
              'offset': 50,
              'radius': 40000,
              'location': 'Ottawa'}

# FULL LIST
'''
PARAMETERS = {'term': 'good food',
              'location': 'San Diego',
              'radius': 10000,
              'categories': 'bars,french',
              'locales': 'en_US',
              'limit': 50,
              'offset': 150,
              'sort_by': 'best_match',
              'price': '1',
              'open_now': True,
              'attributes': 'hot_and_new'
              }
'''

# make a request to the yelp API
response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)

business_data = response.json()

print(get_location(business_data))

