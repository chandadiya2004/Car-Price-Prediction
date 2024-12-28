import streamlit as st
import pandas as pd
import pickle
from datetime import datetime

# Load the trained pipeline model (which includes preprocessing)
with open("predict_car_price.pkl", 'rb') as file:
    model = pickle.load(file)

def predict_price(input_data):
    # Define the column names (these should match the columns used in your model)
    columns = ['car_brand', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'year']
    
    # Convert input to DataFrame (ensure the input matches model input format)
    input_dataframe = pd.DataFrame([input_data], columns=columns)
    
    # Make prediction using the model pipeline (which includes preprocessing)
    prediction = model.predict(input_dataframe)
    
    return round(prediction[0], 2)

# Define the Streamlit app
st.title("Car Price Prediction App")
st.write("Enter the details of the car to predict its selling price.")

# Input fields for car details
car_brand = st.selectbox("Select the Car Brand", ['Maruti', 'Hyundai', 'Datsun', 'Honda', 'Tata', 'Chevrolet',
                                                 'Toyota', 'Jaguar', 'Mercedes-Benz', 'Audi', 'Skoda', 'Jeep',
                                                 'BMW', 'Mahindra', 'Ford', 'Nissan', 'Renault', 'Fiat',
                                                 'Volkswagen', 'Volvo', 'Mitsubishi', 'Land', 'Daewoo', 'MG',
                                                 'Force', 'Isuzu', 'OpelCorsa', 'Ambassador', 'Kia'])

km_driven = st.number_input("Kilometers Driven:", min_value=0, max_value=500000, value=10000, step=100)

current_year = datetime.now().year
year = st.number_input("Car Manufacturing Year:", min_value=2000, max_value=current_year, value=2015)

fuel = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])

seller_type = st.selectbox("Seller Type", ['Individual', 'Dealer', 'Trustmark Dealer'])

transmission = st.selectbox("Transmission Type", ['Manual', 'Automatic'])

owner = st.selectbox("Owner Type", ['First Owner', 'Second Owner', 'Fourth & Above Owner', 
                                   'Third Owner', 'Test Drive Car'])

# Gather input data
input_data = [car_brand, km_driven, fuel, seller_type, transmission, owner, year]

# Predict button
if st.button("Predict Selling Price"):
    if km_driven < 0 or year < 2000 or year > current_year:
        st.error("Invalid input values! Please check again.")
    else:
        predicted_price = predict_price(input_data)
        st.success(f"Estimated Selling Price: ₹{predicted_price}")
