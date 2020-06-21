import requests
import json
import functions
#from YelpAI import get_my_key

business_id = 'c6QaDLAu9T3ge_DZ7w4Sig'
API_KEY = 'Zn549gr0o_ZPmOLCnqnO9p5_ykoXBj2pHMT6z81mFVkiyzZXHQ07t4xqAgncbcQwrRl2K58mKLCCD-ioiWXiNsnezGe1ufPm28XbSca2be5A6w7J5yFQGHtX06XuXnYx'
#API_KEY = get_my_key()
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}
PARAMETERS = {'term':'grocery',
              'limit': 50,
              'radius': 10000,
              'offset': 50,
              'location': 'Berkeley'}

response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)

business_data = response.json()

for biz in business_data['businesses']:
    print(biz['name'])




#ENDPOINT = 'https://api.yelp.com/v3/businesses/matches'

#business_data['businesses']['location']['address1']

#Dictionary mapping 
lines = {}
