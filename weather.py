class Weather:

    def __init__(self, location, temperature, humidity, conditions):
        self.location = location
        self.temperature = temperature - 273
        self.humidity = humidity
        self.conditions = conditions