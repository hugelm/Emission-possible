import requests
import os
from geopy.geocoders import Nominatim

# Documentation: https://docs.graphhopper.com/openapi/routing/getroute
# Keys: https://graphhopper.com/dashboard/#/apikeys (500 requests per day)

api_key = os.getenv("API_KEY_GRAPHHOPPER")
geolocator = Nominatim(user_agent="EmissionPossible")

def geocode_address(address):
    location = geolocator.geocode(address)

    if location:
        return str(location.latitude)+","+str(location.longitude)
    else:
        print(f"Address {address} could not be geocoded.")

def get_distance_and_duration(input_start, input_destination, api_key=api_key):

    input_start = geocode_address(input_start)
    input_destination = geocode_address(input_destination)

    api_url = (f"https://graphhopper.com/api/1/route?"
               f"point={input_start}&"
               f"point={input_destination}&"
               f"profile=car&"
               f"instructions=false&"
               f"key={api_key}"
               )

    response = requests.get(api_url)
    data = response.json()

    if response.status_code == 200:

        route_calculation = data["paths"][0]
        distance = route_calculation["distance"]
        distance_in_km = distance/1000
        duration = route_calculation["time"]
        duration_in_min = duration/60/1000

        return "It takes "+str(round(duration_in_min,2))+"min and "+str(round(distance_in_km,2))+"km.", "success"

    else:

        return response.text, "danger"

#print(get_distance_and_duration("Mainz", "Mannheim"))