import requests
import os

# https://developers.google.com/maps/documentation/distance-matrix/distance-matrix

"""
Do not forget to add the API key as environment variable bore running this module!

Windows CMD:
- set API_KEY=123
- echo %API_KEY%

IntelliJ IDEA
- go to "Run/Edit Configurations/Python"
- setup .py as script file and define environment variable API_KEY=123
"""

api_key = os.getenv("API_KEY")

input_start = "Mannheim"
input_destination = "Mainz"

api_url = (f"https://maps.googleapis.com/maps/api/distancematrix/json?"
           f"origins={input_start}&"
           f"destinations={input_destination}&"
           f"mode=driving&"
# next line enables real time traffic information 
#           f"departure_time=now&"
           f"key={api_key}"
)

response = requests.get(api_url)
print(response)
data = response.json()
print(data)

if response.status_code == 200 and data["status"] == "OK":

    origin_address = data["origin_addresses"][0]
    destination_address = data["destination_addresses"][0]

    route_calculation = data["rows"][0]["elements"][0]
    distance = route_calculation["distance"]
    distance_in_km = distance["value"]/1000
    duration = route_calculation["duration"]
    duration_in_min = duration["value"]/60

    print("It takes "+duration["text"]+" and "+distance["text"]+" to travel from "+origin_address+" to "+destination_address+".")

else:

    print("Error:", response.status_code)
    print(response.text)
