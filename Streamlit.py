import streamlit as st
import pandas as pd
import joblib
model = joblib.load("project_6.pkl")

st.title("Sales Prediction")

st.header("Enter Store Details")

Store = st.number_input("Store number")
Day_of_Week = st.number_input("Day of week",min_value = 0 , max_value=6)
Date = st.date_input("Date")
Open = st.number_input("shop opened_closed",min_value=0,max_value=1)
Promo = st.number_input("Prome code Applied",min_value=0, max_value=1)
State_Holiday=st.text_input("State holiday ")
School_Holiday = st.number_input("Scholl holiday ",min_value=0, max_value=1)
Dat = int(Date.strftime("%Y%m%d"))

if st.button('Predict'):
    input_data = pd.DataFrame([[Store,Day_of_Week,Dat,Open,Promo,State_Holiday,School_Holiday]],columns=["Store","Day_of_Week","Dat","Open","Promo","State_Holiday","School_Holiday"])
    predcition = model.predict(input_data)
