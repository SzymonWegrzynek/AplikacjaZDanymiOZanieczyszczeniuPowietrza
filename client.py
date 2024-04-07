import requests


class AirVisualClient:
    def __init__(self):
        self.api_key = "873dffac-2098-49b7-b803-d3ccd5dae470"
        self.basic_url = "https://api.airvisual.com/v2/"

    def get_air_quality(self):
        url = f"{self.basic_url}city?city=Warsaw&state=Mazovia&country=Poland&key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return data
