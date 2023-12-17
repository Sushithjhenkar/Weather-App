from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '9c1df31231e04ea57f0f732b33e8f072'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form['city']
        weather_data = get_weather_data(city_name)
        time_data = get_time_data(city_name)
        return render_template('index.html', city=city_name, weather_data=weather_data, time_data=time_data)
    return render_template('index.html', city=None, weather_data=None, time_data=None)

def get_weather_data(city_name):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        weather_description = weather_data['weather'][0]['description']
        temperature_kelvin = weather_data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        return weather_data
    else:
        return None
def get_time_data(city_name):
    time_url = 'https://api.api-ninjas.com/v1/worldtime?city={}'.format(city_name)
    time_response = requests.get(time_url, headers={'X-Api-Key': 'ax637K4C0PDTdRQtSobr9g==3IC0TkpMYuu6GIB4'})
    if time_response.status_code == 200:
        time_data = time_response.json()
        return time_data
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='127.0.0.1', port=5000)
