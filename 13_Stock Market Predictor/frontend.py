import streamlit as st
import yfinance as yf
import pandas as pd
import pickle

# --- Page Configuration ---
st.set_page_config(page_title="S&P 500 Predictor", page_icon="📈", layout="centered")

# --- Sidebar ---
with st.sidebar:
    st.header("ℹ️ About the App")
    st.write("""
    This application uses a Machine Learning model to forecast daily directional movements of the **S&P 500**.
    """)
    
    st.subheader("⚙️ Model Specifications")
    st.markdown("""
    * **Algorithm:** Random Forest Classifier
    * **Threshold:** 60% (Strict)
    * **Lookback Horizons:** 2, 5, 60, 250, and 1000 days
    """)
    
    st.divider()
    
    st.warning("""
    **⚠️ Disclaimer:** This tool is for **educational purposes only**. It does not constitute financial advice. 
    Do not use these predictions for real-world trading.
    """)

    st.sidebar.markdown("---")
    st.sidebar.markdown("### Made with ❤️ by Aryan Gupta")

# --- Load the Model ---
@st.cache_resource
def load_model():
    try:
        with open('rf_model.pkl', 'rb') as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        st.error("Model file 'rf_model.pkl' not found. Please ensure it is in the same directory.")
        return None

# --- Fetch and Prepare Data ---
@st.cache_data
def load_and_prep_data():
    # Fetch data
    sp500 = yf.Ticker('^GSPC')
    sp500 = sp500.history(period='max')
    
    # Preprocess exactly as in training
    sp500.drop(columns=['Dividends', 'Stock Splits'], inplace=True, errors='ignore')
    sp500['Tomorrow'] = sp500['Close'].shift(-1)
    sp500['Target'] = (sp500['Tomorrow'] > sp500['Close']).astype(int)
    
    sp500 = sp500.loc['1990-01-01':].copy()
    
    # Feature Engineering (Horizons)
    horizons = [2, 5, 60, 250, 1000]
    new_predictors = []
    
    for horizon in horizons:
        rolling_averages = sp500.rolling(window=horizon).mean()
        
        ratio_column = f'Close_Ratio_{horizon}'
        sp500[ratio_column] = sp500['Close'] / rolling_averages['Close']
        
        trend_column = f'Trend_{horizon}'
        sp500[trend_column] = sp500.shift(1).rolling(horizon).sum()['Target'] 
        
        new_predictors += [ratio_column, trend_column]
        
    sp500 = sp500.dropna()
    return sp500, new_predictors

# --- Main UI ---
st.title("📈 S&P 500 Market Predictor")
st.write("Predict whether the S&P 500 index will close **higher** or **lower** tomorrow based on historical price action and trends.")

st.divider()

# Load model and data
model = load_model()

if model:
    with st.spinner("Fetching latest market data and engineering features..."):
        data, predictors = load_and_prep_data()
        
    if not data.empty:
        # Display Current Data
        st.subheader("Recent Market Performance")
        st.write("Last 100 Days Closing Prices:")
        st.line_chart(data['Close'].tail(100))
        
        # Show the most recent closing price
        latest_date = data.index[-1].strftime("%B %d, %Y")
        latest_close = data['Close'].iloc[-1]
        
        col1, col2 = st.columns(2)
        col1.metric("Last Trading Date", latest_date)
        col2.metric("Last Closing Price", f"${latest_close:,.2f}")
        
        st.divider()
        
        # Prediction Section
        st.subheader("🔮 Predict Tomorrow's Movement")
        st.write("The model uses a strict **60% confidence threshold** to predict an upward movement, reducing false positives.")
        
        if st.button("Run Prediction", type="primary"):
            # Get the very last row of our engineered data
            latest_features = data[predictors].iloc[-1:]
            
            # Predict probabilities
            upward_probability = model.predict_proba(latest_features)[:, 1][0]
            
            # Display results based on your custom 0.6 threshold
            if upward_probability >= 0.6:
                st.success(f"### Prediction: Market goes UP ⬆️")
                st.write(f"**Confidence:** {upward_probability * 100:.2f}%")
                st.info("The model is highly confident that the closing price will increase tomorrow.")
            else:
                st.warning(f"### Prediction: DOWN / NO CLEAR SIGNAL ⬇️")
                st.write(f"**Confidence for an UP day:** {upward_probability * 100:.2f}%")
                st.info("The model's confidence for an upward movement is below the 60% threshold. Expect a downward trend or high market uncertainty tomorrow.")
                
else:
    st.warning("Please train and save your model as `rf_model.pkl` before running the UI.")