# 🌦️ Weather Forecast Application (Python)

This is a terminal-based Weather Forecast application developed using Python.  
The program fetches real-time weather data from an external API and displays it in a clear, user-friendly format.

## 📌 Description

The application prompts the user to enter a city name or zip code.  
Using this input, it sends a request to a weather API, retrieves the current weather data, and displays important weather details such as temperature, humidity, wind speed, and weather condition.

## ✨ Features

- Accepts user input (city name or zip code)
- Makes an API request to retrieve weather data
- Extracts and displays:
  - Temperature (°C)
  - Humidity (%)
  - Wind speed (m/s)
  - Weather condition description
- Displays output in a clean and readable terminal format

## 🛠 Technologies Used

- Python  
- Requests library  
- OpenWeatherMap API  

## ⚙️ How the Code Works

1. The user is prompted to enter a city name or zip code.
2. An API request is sent using the `requests` library.
3. The JSON response from the API is parsed.
4. Required weather details are extracted from the response.
5. The weather information is displayed in the terminal.
6. If the city or zip code is invalid, an error message is shown.

## 🚀 How to Run the Program

1. Install the required library:
   ```bash
   pip install requests
2. Save the code in a file (for example):
   ```bash
   weather_forecast.py

3. Run the program:
   ```bash
   python weather_forecast.py

4. Enter a valid city name or zip code when prompted
