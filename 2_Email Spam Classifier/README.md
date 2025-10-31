# 📩 Email / SMS Spam Classifier

A simple spam classifier built with Streamlit and Python. This app uses a Naive Bayes model trained on a dataset of over 5,000 messages to predict whether a message is "Spam" or "Not Spam."

---

## ✨ Features

- **Real-time Prediction:** Instantly classifies messages from the text area.

- **ML-Powered:** Uses a Multinomial Naive Bayes model trained on 5,000+ messages.

- **NLP Pipeline:** Implements tokenization, stopword removal, and stemming via NLTK.

- **Clean UI:** Simple interface with clear, color-coded results (green for "Not Spam," red for "Spam").

- **EDA Notebook:** Code.ipynb includes full analysis with WordClouds and plots.

---

## 🛠️ How It Works

This classifier uses a **supervised machine learning** model. The core logic is split into two parts:

1. **Model Training (Code.ipynb):**

- Text from `spam.csv` is preprocessed (lowercase, tokenized, stemmed).

- Features are extracted using TfidfVectorizer.

- A `Multinomial Naive Bayes` (MNB) model is trained and exported as model.pkl (along with vectorizer.pkl).

2. **Streamlit App (frontend.py):**

- Loads the pre-trained `model.pkl` and `vectorizer.pkl`.

- Applies the same text preprocessing pipeline to the user's input.

- Vectorizes the input and feeds it to the model for a prediction.

- Displays the "Spam" or "Not Spam" result.

---

## 🚀 Tech Stack

* **Core:** Python, Scikit-Learn 
* **Web Framework:** Streamlit
* **Data Handling & NLP:** NumPy, Pandas, NLTK, Pickle
* **Data Visualization:** Matplotlib, Seaborn, WordCloud

---

## 📦 Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
```bash
    git clone https://github.com/your-username/Machine-Learning-Projects.git
    cd your-repo-name
```

2.  **Install the required libraries:**
 ```bash
    pip install -r requirements.txt
 ```

3.  **Download NLTK Data:**
    The app requires NLTK's `punkt` tokenizer and `stopwords` corpus. Run this in a Python shell:
```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
```

4.  **Run the Jupyter Notebook :**
    If you want to train the model yourself, run the `Code.ipynb` notebook. This will use the `spam.csv` file  to generate the `vectorizer.pkl` and `model.pkl` files.

5.  **Run the application:**
```bash
    streamlit run frontend.py
```

---

## 👨‍💻 Author

**Aryan Gupta**  
📍 Bhilai, Chhattisgarh  
🔗 [GitHub Profile](https://github.com/aryanguptacsvtu)

---

## ⭐ Support

If you like this project, leave a ⭐ and share it with others!