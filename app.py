import streamlit as st
from PIL import Image

def convert_units(category, value, from_unit, to_unit):
    conversions = {
        "Length": {"Kilometers": 1, "Miles": 0.621371, "Meters": 1000, "Feet": 3280.84},
        "Weight": {"Kilograms": 1, "Pounds": 2.20462, "Grams": 1000, "Ounces": 35.274},
        "Temperature": {"Celsius": 1, "Fahrenheit": lambda c: (c * 9/5) + 32, "Kelvin": lambda c: c + 273.15}
    }
    
    if category == "Temperature":
        return conversions[category][to_unit](value) if callable(conversions[category][to_unit]) else value
    else:
        return value * (conversions[category][to_unit] / conversions[category][from_unit])

# Streamlit UI
st.set_page_config(page_title="Pro Unit Converter", page_icon="⚡", layout="centered")
st.title("🌍 Professional Unit Converter")
st.markdown("Convert between different units with ease!")

# Categories
category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])

# Units
units = list({"Length": ["Kilometers", "Miles", "Meters", "Feet"],
              "Weight": ["Kilograms", "Pounds", "Grams", "Ounces"],
              "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]}[category])

from_unit = st.selectbox("From", units)
to_unit = st.selectbox("To", units)
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

if st.button("Convert 🔄"):
    result = convert_units(category, value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
