

import streamlit as st
import requests


API_KEY = "00e71b1fc57250b5081d13f6d58cca89"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Weather Forecast App",
    page_icon="🌦️",
    layout="centered"
)

# ------------------ HEADER ------------------
st.markdown("<h1 style='text-align: center;'>🌦️ Weather Forecast Application</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Get real-time weather information instantly</p>", unsafe_allow_html=True)
st.divider()

# ------------------ SIDEBAR ------------------
st.sidebar.header("🔍 Search Weather")

input_type = st.sidebar.radio(
    "Search By",
    ["City Name", "PIN / ZIP Code"]
)

# City-based input
if input_type == "City Name":
    city = st.sidebar.text_input("City Name", placeholder="Eg: Bengaluru")
    country = st.sidebar.selectbox(
        "Country Code",
        ["IN", "US", "UK", "CA", "AU", "FR", "DE"],
        help="Select country for better accuracy"
    )

# PIN-based input
else:
    pin_code = st.sidebar.text_input("PIN / ZIP Code", placeholder="Eg: 560001")
    country = st.sidebar.selectbox(
        "Country Code",
        ["IN", "US"],
        help="Required for PIN / ZIP based search"
    )

get_weather = st.sidebar.button("🌤️ Get Weather")

# ------------------ MAIN LOGIC ------------------
if get_weather:
    with st.spinner("Fetching weather data..."):

        if input_type == "City Name":
            if city.strip() == "":
                st.warning("⚠️ Please enter a city name.")
                st.stop()

            params = {
                "q": f"{city},{country}",
                "appid": API_KEY,
                "units": "metric"
            }

        else:
            if pin_code.strip() == "":
                st.warning("⚠️ Please enter a valid PIN / ZIP code.")
                st.stop()

            params = {
                "zip": f"{pin_code},{country}",
                "appid": API_KEY,
                "units": "metric"
            }

        response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        description = data["weather"][0]["description"].capitalize()
        location = f"{data['name']}, {data['sys']['country']}"

        st.success("✅ Weather data retrieved successfully!")

        st.subheader(f"📍 {location}")
        st.write(f"☁️ **Condition:** {description}")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("🌡️ Temperature", f"{temperature} °C")

        with col2:
            st.metric("💧 Humidity", f"{humidity} %")

        with col3:
            st.metric("🌬️ Wind Speed", f"{wind_speed} m/s")

    else:
        st.error("❌ Weather data not found. Please check your input.")

# ------------------ FOOTER ------------------
st.divider()
st.markdown(
    "<p style='text-align: center; font-size: 13px;'>Built with ❤️ using Python & Streamlit</p>",
    unsafe_allow_html=True
)
