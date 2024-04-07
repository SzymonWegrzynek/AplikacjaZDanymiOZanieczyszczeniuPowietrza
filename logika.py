from client import AirVisualClient
from persystencja import DataFromAirVisual
from pydantic import ValidationError
from models import AirVisualModel


class GetDataFromClient:
    def __init__(self):
        self.client = AirVisualClient()
        self.database = DataFromAirVisual()

    def add_data_to_database(self):
        data = self.client.get_air_quality()
        try:
            validated_data = AirVisualModel(**data)
            self.database.add_data(validated_data.dict())
        except ValidationError as e:
            print(f"Data validation failed: {e}")


if __name__ == "__main__":
    GetDataFromClient().add_data_to_database()
