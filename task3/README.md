🌦️ Weather Forecast Application (Python + Streamlit)

This is a **UI-based Weather Forecast application** developed using **Python and Streamlit**.  
The application fetches real-time weather data from an external API and presents it in a clean, interactive, and user-friendly interface.

📌 Description  
The application allows users to search for current weather information using either a **city name with country code** or a **PIN/ZIP code**.  
Based on the user’s input, the app sends a request to a weather API, retrieves real-time weather data, and displays key weather details such as temperature, humidity, wind speed, and weather conditions in a visually organized format.

✨ Features  
• Search weather by **City Name + Country Code**  
• Search weather by **PIN / ZIP Code**  
• Real-time weather data retrieval using an API  
• Displays:
  - Temperature (°C)  
  - Humidity (%)  
  - Wind speed (m/s)  
  - Weather condition description  
• Interactive UI built with Streamlit  
• Card-style layout for weather metrics  
• Soft background design for better user experience  
• Error handling for invalid inputs  

🛠 Technologies Used  
• Python  
• Streamlit  
• Requests library  
• OpenWeatherMap API  

⚙️ How the Application Works  
• The user selects the input type (City Name or PIN/ZIP Code).  
• The user enters the required details in the input panel.  
• An API request is sent using the requests library.  
• The JSON response from the API is parsed.  
• Required weather details are extracted from the response.  
• Weather information is displayed in an interactive UI with clear sections and metrics.  
• If the input is invalid, an appropriate error message is shown.

🚀 How to Run the Application  
1. Install the required libraries:
   pip install streamlit requests  

2. Save the code in a file (for example):
   weather.py  

3. Run the application:
   streamlit run weather.py  

4. The application will open automatically in your web browser.  
5. Enter a valid city name or PIN/ZIP code to view weather details.

🎓 Learning Outcome  
• Learned how to build interactive user interfaces using Streamlit  
• Gained experience in API integration and JSON data handling  
• Improved understanding of UI/UX design in Python applications  
• Worked with real-time external data sources  

📄 Note  
The API key used in this application should be kept private and should not be shared publicly.

📄 License  
This project is created for educational and learning purposes.
