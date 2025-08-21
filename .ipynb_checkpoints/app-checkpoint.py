import streamlit as st
import pandas as pd
import joblib

# Load trained model pipeline (includes preprocessing + model)
model = joblib.load("housing_model.pkl")

st.set_page_config(page_title="🏡 House Price Prediction", layout="centered")

st.title("🏡 House Price Prediction App")
st.write("This app predicts the price of a house based on its features.")

# Collect user inputs
st.subheader("Enter House Features")

area = st.number_input("Area (sq ft)", min_value=100, max_value=10000, value=1500)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
stories = st.number_input("Number of Stories", min_value=1, max_value=5, value=1)

mainroad = st.selectbox("Main Road", ["yes", "no"])
guestroom = st.selectbox("Guest Room", ["yes", "no"])
basement = st.selectbox("Basement", ["yes", "no"])
hotwaterheating = st.selectbox("Hot Water Heating", ["yes", "no"])
airconditioning = st.selectbox("Air Conditioning", ["yes", "no"])
prefarea = st.selectbox("Preferred Area", ["yes", "no"])

parking = st.number_input("Parking Spaces", min_value=0, max_value=5, value=1)
furnishingstatus = st.selectbox("Furnishing Status", ["furnished", "semi-furnished", "unfurnished"])

# ✅ Input DataFrame with exact same feature names used during training
input_data = pd.DataFrame({
    "area": [area],
    "bedrooms": [bedrooms],
    "bathrooms": [bathrooms],
    "stories": [stories],
    "mainroad": [mainroad],
    "guestroom": [guestroom],
    "basement": [basement],
    "hotwaterheating": [hotwaterheating],
    "airconditioning": [airconditioning],
    "parking": [parking],
    "furnishingstatus": [furnishingstatus],
    "prefarea": [prefarea]
})

# Predict
if st.button("Predict House Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated House Price: **${prediction:,.2f}**")
