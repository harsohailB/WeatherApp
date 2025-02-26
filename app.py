# File Name: app.py
# Author: Harsohail Brar
# Date: Feb. 9, 2020

from flask import Flask, render_template, request, redirect, jsonify, url_for
from weather import Weather
import requests
import json

app = Flask(__name__)

# OpenWeather API 
API_KEY = "7bfff787fb67367678448aea34738ae9"

# Parses json and creates the Weather object 
def createWeather(json):
    location = json['name'] + ", " + json['sys']['country']
    temperature = json['main']['temp']
    humidity = json['main']['humidity']
    conditions = json['weather'][0]['description']
    weather = Weather(location, temperature, humidity, conditions)
    return weather

# Home Page
@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        country = request.form['country']

        if city is '' or country is '':
            city = 'london'
            country = 'GB'

        return redirect(url_for('result', city = city, country = country))
    else:
        return render_template('index.html')

# Result Page
@app.route('/result/<city>/<country>')
def result(city, country):
    print(city)
    api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "," +  country + "&appid=" + API_KEY       
    json = requests.get(api_link).json()
    weather = createWeather(json)
    return render_template('result.html', weather = weather)

# Debug Mode (updates page after each save)
if __name__ == "__main__":
    app.run(debug=True)