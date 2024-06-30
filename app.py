import pandas as pd
import numpy as np
import streamlit as st
import pickle as pk

model = pk.load(open('C:\Program Files\Python312\Heart Disease folder 2\Heart_disease_model.pkl','rb'))

data = pd.read_csv('C:\Program Files\Python312\Heart Disease folder 2\heart_disease.csv')

st.header('Heart Disease Predictor')

gender = st.selectbox('Choose Gender', data['Gender'].unique())
if gender== 'Male':
    gen = 1
else:
    gen = 0

age = st.number_input("Enter Age")
currentSmoker = st.number_input("Is Patient a smoker currently?")
cigsPerDay = st.number_input("Enter cigarettes per day")
BPMeds = st.number_input("Is Patient on BP Medication? (Enter 1 if yes and 0 if no)")
prevalentStroke = st.number_input("Does the patient have any history of stroke?")
prevalentHyp = st.number_input("Enter prevalentHyp status")
diabetes = st.number_input("Enter diabetes status")
totChol = st.number_input("Enter Cholesterol level")
sysBP = st.number_input("Enter systolic BP")
diaBP = st.number_input("Enter diastolic BP")
BMI = st.number_input("Enter BMI")
heartRate= st.number_input("Enter heartRate")
glucose = st.number_input("Enter glucose level")
if st.button('Predict'):
    input = np.array([[gen,age,currentSmoker,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,
                   totChol,sysBP,diaBP,BMI,heartRate,glucose]])
    output = model.predict(input)
    if output[0] == 0:
         stn = 'Patient is Healthy , No hert Disease'
    else:
         stn = 'Patient May have Heart Disese'
    st.markdown(stn)