import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Customer Churn Predictor", page_icon="📞", layout="wide")

st.markdown("""
<style>
    /* Change global header color */
    h1 {
        color: #1f77b4;
    }
    /* Style the form submit button */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #e63946;
        border-color: #e63946;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar Information ---
with st.sidebar:
    st.markdown("# 📊 Telco Analytics")
    
    st.title("About this App")
    st.info("This predictive application uses a pre-trained Machine Learning model to determine the likelihood of a customer leaving the service provider (Churn).")
    
    st.markdown("### 🛠️ How to Use:")
    st.markdown("""
                1. Enter the customer's **Demographics**.
                2. Input their **Account Info** and charges.
                3. Select their active **Services**.
                4. Click **Predict Churn** at the bottom.
                """)
    
    st.markdown("---")
    st.markdown("Made with ❤️ by Aryan Gupta")

# --- Main App Header ---
st.title("📞 Telco Customer Churn Predictor")
st.write("Enter the customer's details below to predict if they are likely to churn.")

# --- Load Models and Encoders ---
@st.cache_resource
def load_assets():

    with open("customer_churn_model.pkl", "rb") as f:
        model_data = pickle.load(f)
    model = model_data["model"]
    feature_names = model_data["features_names"]
    
    with open("encoders.pkl", "rb") as f:
        encoders = pickle.load(f)
        
    return model, feature_names, encoders

loaded_model, feature_names, encoders = load_assets()

# --- User Input Form ---
with st.form("prediction_form"):

    st.subheader("Customer Demographics")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        gender = st.selectbox("Gender", ["Female", "Male"])
    with col2:
        senior_citizen = st.selectbox("Senior Citizen", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    with col3:
        partner = st.selectbox("Partner", ["Yes", "No"])
    with col4:
        dependents = st.selectbox("Dependents", ["Yes", "No"])

    st.subheader("Account Information")

    col5, col6, col7 = st.columns(3)
    with col5:
        tenure = st.number_input("Tenure (Months)", min_value=0, max_value=100, value=1)
    with col6:
        contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    with col7:
        paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])

    col8, col9, col10 = st.columns(3)
    with col8:
        payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
    with col9:
        monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, value=29.85)
    with col10:
        total_charges = st.number_input("Total Charges ($)", min_value=0.0, value=29.85)

    st.subheader("Services Subscribed")

    col11, col12, col13, col14 = st.columns(4)
    with col11:
        phone_service = st.selectbox("Phone Service", ["Yes", "No"])
        multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
    with col12:
        internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
        online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
    with col13:
        online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
        device_protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
    with col14:
        tech_support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
        streaming_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
        streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])

    submitted = st.form_submit_button("Predict Churn")

# --- Prediction Logic ---
if submitted:
    input_data = {
        'gender': gender,
        'SeniorCitizen': senior_citizen,
        'Partner': partner,
        'Dependents': dependents,
        'tenure': tenure,
        'PhoneService': phone_service,
        'MultipleLines': multiple_lines,
        'InternetService': internet_service,
        'OnlineSecurity': online_security,
        'OnlineBackup': online_backup,
        'DeviceProtection': device_protection,
        'TechSupport': tech_support,
        'StreamingTV': streaming_tv,
        'StreamingMovies': streaming_movies,
        'Contract': contract,
        'PaperlessBilling': paperless_billing,
        'PaymentMethod': payment_method,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges
    }

    input_df = pd.DataFrame([input_data])

    # Apply Label Encoders
    for column, encoder in encoders.items():
        if column in input_df.columns:
            input_df[column] = encoder.transform(input_df[column])

    # Align columns with training data order
    input_df = input_df.reindex(columns=feature_names)

    # Make Prediction
    prediction = loaded_model.predict(input_df)
    pred_prob = loaded_model.predict_proba(input_df)[0]

    st.markdown("---")
    st.subheader("Prediction Results")
    
    if prediction[0] == 1:
        st.markdown(f"""
        <div style="background-color: #ffe6e6; padding: 20px; border-radius: 10px; border-left: 6px solid #ff4b4b; margin-bottom: 20px;">
            <h3 style="color: #cc0000; margin: 0;">⚠️ High Risk: Customer is not likely to stay.</h3>
            <p style="margin: 5px 0 0 0; font-size: 16px; color: #333;">Model Confidence: <b>{pred_prob[1] * 100:.1f}%</b></p>
        </div>
        """, unsafe_allow_html=True)
        st.progress(float(pred_prob[1]))

    else:
        st.markdown(f"""
        <div style="background-color: #e6ffe6; padding: 20px; border-radius: 10px; border-left: 6px solid #28a745; margin-bottom: 20px;">
            <h3 style="color: #155724; margin: 0;">✅ Safe: Customer is likely to stay.</h3>
            <p style="margin: 5px 0 0 0; font-size: 16px; color: #333;">Model Confidence: <b>{pred_prob[0] * 100:.1f}%</b></p>
        </div>
        """, unsafe_allow_html=True)
        st.progress(float(pred_prob[0]))