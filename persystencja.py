class DataFromAirVisual:
    def __init__(self):
        self.database = []

    def add_data(self, data):
        self.database.append(data)

    def get_data(self):
        return self.database

    def print_data(self):
        for data in self.database:
            print(data)
