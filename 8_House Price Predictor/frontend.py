import streamlit as st
import pandas as pd
import pickle

# --- Page Config ---
st.set_page_config(page_title="Housing Price Predictor", page_icon="🏡", layout="centered")

# --- Load the Model ---
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:
        return pickle.load(file)

model = load_model()

# --- Sidebar: Feature Information ---
with st.sidebar:
    st.header("📖 Feature Glossary")
    st.info("""
    **Understanding the Inputs:**
    
    * **Longitude:** A measure of how far west a house is; a higher value is farther west.
    * **Latitude:** A measure of how far north a house is; a higher value is farther north.
    * **Housing Median Age:** Median age of a house within a block; a lower number is a newer building.
    * **Total Rooms:** Total number of rooms within a block.
    * **Total Bedrooms:** Total number of bedrooms within a block.
    * **Population:** Total number of people residing within a block.
    * **Households:** Total number of households (a group of people residing within a home unit) for a block.
    * **Median Income:** Median income for households within a block of houses (measured in tens of thousands of US Dollars).
    * **Ocean Proximity:** Location of the house w.r.t ocean/sea.
    """)
    st.markdown("---")
    st.markdown("### Made with ❤️ by Aryan Gupta")

# --- App Header ---
st.title("🏡 California Housing Price Predictor")
st.write("Enter the block details below to predict the median house value. (Check the sidebar for feature definitions!)")
st.markdown("---")

# --- Input Fields ---
col1, col2 = st.columns(2)

with col1:
    longitude = st.number_input("Longitude", value=-122.230, format="%.3f")
    housing_median_age = st.number_input("Housing Median Age", value=41.0, min_value=1.0)
    total_bedrooms = st.number_input("Total Bedrooms", value=129.0, min_value=1.0)
    households = st.number_input("Households", value=126.0, min_value=1.0)
    ocean_proximity = st.selectbox("Ocean Proximity", options=["<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND"],index=3)

with col2:
    latitude = st.number_input("Latitude", value=37.880, format="%.3f")
    total_rooms = st.number_input("Total Rooms", value=880.0, min_value=1.0)
    population = st.number_input("Population", value=322.0, min_value=1.0)
    median_income = st.number_input("Median Income (in $10k)", value=8.3252, format="%.4f")

st.markdown("---")

# --- Prediction Logic ---
if st.button("Predict House Price", type="primary"):
    input_data = pd.DataFrame([{
                                "longitude": longitude,
                                "latitude": latitude,
                                "housing_median_age": housing_median_age, 
                                "total_rooms": total_rooms,
                                "total_bedrooms": total_bedrooms,
                                "population": population,
                                "households": households,
                                "median_income": median_income,
                                "ocean_proximity": ocean_proximity
                            }])
    
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"### Predicted Median House Value: ${prediction:,.2f}")
        st.balloons()

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
