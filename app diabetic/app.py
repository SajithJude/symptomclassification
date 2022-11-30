from matplotlib.pyplot import step
from numpy import result_type
import streamlit as st
import requests
from PIL import Image

# diabetes explanation
st.title("Diabetes Disease Prediction")
img = Image.open('Diabetic.jpg')
st.image(img, width=400, use_column_width=True)
st.subheader('           ')
st.subheader('What is Diabetes?')
st.markdown('According to WHO, Diabetes is a chronic, metabolic disease characterized by elevated levels of blood glucose (or blood sugar), which leads over time to serious damage to the heart, blood vessels, eyes, kidneys and nerves. The most common is type 2 diabetes, usually in adults, which occurs when the body becomes resistant to insulin or doesn`t make enough insulin. In the past three decades the prevalence of type 2 diabetes has risen dramatically in countries of all income levels. Type 1 diabetes, once known as juvenile diabetes or insulin-dependent diabetes, is a chronic condition in which the pancreas produces little or no insulin by itself. For people living with diabetes, access to affordable treatment, including insulin, is critical to their survival. There is a globally agreed target to halt the rise in diabetes and obesity by 2025.') 
img1 = Image.open('422milliondiabetes.jpg')
st.image(img1, width=250, use_column_width=True)
st.markdown('About 422 million people worldwide have diabetes, the majority living in low-and middle-income countries, and 1.5 million deaths are directly attributed to diabetes each year. Both the number of cases and the prevalence of diabetes have been steadily increasing over the past few decades.')
st.subheader('           ')
st.header('Diabetes diagnostics for women aged at least 21 years of Indian Pima descent')
st.subheader('Check Yourself Is Diabetic or Healthy!!')

# Pima Indians Diabetes Database
# Predict the onset of diabetes based on diagnostic measures
Name = st.text_input("Name:")
Pregnancies = st.number_input("Number of times pregnant :")
Glucose = st.number_input("Plasma glucose tolerant Concentration (mg/dL):")
BloodPressure =  st.number_input("Diastolic blood pressure (mm/Hg):")
SkinThickness = st.number_input("Triceps skin fold thickness (mm):")
Insulin = st.number_input("After 2-hour use of insulin serum (mu U/ml):")
BMI = st.number_input("Body mass index (weight in kg/(height in m)^2):")
DiabetesPedigreeFunction = st.number_input("Diabetes due to genetics:")
Age = st.number_input("Age:",min_value=21,max_value=81,step=1)
submit = st.button('Predict')

# inference
data = { 'Name' : Name,
        'Pregnancies' : Pregnancies,
        'Glucose' : Glucose,
        'BloodPressure' : BloodPressure,
        'SkinThickness' : SkinThickness,
        'Insulin' : Insulin,
        'BMI': BMI,
        'DiabetesPedigreeFunction' :DiabetesPedigreeFunction,
        'Age': Age}

# URL = "http://127.0.0.1:5000/diabetic_prediction" # sebelum push backend
URL = "https://diabeticmilestone.herokuapp.com/diabetes_prediction" # URL Heroku

# communication
r = requests.post(URL, json=data)
res = r.json()

if r.status_code == 200:
    if submit:
        prediction = res['result']['label_name']
        if prediction == "Not Diabetic":
            st.write('Congratulation',Name,'You are not Diabetes')
        else:
            st.write(Name," we are really sorry to say but it seems like you are Diabetes")
else:
    st.title("ERROR BOSS")
    st.write(res['message'])
