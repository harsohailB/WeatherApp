# File Name: weather.py
# Author: Harsohail Brar
# Date: Feb. 9, 2020

# Weather class holds weather data for a specific location to be accessed 
# by result.html
class Weather:

    def __init__(self, location, temperature, humidity, conditions):
        self.location = location
        self.temperature = round(temperature - 273, 2)
        self.humidity = humidity
        self.conditions = conditions