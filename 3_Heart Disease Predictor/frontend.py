import numpy as np
import pandas as pd
import streamlit as st
import pickle
import base64
import plotly.express as px

# --- Page setup & theming (UI only) ---
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="🫀",
    layout="wide",
)


# Subtle CSS polish: nicer cards, tighter spacing, better tabs/buttons
st.markdown("""
<style>
/* Reduce padding & tidy up container look */
.block-container {padding-top: 1.2rem; padding-bottom: 2rem;}
/* Card-like look for sections */
.section-card {border: 1px solid rgba(49,51,63,0.2); border-radius: 14px; padding: 1rem 1.2rem; background: rgba(250,250,252,0.8);}
hr {border: none; border-top: 1px solid rgba(0,0,0,0.08); margin: .75rem 0 1rem;}
/* Prettier tabs */
.stTabs [data-baseweb="tab-list"] {gap: 8px;}
.stTabs [data-baseweb="tab"] {border-radius: 10px; padding: 10px 14px; background: #f6f7fb;}
/* Buttons */
.stButton > button {border-radius: 10px; padding: .6rem 1.1rem; font-weight: 600;}
/* Tables */
.dataframe tbody tr:hover {background: rgba(0,0,0,0.02);}
.small-muted {color: #6b7280; font-size: 0.9rem;}
.badge {display: inline-block; padding: .25rem .55rem; border-radius: 999px; background: #eef2ff; font-size: .8rem; font-weight: 600; color: #3730a3;}
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.title("🫀 Heart Disease Predictor")
st.caption("Make single or bulk predictions with pre-trained ML models, and review model metrics.")

# --- Helper (unchanged functionality; fixed quote bug in download link) ---
def get_binary_file_downloader(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="predictions.csv">⬇️ Download Predictions CSV</a>'
    return href

tab1, tab2, tab3 = st.tabs(['🔮 Predict', '📦 Bulk Predict', 'ℹ️ Model Information'])

# =========================
# Tab 1: Predict (single)
# =========================
with tab1:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("Single Prediction")
    st.caption("Fill in the patient details below and click **Predict Heart Disease**.")

    # Group inputs into clean columns (UI only)
    c1, c2, c3 = st.columns(3)
    with c1:
        age = st.number_input("Age (years)", min_value=1, max_value=140, help="Age of the patient.")
        sex = st.selectbox('Sex', ['Male', 'Female'])
        chest_pain = st.selectbox('Chest Pain Type', ['Typical Angina','Atypical Angina','Non-Anginal Pain','Asymptomatic'])
        resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=300)
    with c2:
        cholesterol = st.number_input("Serum Cholesterol (mg/dL)", min_value=0)
        fasting_bs = st.selectbox('Fasting Blood Sugar', ['> 120 mg/dl', '<= 120 mg/dl'])
        resting_ecg = st.selectbox('Resting ECG Results', ['Normal','ST-T Wave Abnormality','Left Ventricular Hypertrophy'])
        max_hr = st.number_input("Maximum Heart Rate Achieved", min_value=50, max_value=250)
    with c3:
        exercise_angina = st.selectbox('Exercise Induced Angina', ['Yes','No'])
        oldpeak = st.number_input("Oldpeak (ST depression)", min_value=0.0, max_value=10.0)
        st_slope = st.selectbox("Slope of Peak Exercise ST Segment", ['Upsloping','Flat','Downsloping'])

    # Convert categorical inputs to Numerical Values (unchanged logic)
    sex = 0 if sex == "Male" else 1
    chest_pain = ['Typical Angina','Atypical Angina','Non-Anginal Pain','Asymptomatic'].index(chest_pain)
    fasting_bs = 1 if fasting_bs == '> 120 mg/dl' else 0
    resting_ecg = ['Normal','ST-T Wave Abnormality','Left Ventricular Hypertrophy'].index(resting_ecg)
    exercise_angina = 1 if exercise_angina == 'Yes' else 0
    st_slope = ['Upsloping','Flat','Downsloping'].index(st_slope)

    input_data = pd.DataFrame({
        'Age': [age],
        'Sex': [sex],
        'ChestPainType': [chest_pain],
        'RestingBP': [resting_bp],
        'Cholesterol': [cholesterol],
        'FastingBS': [fasting_bs],
        'RestingECG': [resting_ecg],
        'MaxHR': [max_hr],
        'ExerciseAngina': [exercise_angina],
        'Oldpeak': [oldpeak],
        'ST_Slope': [st_slope]
    })

    algo_names = ['Logistic Regression','Support Vector Machine','Decision Tree','Random Forest']
    model_files = ['LogisticRegression.pkl','SVM.pkl','DecisionTree.pkl','RandomForest.pkl']

    predictions = []

    def predict_heart_disease(data):
        for modelname in model_files:
            model = pickle.load(open(modelname, 'rb'))
            pred = model.predict(data)
            predictions.append(pred[0])
        return predictions

    st.markdown("<hr/>", unsafe_allow_html=True)
    if st.button("🔎 Predict Heart Disease"):
        st.subheader('📃 Results')
        st.markdown("<hr/>", unsafe_allow_html=True)

        result = predict_heart_disease(input_data)

        # Display results in two columns for readability
        col_a, col_b = st.columns(2)
        for i in range(len(predictions)):
            container = col_a if i % 2 == 0 else col_b
            with container:
                st.markdown(f"**{algo_names[i]}**  <span class='badge'>Model</span>", unsafe_allow_html=True)
                if result[i] == 0:
                    st.success("✅ Result: No Heart Disease Detected")
                else:
                    st.error("⚠️ Result: Heart Disease Detected")
                st.markdown("<hr/>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# Tab 2: Bulk Predict
# =========================
with tab2:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("Upload CSV File")
    with st.expander("📋 Instructions to upload file", expanded=True):
        st.info('''
1. No NaN values are allowed.  
2. Total **11 features** required in this order:  
   **(Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope)**  
3. Check the spellings of the feature names.  
4. Feature values convention:
   - Age : age of the patient (years)  
   - Sex : sex of the patient [0:Male, 1:Female]  
   - ChestPainType : chest pain type [3:'Typical Angina', 0:'Atypical Angina', 1:'Non-Anginal Pain', 2:'Asymptomatic']  
   - RestingBP : resting blood pressure [mm Hg]  
   - Cholesterol : serum cholesterol [mg/dl]  
   - FastingBS : fasting blood sugar [1: if FastingBS >120 mg/dl , 0: otherwise]  
   - RestingECG : resting ECG results [0:Normal , 1:ST-T wave abnormality , 2:'Left Ventricular Hypertrophy']  
   - MaxHR : maximum heart rate achieved [Numeric value between 60 and 202]  
   - ExerciseAngina : exercise-induced angina [1:Yes, 0:No]  
   - Oldpeak : ST [Numeric value measured in depression]  
   - ST_Slope : slope of the peak exercise ST segment [0:'Upsloping', 1:'Flat', 2:'Downsloping']  
        ''')

    uploaded_file = st.file_uploader("📤 Upload a CSV file", type=['csv'])

    if uploaded_file is not None:
        input_data = pd.read_csv(uploaded_file)
        model = pickle.load(open('LogisticRegression.pkl', 'rb'))

        expected_columns = ['Age','Sex','ChestPainType','RestingBP','Cholesterol','FastingBS','RestingECG', 'MaxHR','ExerciseAngina','Oldpeak','ST_Slope']
        
        if set(expected_columns).issubset(input_data.columns):

            input_data['Prediction LR'] = ''

            for i in range(len(input_data)):
                arr = input_data.iloc[i, :-1].values
                input_data['Prediction LR'][i] = model.predict([arr])[0]

            input_data.to_csv('PredictedHeart.csv', index=False)

            st.subheader("Predictions")
            st.caption("Below are your predictions with an added **Prediction LR** column.")
            st.write(input_data)

            st.markdown(get_binary_file_downloader(input_data), unsafe_allow_html=True)

        else:
            st.warning("⚠️ Please make sure the uploaded CSV file has the correct columns.")
    else:
        st.warning("📎 Upload a CSV file to get prediction.")
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# Tab 3: Model Information
# =========================
with tab3:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("Model Accuracies")
    data = {
        'Decision Trees': 81.52,
        'Logistic Regression': 85.86,
        'Random Forest': 86.41,
        'Support Vector Machine': 85.22
    }
    Models = list(data.keys())
    Accuracies = list(data.values())
    df = pd.DataFrame(list(zip(Models, Accuracies)), columns=['Models','Accuracies'])

    fig = px.bar(df, y='Accuracies', x='Models',
                 title="Validation Accuracies by Model")
    fig.update_yaxes(title_text="Accuracy (%)", rangemode="tozero")
    fig.update_xaxes(title_text="Model")
    fig.update_layout(height=420, bargap=0.25)

    st.plotly_chart(fig, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)
