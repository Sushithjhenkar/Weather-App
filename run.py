from flask import Flask, render_template, request

import requests

app = Flask(__name__)

API_KEY = '9c1df31231e04ea57f0f732b33e8f072'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form['city']
        weather_data = get_weather_data(city_name)
        return render_template('index.html', city=city_name, weather_data=weather_data)
    return render_template('index.html', city=None, weather_data=None)

def get_weather_data(city_name):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'

    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
    else:
        return f"Error {response.status_code}: Unable to retrieve weather data for {city_name}. Please check the city name."

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='127.0.0.1', port=5000)
