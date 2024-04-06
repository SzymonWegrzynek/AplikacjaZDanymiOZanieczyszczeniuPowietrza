import requests


class AirVisualClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.airvisual.com/v2/"

    def get_air_quality(self, city, state, country):
        url = f"{self.base_url}city?city={city}&state={state}&country={country}&key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return data


client = AirVisualClient("873dffac-2098-49b7-b803-d3ccd5dae470")
data = client.get_air_quality("Warsaw", "Mazovia", "Poland")
print(data)
