import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open('model.pkl','rb'))

sex = ['Male','Female']

st.title('Check Your Hearts health')

col1, col2 = st.columns(2)

with col1:
    age = st.number_input('Age')

with col2:
    sex = st.selectbox('Select your gender',sorted(sex))

col3, col4, col5 = st.columns(3)

with col3:
    cp = st.number_input('constrictive pericarditis, range(0-3)')

with col4:
    trestbps = st.number_input('Resting Blood Pressure')

with col5:
    chol = st.number_input('cholesterol level')

col6, col7, col8 = st.columns(3)

with col6:
    fbs = st.number_input('Fasting Blood Sugar level')

with col7:
    restecg = st.number_input('Resting ECG')

with col8:
    thalach = st.number_input('max heart rate')

col9, col10, col11 = st.columns(3)

with col9:
    exang = st.number_input('exercise-induced angina')

with col10:
    oldpeak = st.number_input('ECG plot depression')

with col11:
    slope = st.number_input('ECG plot slope')

col12, col13 = st.columns(2)

with col12:
    ca = st.number_input('coronary artery calcification')

with col13:
    thal = st.number_input('Thalassemia')

if st.button('Predict Heart Health'):
    if sex == 'Male':
        sex = 1
    else:
        sex = 0

    input_df = pd.DataFrame({
        'age':[age],
        'sex':[sex],
        'cp':[cp],
        'trestbps':[trestbps],
        'chol':[chol],
        'fbs':[fbs],
        'restecg':[restecg],
        'thalach':[thalach],
        'exang':[exang],
        'oldpeak':[oldpeak],
        'slope':[slope],
        'ca':[ca],
        'thal':[thal],
    })

    result = model.predict(input_df)

    if result == 1:
        st.header("The Person may have heart disease, please contact a doctor.")
    else:
        st.header("The Person has a healthy heart")
