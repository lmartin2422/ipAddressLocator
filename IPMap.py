""" IP Address Locator"""

# run command on terminal: pip install geocode
# run command on terminal: pip install folium

import geocoder
import folium  # displays maps

g = geocoder.ip("me")  # my IP address
print("my ip location: ", g)

myAddress = g.latlng  # finds your latitude and longitude
print("lat & long: ", myAddress)

my_map1 = folium.Map(location=myAddress, zoom_start=12)  # shows my location on a map

# adds a circle for my location on the map
folium.CircleMarker(location=myAddress,
                    radius=50, popup="Baltimore").add_to(my_map1)


#  creates a blue marker for a more specific location indicator
folium.Marker(myAddress, popup="Baltimore").add_to(my_map1)

my_map1.save("my_map.html ")  # saves the map address to a html file

