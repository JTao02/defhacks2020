from functions import get_file_contents
import requests
import json

access_key = get_file_contents('ip_api_key.txt')
url = 'http://api.ipapi.com/api/161.185.160.93' + '?access_key=' + access_key
payload = {}
headers = {
  'Cookie': '__cfduid=dbfeb8f7b0a9217826dae3c633396a53c1592773873'
}
response = requests.get(url, headers=headers, data = payload)
location = response.json()

def get_lat_long():
  return location['latitude'], location['longitude']

#print(response.text.encode('utf8'))