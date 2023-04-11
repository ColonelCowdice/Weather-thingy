# Silly Weather

## Imports
import requests

## Key
api_key = "253682c0bd759acfb4255d4aa08c3dd7"  # Replace with your OpenWeatherMap API key

# Letter by letter

def p(string):
    for char in string:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print("")



# Function 1

# Searches City from input
def get_weather_data(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

# Function 2

# Harvests Weather data
def print_weather_data(weather_data):
    weather = weather_data["weather"][0]["main"]

    # Temperature
    temperature = round(weather_data["main"]["temp"] - 273.15, 2)  # Convert from Kelvin to Celsius
    # Humidity
    humidity = weather_data["main"]["humidity"]
    # Wind speed
    wind_speed = weather_data["wind"]["speed"]

# Communication
    p(f"The weather in {weather_data['name']} is {weather}.")
    p(f"The temperature is {temperature}°C.")
    p(f"The humidity is {humidity}%.")
    p(f"The wind speed is {wind_speed} m/s.")

# Input
city_name = input("Enter the name of the city: ")
weather_data = get_weather_data(city_name)
if weather_data["cod"] == 200:
    print_weather_data(weather_data)
else:
    p("Sorry, we couldn't find that city.")
