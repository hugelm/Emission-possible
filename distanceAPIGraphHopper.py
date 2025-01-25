import requests
import os

# Documentation: https://docs.graphhopper.com/openapi/routing/getroute
# Keys: https://graphhopper.com/dashboard/#/apikeys (500 requests per day)

api_key = os.getenv("API_KEY_GRAPHHOPPER")

def get_distance_and_duration(input_start, input_destination, api_key=api_key):

    # convert address to coordinates (geocoding with Nominatim API)
    geocoding_start = requests.get(f"https://nominatim.openstreetmap.org/search?q={input_start}&format=json&limit=1",
                                        headers = {"User-Agent": "MyGeocodingApp/1.0 (myemail@example.com)"}
                                        ).json()[0]
    geocoding_destination = requests.get(f"https://nominatim.openstreetmap.org/search?q={input_destination}&format=json&limit=1",
                                        headers = {"User-Agent": "MyGeocodingApp/1.0 (myemail@example.com)"}
                                        ).json()[0]
    input_start = str(geocoding_start["lat"])+","+str(geocoding_start["lon"])
    input_destination = str(geocoding_destination["lat"])+","+str(geocoding_destination["lon"])

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

        print("It takes "+str(round(duration_in_min,2))+"min and "+str(round(distance_in_km,2))+"km.")

    else:

        print(response.text)

get_distance_and_duration("Mainz", "Mannheim")