# Google maps API call

from pprint import pprint
import requests
import googlemaps
import gmaps
from googlemaps import convert

# Read api key:
api_key = "Haha No free Gmaps key for you :)"

map_client = googlemaps.Client(key = api_key)

myAddress = "Address"

response = map_client.geocode(myAddress)
pprint(response)
print("\n\n\n\n")
print(response[0]['geometry'])


