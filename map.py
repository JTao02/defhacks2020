import folium
from decipher_api import get_coordinates

# create map object
m = folium.Map(location=[45.421532, -75.697189], zoom_start=12)

# generate map
m.save('map.html')