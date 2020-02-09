class Weather:

    def __init__(self, location, temperature, humidity, conditions):
        self.location = location
        self.temperature = round(temperature - 273, 2)
        self.humidity = humidity
        self.conditions = conditions