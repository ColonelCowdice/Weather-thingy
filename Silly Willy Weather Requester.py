# Fun Weather Forecast

# Required Libraries
import requests
import time

# API Configuration
api_key = "insert key here"

# Custom Print Function
def custom_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print("")

# Retrieve Weather Data
def fetch_weather_data(city):
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(api_url)
    weather_data = response.json()
    return weather_data

# Display Weather Data
def display_weather_info(weather_info):
    current_weather = weather_info["weather"][0]["main"]

    # Temperature (Kelvin to Celsius)
    temp_celsius = round(weather_info["main"]["temp"] - 273.15, 2)
    # Humidity
    humidity_percentage = weather_info["main"]["humidity"]
    # Wind Speed
    wind_speed_ms = weather_info["wind"]["speed"]

    # Output
    custom_print(f"The weather in {weather_info['name']} is {current_weather}.")
    custom_print(f"The temperature is {temp_celsius}°C.")
    custom_print(f"The humidity is {humidity_percentage}%.")
    custom_print(f"The wind speed is {wind_speed_ms} m/s.")

# User Input
city = input("Enter the name of the city: ")
retrieved_weather_data = fetch_weather_data(city)
if retrieved_weather_data["cod"] == 200:
    display_weather_info(retrieved_weather_data)
else:
    custom_print("Apologies, we couldn't find that city.")
