import streamlit as st
import pandas as pd
import numpy as np
import pickle as pk

regressor = pk.load(open("regressor.pkl","rb"))
scaler = pk.load(open("scaler.pkl","rb"))

st.header(" Diabetes Prediction System")

gender = st.selectbox('What is your gender?', ['Male', 'Female', 'Other'])
age = st.slider('How old are you?', 0, 100)
hypertension = st.selectbox('Have you ever been diagnosed with hypertension (high blood pressure)?', ['Yes', 'No'])
heart_disease = st.selectbox('Have you ever been diagnosed with any kind of heart disease?', ['Yes', 'No'])
smoking_history = st.selectbox('What best describes your smoking history?', 
                               ['Never', 'No Info', 'Current', 'Former', 'Ever', 'Not Current'])
bmi = st.slider('What is your Body Mass Index (BMI)?', 10.00, 45.00)
HbA1c_level = st.slider('What is your HbA1c test result (average blood sugar level over the past 3 months)?', 3.01, 9.00)
blood_glucose_level = st.slider('What is your current blood glucose level (in mg/dL)?', 80.00, 300.00)


if gender == 'Male':
    gender_s = 1            
elif gender == 'Female':
    gender_s = 0
else:
    gender_s = 2

if hypertension == 'Yes':
    hypertension_s = 1
else:
    hypertension_s = 0

if heart_disease == 'Yes':
    heart_disease_s = 1
else:
    heart_disease_s = 0

if smoking_history == 'No Info':
    smoking_history_s = 0
elif smoking_history == 'Current':
    smoking_history_s = 1
elif smoking_history == 'Ever':
    smoking_history_s = 2
elif smoking_history == 'Former':
    smoking_history_s = 3
elif smoking_history == 'Never':
    smoking_history_s = 4
else:
    smoking_history_s = 5



if st.button("Predict"):
    pred_data = pd.DataFrame([[gender_s, age, hypertension_s, heart_disease_s, smoking_history_s,
                               bmi, HbA1c_level, blood_glucose_level]],
                             columns=['gender', 'age', 'hypertension', 'heart_disease', 'smoking_history',
                                      'bmi', 'HbA1c_level', 'blood_glucose_level'])

    pred_data = scaler.transform(pred_data)
    predict = regressor.predict(pred_data)

    if predict[0] == 1:
        st.markdown("🔴 High Risk of Diabetes Detected! 🔴")
        st.warning("⚠️ Please consult a medical professional immediately. This result indicates a high risk of diabetes. ⚠️")
    else:
        st.markdown("🟢 Low Risk / No Diabetes Detected 🟢")
        st.success("😅 Phew! You dodged the sugar bullet this time. But hey, maybe skip that extra donut and drink some water. Take care of your health! 💪🍎")
