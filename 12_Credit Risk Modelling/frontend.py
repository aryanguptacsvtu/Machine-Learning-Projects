import pandas as pd
import numpy as np
import streamlit as st
import pickle

# Load models and encoders
model = pickle.load(open('rf_model.pkl', 'rb'))
encoders = {col : pickle.load(open(f'{col}_encoder.pkl', 'rb')) 
            for col in ['Sex', 'Housing', 'Saving accounts', 'Checking account']}

# --- Sidebar Configuration ---
st.sidebar.title("Feature Guide")
st.sidebar.info("""

* **Job** (0 - unskilled and non-resident, 1 - unskilled and resident, 2 - skilled, 3 - highly skilled)
* **Housing** (own, rent, or free)
* **Saving accounts** (little, moderate, quite rich, rich)
* **Checking account** ( little, moderate, rich)
* **Credit amount** (total loan money borrowed by applicant, in DM -Deutsch Mark)
* **Credit Risk** (**GOOD** : applicant is likely to repay reliably  , **BAD** : applicant is more likely to default or struggle with repayment)

""")

st.sidebar.markdown("---")
st.sidebar.markdown("### Made with ❤️ by Aryan Gupta")
# -----------------------------

# Main App UI
st.title("📊 Credit Risk Prediction")
st.write("Enter the applicant details to predict credit risk :")

age = st.number_input("Age", min_value=18, max_value=100, value=30)
sex = st.selectbox('Sex', ['male', 'female'])

job = st.selectbox('Job', [0, 1, 2, 3])
housing = st.selectbox('Housing', ['own', 'rent', 'free'])

saving_account = st.selectbox('Saving accounts', ['little', 'moderate', 'rich', 'quite rich'])
checking_account = st.selectbox('Checking accounts', ['little', 'moderate', 'rich'])

credit_amount = st.number_input("Credit Amount", min_value=0, value=1000)
duration = st.number_input("Duration (months)", min_value=1, value=12)

# Format input data
input_df = pd.DataFrame({
                            'Age': [age],
                            'Sex': [encoders['Sex'].transform([sex])[0]],
                            'Job': [job],   
                            'Housing':  [encoders['Housing'].transform([housing])[0]],
                            'Saving accounts': [encoders['Saving accounts'].transform([saving_account])[0]],
                            'Checking account':  [encoders['Checking account'].transform([checking_account])[0]],
                            'Credit amount': [credit_amount],
                            'Duration': [duration]
                        })

# Prediction Logic
if st.button("Predict"):
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.success("GOOD Credit Risk")
        st.balloons()
    else:
        st.error("BAD Credit Risk")