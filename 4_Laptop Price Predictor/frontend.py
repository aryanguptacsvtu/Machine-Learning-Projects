import streamlit as st
import pickle
import numpy as np

# --- Page config and header ---
st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻", layout="centered")

# --- Custom CSS ---
st.markdown("""
<style>
/* Change the title color */
h1 {
    color: #4A90E2; /* A nice blue color */
}

/* Style the predict button */
div[data-testid="stButton"] > button {
    background: linear-gradient(90deg, #4A90E2, #9013FE); /* Gradient background */
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 24px;
    font-weight: bold;
    box-shadow: 0 4px 14px 0 rgba(0,118,255,0.39);
    transition: all 0.3s ease;
}

div[data-testid="stButton"] > button:hover {
    background: linear-gradient(90deg, #9013FE, #4A90E2);
    box-shadow: 0 6px 20px 0 rgba(0,118,255,0.23);
}

/* Style the output container */
div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

/* Style the metric value */
div[data-testid="stMetricValue"] {
    color: #28a745; /* Green color for price */
    font-size: 2.5rem !important;
}

</style>
""", unsafe_allow_html=True)


# --- Load model and data ---
try:
    pipe = pickle.load(open('pipe.pkl','rb'))
    df = pickle.load(open('df.pkl','rb'))
except FileNotFoundError:
    st.error("Error: Model files (pipe.pkl, df.pkl) not found in the directory.")
    st.info("Please make sure the necessary model files are present to run the app.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading model files: {e}")
    st.stop()

# --- Page config and header ---
st.title("💻 Laptop Price Predictor")
st.markdown("Predict an estimated laptop price using a trained model. Adjust features and press **Predict Price**.")
st.write("---")

# --- Sidebar for info & dataset preview ---
with st.sidebar:
    st.header("About")
    st.write("This app estimates the laptop price using the model saved in `pipe.pkl`.")
    st.write("Select features in the tabs.") 
    st.write("---")
    if st.checkbox("Show dataset sample"):
        st.dataframe(df.sample(5))


# ------------- Main input layout -----------
tab1, tab2, tab3 = st.tabs(["💻 Core Specs", "💾 Hardware", "🖥️ Display"])

with tab1:
    st.subheader("Basic Specs")

    company = st.selectbox('Brand', df['Company'].unique(), help='Laptop manufacturer / brand')
    type = st.selectbox('Type', df['TypeName'].unique(), help='Laptop type (Notebook/Gaming/Ultrabook etc.)')
    cpu = st.selectbox('CPU', df['Cpu brand'].unique(), help='CPU brand')
    gpu = st.selectbox('GPU', df['Gpu brand'].unique(), help='GPU brand')
    os = st.selectbox("OS", df['os'].unique(), help='Operating system')

with tab2:
    st.subheader("Hardware Specs")

    ram = st.selectbox('RAM (GB)', [2,4,6,8,12,16,24,32,64], index=3, help='System memory in GB')
    hdd = st.selectbox('HDD (GB)', [0,128,256,512,1024,2048], help='Hard disk drive capacity')
    ssd = st.selectbox('SSD (GB)', [0,8,128,256,512,1024,2048], help='Solid state drive capacity')
    weight = st.number_input('Weight of Laptop (kg)', min_value=0.0, format="%.2f", help='Enter laptop weight in kilograms')

with tab3:
    st.subheader("Display")
    c1, c2 = st.columns(2)
    with c1:
        screen_size = st.number_input('Screen Size (inches)', min_value=0.0, format="%.2f", help='Diagonal screen size in inches')
        touchscreen = st.selectbox('Touchscreen',['No','Yes'], help='Is the screen a touchscreen?')
    with c2:
        resolution = st.selectbox('Screen Resolution', ['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'], help='Display resolution')
        ips = st.selectbox('IPS Panel',['No','Yes'], help='Is the panel IPS?')


st.write('') 
colc1, colc2, colc3 = st.columns([1,2,1]) 
with colc2:
    predict_button = st.button('🔮 Predict Price', use_container_width=True)

# --- Prediction logic---
if predict_button:
    ppi = None

    if touchscreen == 'Yes':
        touchscreen_val = 1
    else:
        touchscreen_val = 0

    if ips == 'Yes':
        ips_val = 1
    else:
        ips_val = 0

    # parse resolution safely
    try:
        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])
    except Exception:
        X_res = 0
        Y_res = 0

    # compute PPI only when screen_size is a positive number
    if screen_size and float(screen_size) > 0:
        ppi = ((X_res**2 + Y_res**2)**0.5) / float(screen_size)
    else:
        st.warning('Screen Size must be greater than zero to compute PPI. Using PPI=0 for prediction.')
        ppi = 0.0

    query = np.array([company, type, ram, weight, touchscreen_val, ips_val, ppi, cpu, hdd, ssd, gpu, os], dtype=object)
    query = query.reshape(1, 12)

    # model prediction 
    prediction = int(np.exp(pipe.predict(query)[0]))

    # --- Output Display ---
    st.write("---")
    with st.container(border=True):
        st.success("Prediction complete", icon="✅")
        
        colr1, colr2, colr3 = st.columns([1,2,1])
        with colr2:
            st.metric(label="Estimated Price", value=f"₹ {prediction:,.2f}") 
            
        st.caption("Price shown is the model's estimate. Consider this as guidance, not an exact market price.")