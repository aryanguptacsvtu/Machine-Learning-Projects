import streamlit as st
import pandas as pd
import pickle

# --- Page Config ---
st.set_page_config(page_title="Titanic Survival Predictor", page_icon="🚢", layout="centered")

# --- Load the Model ---
@st.cache_resource
def load_model():
    with open("rf_model.pkl", "rb") as file:
        return pickle.load(file)

model = load_model()

# --- Sidebar: Feature Information ---
with st.sidebar:
    st.header("📖 Feature Glossary")
    st.info("""
    **Understanding the Inputs:**
    
    * **Pclass:** Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd). A proxy for socio-economic status.
    * **Sex:** Gender of the passenger.
    * **Age:** Age of the passenger in years.
    * **SibSp:** Number of siblings or spouses the passenger had aboard the Titanic.
    * **Parch:** Number of parents or children the passenger had aboard the Titanic.
    * **Fare:** How much the passenger paid for their ticket.
    * **Embarked:** Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).
    """)
    st.markdown("---")
    st.markdown("### Made with ❤️ by Aryan Gupta")

# --- App Header ---
st.title("🚢 Titanic Survival Predictor")
st.write("Enter passenger details below to predict whether they would have survived the Titanic disaster.")
st.markdown("---")

# --- Input Fields ---
col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox("Ticket Class (Pclass)", options=[1, 2, 3], index=2)
    sex = st.selectbox("Sex", options=["Male", "Female"])
    age = st.number_input("Age", min_value=0.0, max_value=120.0, value=28.0, step=1.0)
    fare = st.number_input("Fare ($)", min_value=0.0, value=32.20, step=1.0)

with col2:
    sibsp = st.number_input("Siblings/Spouses Aboard (SibSp)", min_value=0, max_value=10, value=0)
    parch = st.number_input("Parents/Children Aboard (Parch)", min_value=0, max_value=10, value=0)
    embarked = st.selectbox("Port of Embarkation", options=["Southampton (S)", "Cherbourg (C)", "Queenstown (Q)"])

st.markdown("---")

# --- Prediction Logic ---
if st.button("Predict Survival", type="primary"):
    
    # Encode 'Sex' (male: 0, female: 1) 
    sex_encoded = 0 if sex == "Male" else 1
    
    # Encode 'Embarked' (S: 0, C: 1, Q: 2) 
    if embarked.startswith("S"):
        embarked_encoded = 0
    elif embarked.startswith("C"):
        embarked_encoded = 1
    else:
        embarked_encoded = 2
        
    input_data = pd.DataFrame([{
                                "Pclass": pclass,
                                "Sex": sex_encoded,
                                "Age": age,
                                "SibSp": sibsp,
                                "Parch": parch,
                                "Fare": fare,
                                "Embarked": embarked_encoded
                            }])
                            
    try:
        # Make prediction
        prediction = model.predict(input_data)[0]
        
        # Display the result
        if prediction == 1:
            st.success("### 🟢 Prediction: The passenger survived!")
            st.balloons()
        else:
            st.error("### 🔴 Prediction: The passenger did not survive.")
            
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
