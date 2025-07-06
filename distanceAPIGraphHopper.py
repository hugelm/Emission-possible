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

def get_distance_and_duration(input_start, input_destination, input_vehicle, api_key=api_key):

    input_start = geocode_address(input_start)
    input_destination = geocode_address(input_destination)

    api_url = (f"https://graphhopper.com/api/1/route?"
               f"point={input_start}&"
               f"point={input_destination}&"
               f"profile={input_vehicle}&"
               f"instructions=false&"
               f"key={api_key}"
               )

    response = requests.get(api_url)
    data = response.json()

    if response.status_code == 200:

        data = response.json()
        route = data["paths"][0]
        distance_m = route["distance"]  # meters
        duration_ms = route["time"]     # milliseconds

        distance_km = distance_m / 1000
        duration_min = duration_ms / 1000 / 60

        return distance_km, duration_min, "success"

    else:

        return None, None, response.text