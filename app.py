import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the saved model
model = joblib.load("best_model.pkl")

st.set_page_config(page_title="California Housing Price Predictor 🏠", layout="centered")

st.title("🏡 California Housing Price Predictor")
st.markdown("Enter values for each feature below to predict the median house value (in $100,000s).")

# Input fields
MedInc = st.number_input("Median Income (10k USD)", min_value=0.0, value=3.0, step=0.1)
HouseAge = st.number_input("House Age", min_value=1, value=20)
AveRooms = st.number_input("Average Rooms", min_value=0.0, value=5.0)
AveBedrms = st.number_input("Average Bedrooms", min_value=0.0, value=1.0)
Population = st.number_input("Population", min_value=0, value=1000)
AveOccup = st.number_input("Average Occupants", min_value=0.1, value=2.5)
Latitude = st.number_input("Latitude", min_value=32.0, max_value=42.0, value=34.0)
Longitude = st.number_input("Longitude", min_value=-124.0, max_value=-114.0, value=-118.0)

# Custom feature
rooms_per_household = AveRooms / AveOccup

# Prepare input as DataFrame
input_data = pd.DataFrame([{
    "MedInc": MedInc,
    "HouseAge": HouseAge,
    "AveRooms": AveRooms,
    "AveBedrms": AveBedrms,
    "Population": Population,
    "AveOccup": AveOccup,
    "Latitude": Latitude,
    "Longitude": Longitude,
    "rooms_per_household": rooms_per_household
}])

# Predict
if st.button("Predict House Price"):
    prediction = model.predict(input_data)
    st.success(f"🏠 Estimated Median House Price: **${prediction[0]*100000:,.2f}**")
