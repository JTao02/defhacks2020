import requests
import folium
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

# create map object
m = folium.Map(location=[45.421532, -75.697189], zoom_start=12)
tooltip = 'Click for more info'

latitude_list = get_latitude_list(business_data)
longitude_list = get_longitude_list(business_data)
address_list = get_addresses(business_data)

for i, e in enumerate(latitude_list):
    folium.Marker([latitude_list[i],longitude_list[i]],
                popup=address_list[i],
                tooltip=tooltip,
                icon=folium.Icon(color='green', icon='leaf')).add_to(m)

# generate map
m.save('map.html')

