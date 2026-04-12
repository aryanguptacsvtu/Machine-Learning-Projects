
# 📰 Fake News Detector

**Fake News Detector** is an NLP-powered web application that classifies news articles as **Real** or **Fake** . 
The project comes with an interactive **Streamlit** frontend where users can paste any news text and instantly get a prediction along with a confidence score.

---

## 🚀 Features

- ✅ Classifies news text as **Real** or **Fake** in real time
- 📊 Displays **confidence score** for every prediction
- 🧹 Full **text preprocessing pipeline** (URL removal, punctuation cleaning, digit stripping, HTML tag removal)
- 💾 Model and vectorizer saved via `pickle` for instant inference
- 🖥️ Clean, styled **Streamlit UI** with sidebar disclaimer

---

## 🧠 Models Evaluated

| Model | Accuracy |
|---|---|
| Logistic Regression | **~99.0%** ✅ (Deployed) |
| Decision Tree | ~99.4% |
| Random Forest | ~98.9% |
| Gradient Boosting | **~99.5%** |

> Logistic Regression was chosen for deployment due to its balance of speed, interpretability, and strong performance.

---

## 📂 Project Structure

```
Fake-News-Detector/
│
├── Code.ipynb          # Data loading, model training & evaluation
├── frontend.py         # Streamlit web application
├── model.pkl           # Saved Logistic Regression model
├── vectorizer.pkl      # Saved TF-IDF vectorizer
├── True.csv            # Dataset of real news articles
├── Fake.csv            # Dataset of fake news articles
└── README.md
```

---

## 🗃️ Dataset

The project uses two CSV files:

- **`True.csv`** — Real news articles 
- **`Fake.csv`** — Fake news articles 

Both datasets are merged, labeled (`1` = Real, `0` = Fake), and shuffled before training.

---

## ⚙️ Text Preprocessing

Every article goes through the following cleaning steps before vectorization:

1. Lowercase conversion
2. URL removal (`http`, `www`)
3. Punctuation removal
4. Digit removal
5. Newline removal
6. HTML tag stripping

---

## 📦 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/aryanguptacsvtu/Machine-Learning-Projects.git
cd "Machine-Learning-Projects/Fake News Detector"
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit scikit-learn pandas numpy matplotlib seaborn
```

### 3. Train the model

If you want to train the model from scratch, run all cells in:

```bash
jupyter notebook Code.ipynb
```

This will regenerate `model.pkl` and `vectorizer.pkl`.

### 4. Launch the Streamlit app

```bash
streamlit run frontend.py
```

---

## ⚠️ Disclaimer

> This model is trained on historical data and **may not be 100% accurate**.
> Predictions should **not** be treated as absolute truth.
> Always verify news from multiple trusted sources independently.

---

## 💻 Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Pandas / NumPy** | Data loading and manipulation |
| **Scikit-learn** | Model building, TF-IDF vectorization, evaluation |
| **Streamlit** | Interactive web frontend |
| **Pickle** | Model serialization |

---

## 👨‍💻 Author

**Aryan Gupta**
🔗 [GitHub Profile](https://github.com/aryanguptacsvtu)

---

## ⭐ Support

If you found this project useful, please leave a ⭐ and share it with others!
