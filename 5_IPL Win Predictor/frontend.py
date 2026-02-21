import streamlit as st
import pickle
import pandas as pd

# Custom CSS
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .title-container {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    .title-text {
        color: white;
        font-size: 42px;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin: 0;
    }
    
    .subtitle-text {
        color: #fff;
        font-size: 18px;
        margin-top: 10px;
        opacity: 0.9;
    }
    
    .prediction-container {
        background: white;
        padding: 25px;
        border-radius: 15px;
        margin-top: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }
    
    .team-prediction {
        padding: 20px;
        border-radius: 10px;
        margin: 15px 0;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .batting-team {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
    }
    
    .bowling-team {
        background: linear-gradient(135deg, #ee0979 0%, #ff6a00 100%);
        color: white;
    }
    
    .cricket-icon {
        font-size: 40px;
        margin-bottom: 10px;
    }
    
    div[data-testid="stNumberInput"] label,
    div[data-testid="stSelectbox"] label {
        color: white !important;
        font-weight: 600 !important;
        font-size: 16px !important;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        font-size: 20px;
        font-weight: bold;
        padding: 15px 40px;
        border-radius: 30px;
        border: none;
        box-shadow: 0 5px 20px rgba(245, 87, 108, 0.4);
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(245, 87, 108, 0.6);
    }
    
    .info-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 20px;
        border-radius: 12px;
        margin: 20px 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background: rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(10px);
        color: white;
        text-align: center;
        padding: 15px;
        font-size: 16px;
        border-top: 1px solid rgba(255, 255, 255, 0.2);
        z-index: 999;
    }
    
    .footer-text {
        margin: 0;
        font-weight: 500;
    }
    
    .footer-name {
        font-weight: bold;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .sidebar .block-container {
        padding-top: 2rem;
    }
    
    .sidebar-card {
        background: rgba(255, 255, 255, 0.95);
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .sidebar-title {
        font-size: 18px;
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
        text-align: center;
    }
    
    .sidebar-content {
        font-size: 14px;
        color: #666;
        line-height: 1.6;
    }
    
    .stat-item {
        display: flex;
        justify-content: space-between;
        padding: 8px 0;
        border-bottom: 1px solid #eee;
    }
    
    .stat-label {
        font-weight: 600;
        color: #555;
    }
    
    .stat-value {
        color: #f5576c;
        font-weight: bold;
    }
    
    .ipl-logo {
        width: 100%;
        text-align: center;
        font-size: 80px;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

teams = ['Sunrisers Hyderabad',
        'Mumbai Indians',
        'Royal Challengers Bangalore',
        'Kolkata Knight Riders',
        'Kings XI Punjab',
        'Chennai Super Kings',
        'Rajasthan Royals',
        'Delhi Capitals']


cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
        'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
        'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
        'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
        'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
        'Sharjah', 'Mohali', 'Bengaluru']

pipe = pickle.load(open('pipe.pkl','rb'))


# Create sidebar
with st.sidebar:
    
    st.markdown("""
        <div class="sidebar-card">
            <div class="sidebar-title">📊 About IPL</div>
            <div class="sidebar-content">
                The Indian Premier League is a professional Twenty20 cricket league in India. It's one of the most-attended cricket leagues in the world.
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="sidebar-card">
            <div class="sidebar-title">🎯 Quick Facts</div>
            <div class="stat-item">
                <span class="stat-label">Teams:</span>
                <span class="stat-value">8</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Format:</span>
                <span class="stat-value">T20</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Overs:</span>
                <span class="stat-value">20</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Players:</span>
                <span class="stat-value">11 per team</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="sidebar-card">
            <div class="sidebar-title">🤖 ML Model</div>
            <div class="sidebar-content">
                This predictor uses machine learning algorithms trained on historical IPL match data to predict win probabilities based on current match conditions.
            </div>
        </div>
    """, unsafe_allow_html=True)
    
   

# Title with custom HTML
st.markdown("""
    <div class="title-container">
        <h1 class="title-text">🏏 IPL Win Predictor</h1>
        <p class="subtitle-text">Predict match outcomes with machine learning</p>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(teams))

selected_city = st.selectbox('Select host city',sorted(cities))

target = st.number_input('Target')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Overs completed')
with col5:
    wickets = st.number_input('Wickets out')


if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    
    st.markdown("""
        <div class="prediction-container">
            <h2 style="text-align: center; color: #333; margin-bottom: 20px;">📊 Match Prediction</h2>
            <div class="team-prediction batting-team">
                🏏 {} - {}%
            </div>
            <div class="team-prediction bowling-team">
                ⚾ {} - {}%
            </div>
        </div>
    """.format(batting_team, str(round(win*100)), bowling_team, str(round(loss*100))), unsafe_allow_html=True)


# Footer
st.markdown("""
    <div class="footer">
        <p class="footer-text">Made by <span class="footer-name">Aryan Gupta</span></p>
    </div>
""", unsafe_allow_html=True)