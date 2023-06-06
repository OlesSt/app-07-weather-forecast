import streamlit as st
import plotly.express as px
from backend import get_data

try:
    st.title("Weather Forecast for next 5 days")
    place = st.text_input("Place: ")
    days = st.slider("Forecast days", min_value=1, max_value=5, help="Nubmer of days")
    option = st.selectbox("Select data to view", ("Temperature", "Sky"))
    st.subheader(f"{option} for the next {days} days in {place}")


    if place:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]

            temperatures_toCelsius = []
            for temp in temperatures:
                temp = int(temp) - 273.15
                temperatures_toCelsius.append(str(temp))

            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures_toCelsius, labels={"x" : "Date", "y" : "Temp (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png",
                      "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
            image_path = [images[condition] for condition in sky_condition]
            st.image(image_path, width=85)
except KeyError:
    st.title("Please enter the city name")



