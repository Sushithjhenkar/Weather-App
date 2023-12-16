import requests

API_KEY = '9c1df31231e04ea57f0f732b33e8f072'

while True:
    city_name = input("Enter city name: ")

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'

    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()

        # Extracting relevant information
        weather_description = weather_data['weather'][0]['description']
        temperature_kelvin = weather_data['main']['temp']

        # Converting temperature from Kelvin to Celsius
        temperature_celsius = temperature_kelvin - 273.15

        print(f"Weather in {city_name}: {weather_description}")
        print(f"Temperature: {temperature_celsius:.2f}°C")
    else:
        print(f"Error {response.status_code}: Unable to retrieve weather data for {city_name}. Please check the city name.")

print('sushith')