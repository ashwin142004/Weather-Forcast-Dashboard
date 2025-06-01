import streamlit as st 
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of days for the weather forecast")

option = st.selectbox(
    "Select Weather Type",
    ("Temperature", "Sky"),
    help="Choose the type of weather data you want to see"
)

st.subheader(f"Weather forecast for {place} for the next {days} days")

if place:
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            dates = [dict["dt_txt"] for dict in filtered_data]
            temperatures = [dict["main"]["temp"] - 273.15 for dict in filtered_data]  # Convert from Kelvin to Celsius

            filtered_data = [dict["main"]["temp"] for dict in filtered_data]
            figure = px.line(x = dates, y = temperatures, labels={'x': 'Date', 'y': "Temperature (°C)"},)
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", 
                    "Clouds": "images/cloud.png", 
                    "Rain": "images/rain.png", 
                    "Snow": "images/snow.png"}

            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions if condition in images]
            dates = [dict["dt_txt"] for dict in filtered_data]
            print(sky_conditions)
            st.image(image_paths, width=100, caption=dates)
    
    except KeyError as e:
        st.error("The place you entered is not valid. Please try again.")