import streamlit as st
import pickle
import re

# Initialize session state
if 'user_input' not in st.session_state:
    st.session_state.user_input = ''

# Load saved model and vectorizer
@st.cache_resource
def load_model():
    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    return model, vectorizer

model, vectorizer = load_model()

# Text preprocessing
def word_operations(text):
    text = text.lower()
    text = re.sub(r'https?://\S+|[www.\S+](http://www.\S+)', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d', '', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'<.*?>', '', text)
    return text

# Get prediction probability
def get_confidence(model, vectorized_text):
    if hasattr(model, 'predict_proba'):
        probs = model.predict_proba(vectorized_text)[0]
        return max(probs) * 100
    return 0

# ------------- Sidebar Disclaimer -------
with st.sidebar:
    st.title("⚠️ Important Disclaimer")
    st.warning(
        "**Please Note:**\n\n"
        "This model is trained on historical data and may not be 100% accurate. "
        "The predictions should NOT be fully relied upon as absolute truth.\n\n"
        "• Check multiple sources\n\n"
        "• Verify facts independently\n\n"
        "• Use this as a supplementary tool only\n\n"
        "Always do your own research before believing any news!"
    )
    st.divider()
    st.markdown("### Made with ❤️ by Aryan Gupta")

# ----------- UI Styling --------
st.markdown("""
<style>
.main {
background-color: #f5f7fa;
}
.title {
text-align: center;
font-size: 40px;
font-weight: bold;
color: #2c3e50;
}
.subtitle {
text-align: center;
font-size: 18px;
color: #555555;
margin-bottom: 20px;
}

.stButton button {
background-color: #4CAF50;
color: white;
border-radius: 8px;
height: 40px;
width: 100%;
font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# -------------- Main UI ---------------

st.markdown('<div class="title">📰 Fake News Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Check if a news article is Real or Fake</div>', unsafe_allow_html=True)

user_input = st.text_area("Enter News Text Here", value=st.session_state.user_input, height=200)
st.session_state.user_input = user_input

# Character counter
char_count = len(user_input)
st.caption(f"📝 Characters: {char_count} / 10000")

# Predict and Clear buttons 
col1, col2 = st.columns(2)
with col1:
    predict_btn = st.button("🔍 Predict", use_container_width=True)
with col2:
    clear_btn = st.button("🗑️ Clear", use_container_width=True)

if clear_btn:
    st.session_state.user_input = ""
    st.rerun()

if predict_btn:
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text!")
        
    else:
        cleaned_text = word_operations(user_input)
        vectorized_text = vectorizer.transform([cleaned_text])

        prediction = model.predict(vectorized_text)[0]
        confidence = get_confidence(model, vectorized_text)

        if prediction == 1:
            st.success(f"✅ This news is **Real** (Confidence: {confidence:.1f}%)")
        else:
            st.error(f"🚨 This news is **Fake** (Confidence: {confidence:.1f}%)")



