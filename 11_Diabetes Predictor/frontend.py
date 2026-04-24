import streamlit as st
import pandas as pd
import numpy as np
import pickle

# --- Load the saved model and scaler ---
try:
    model = pickle.load(open('svc_model.pkl', 'rb'))
    scaler = pickle.load(open('scaler.pkl', 'rb')) 
except FileNotFoundError:
    st.error("Model or Scaler file not found. Please ensure 'svc_model.pkl' and 'scaler.pkl' are in the directory.")

def predict_diabetes(input_data):
    input_as_numpy = np.asarray(input_data).reshape(1, -1)
    std_data = scaler.transform(input_as_numpy)
    prediction = model.predict(std_data)
    return prediction[0]

def main():
    st.set_page_config(page_title="Diabetes Prediction App", layout="wide")
    
    # --- SIDEBAR INFO ---
    st.sidebar.header("Feature Guide")
    st.sidebar.info("""
    **Pregnancies**: Number of times pregnant.
                    
    **Glucose**: Plasma glucose concentration.
                    
    **Blood Pressure**: Diastolic blood pressure (mm Hg).
                    
    **Skin Thickness**: Triceps skin fold thickness (mm).
                    
    **Insulin**: 2-Hour serum insulin.
                    
    **BMI**: Body Mass Index.
                    
    **Diabetes Pedigree Function**: Genetic risk score.
                    
    **Age**: Age in years.
    """)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Made with ❤️ by Aryan Gupta")

    # --- MAIN UI ---
    st.title("📊 Diabetes Prediction System")
    st.write("Adjust the values below and click predict. Default values are set to dataset averages.")
    
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            pregnancies = st.number_input("Number of Pregnancies", min_value=0, step=1, value=2,help="Count of pregnancies, 0 means never pregnant")
            glucose = st.number_input("Glucose Level", min_value=0, value=117, help="Normal range is usually < 140 mg/dL")
            blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0, value=72,help="Typical adult range is around 60-80 mm Hg")
            skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0, value=23,help="20-30 mm is common")

        with col2:
            insulin = st.number_input("Insulin Level (mu U/ml)", min_value=0, value=30,help="Rough reference range is about 16-166")
            bmi = st.number_input("BMI (Body Mass Index)", min_value=0.0, format="%.1f", value=32.0,help="Normal BMI is 18.5-24.9")
            dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f", value=0.372, help="Higher value = higher genetic risk")
            age = st.number_input("Age of Person", min_value=0, step=1, value=29,help="Age in years")

    st.markdown("---")
    
    # Result Button
    if st.button("Check Result", use_container_width=True):
        features = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]
        result = predict_diabetes(features)
        
        if result == 1:
            st.error("### ⚠️ Result: The patient is likely to be Diabetic.")
        else:
            st.success("### ✅ Result: The patient is likely NOT Diabetic.")
            st.balloons()

if __name__ == '__main__':
    main()