import requests
import json

from decoder import *

class Route:
    def __init__(self, starting_point, arrival_point, costing):
        self.starting_point = starting_point
        self.arrival_point = arrival_point
        self.costing = costing
        self.json_data = {
            "locations":[
                {
                    "lat": self.starting_point[0],
                    "lon": self.starting_point[1]
                },
                {
                    "lat": self.arrival_point[0],
                    "lon": self.arrival_point[1]
                }
            ],
            "language": "fr-FR",
            "costing": self.costing,
            "directions_options": {"units": "km"}
        }

    def get_shortest_path(self):
        api_url = f"http://localhost:8002/route?json={str(self.json_data)}"

        api_url = api_url.replace("'", '"')

        reponse = requests.get(api_url)

        return json.loads(json.dumps(reponse.json(), indent=2))
    
result = Route(
    starting_point=[48.849442, 2.261198],
    arrival_point=[48.872787, 2.408092],
    costing="pedestrian"
).get_shortest_path()

print(result)

result = json.loads(result)
result = result["trip"]["legs"][0]["shape"]
print(decode(result))