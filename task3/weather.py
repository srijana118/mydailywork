import requests

API_KEY = "00e71b1fc57250b5081d13f6d58cca89"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Step 1: User input
city = input("Enter city name or zip code: ")

# Step 2: API request
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)

# Step 3: Parse response
if response.status_code == 200:
    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]

    # Step 4: Display output
    print("\n🌦️ Weather Forecast")
    print(f"📍 Location: {data['name']}")
    print(f"🌡️ Temperature: {temperature}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"🌬️ Wind Speed: {wind_speed} m/s")
    print(f"☁️ Condition: {description.capitalize()}")

else:
    print("❌ City not found or invalid input")
