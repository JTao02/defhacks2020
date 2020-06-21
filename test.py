import requests
import folium
from functions import get_file_contents
from decipher_api import *
# Business Search - https://api.yelp.com/v3/businesses/search
#

# define a business ID
business_id = 'zZ-ytyY5R_KGk1tJCE2f2g'

API_KEY = get_file_contents('apikey')
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

# define the parameters
PARAMETERS = {'limit': 50,
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

start_latitude = get_region_latitude(business_data)
start_longitude = get_region_longitude(business_data)

# create map object
m = folium.Map(location=[start_latitude, start_longitude], zoom_start=12)
tooltip = 'Click for more info'


latitude_list = get_latitude_list(business_data)
longitude_list = get_longitude_list(business_data)
address_list = get_addresses(business_data)
alias_list = get_aliases(business_data)
unique_alias_list = get_unique_aliases(business_data)

vegan_places=["vegan"]
coffee_places=["coffee","breakfast_brunch"]

folium.Marker([start_latitude, start_longitude],
                tooltip="You are here",
                icon=folium.Icon(color='red', icon='leaf')).add_to(m)


for i, e in enumerate(latitude_list):
    if alias_list[i] in vegan_places:
        color = "green"
    elif alias_list[i] in coffee_places:
        color = "black"
    else:
        color = "blue"
    folium.Marker([latitude_list[i],longitude_list[i]],
                popup=address_list[i],
                tooltip=tooltip,
                icon=folium.Icon(color=color, icon='leaf')).add_to(m)

# generate map
m.save('map.html')


