import streamlit as st
import pickle
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string

# ------------------------- Load Data -------------------------
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))
ps = PorterStemmer()

# ------------------------- Preprocessing -------------------------
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text) # Tokenization

    y = []
    for i  in text:
        if i.isalnum():
            y.append(i)  # Removing special characters

    text = y[:]
    y.clear()

    # Removing stopwords & punctuation
    for i in text:
        if (i not in stopwords.words('english')) and (i not in string.punctuation):
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# ------------------------- Custom CSS ----------------------------------------
st.markdown("""
    <style>
        /* Page background and font */
        body {
            background-color: #f9fafc;
        }
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #dfe9f3 0%, #ffffff 100%);
        }
        h1 {
            color: #2E4053;
            text-align: center;
            font-family: 'Poppins', sans-serif;
        }
        .stTextArea label {
            font-weight: 600;
            font-size: 1rem;
        }
        .result-card {
            border-radius: 15px;
            padding: 25px;
            margin-top: 25px;
            text-align: center;
            font-size: 1.5rem;
            font-weight: 600;
            animation: fadeIn 1s ease-in;
        }
        @keyframes fadeIn {
            from {opacity: 0; transform: translateY(15px);}
            to {opacity: 1; transform: translateY(0);}
        }
        .spam {
            background-color: #ffebee;
            color: #c62828;
            box-shadow: 0px 4px 10px rgba(255, 0, 0, 0.2);
        }
        .not-spam {
            background-color: #e8f5e9;
            color: #2e7d32;
            box-shadow: 0px 4px 10px rgba(0, 255, 0, 0.2);
        }
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ------------------------- App Header ---------------------------------------------
st.markdown("<h1>📩 Email / SMS Spam Classifier</h1>", unsafe_allow_html=True)
st.write("🔍 This app uses a Machine Learning model to classify messages as **Spam** or **Not Spam**.")

# ------------------------- Input Section -------------------------------------------
with st.container():
    input_sms = st.text_area("✉️ Enter your message below:", placeholder="Type or paste the message here...")

# ------------------------- Prediction Section ---------------------------------------------
if st.button("🚀 Predict"):
    if input_sms.strip() == "":
        st.warning("⚠️ Please enter a message before predicting.")
    else:
        # Preprocess and predict
        transformed_sms = transform_text(input_sms)
        vector_input = tfidf.transform([transformed_sms])
        result = model.predict(vector_input)[0]

        if result == 1:
            st.markdown('<div class="result-card spam">🚫 This message is <b>SPAM</b>!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result-card not-spam">✅ This message is <b>NOT SPAM</b>!</div>', unsafe_allow_html=True)

# ------------------------- Footer ------------------------------------------
st.markdown("""
<hr>
<p style='text-align:center; font-size:0.9rem; color:gray;'>
Made with ❤️ by <b>Aryan Gupta</b> | Streamlit + ML
</p>
""", unsafe_allow_html=True)
