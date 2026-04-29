# 📈 S&P 500 Market Direction Predictor

A machine learning project that forecasts the **daily directional movement** of the S&P 500 index - predicting whether it will close higher or lower the next trading day. Built with a Random Forest Classifier and served through an interactive Streamlit web app.

The model is trained on decades of **historical S&P 500 data** (from 1990 onwards) fetched live via `yfinance`. 

---

### 📊 Feature Engineering

For each of the following **lookback horizons** - `2, 5, 60, 250, and 1000 days` - two features are computed:

| Feature | Description |
|---|---|
| `Close_Ratio_{horizon}` | Current close price divided by the rolling mean close - captures momentum |
| `Trend_{horizon}` | Rolling sum of past up-days (Target = 1) - captures directional trend strength |

This results in **10 engineered features** fed into the classifier.

---
### 🤖 Model

| Parameter | Value |
|---|---|
| Algorithm | Random Forest Classifier |
| Estimators | 200 trees |
| Min Samples Split | 50 |
| Prediction Threshold | **60%** (strict - reduces false positives) |

The strict 0.6 probability threshold means the model only signals an **UP day** when it's highly confident.

---

## 🖥️ Streamlit App

The `frontend.py` Streamlit app provides an interactive interface to:

- View the **last 100 days** of S&P 500 closing prices
- See the **latest closing price and trading date**
- Run a **live prediction** for the next trading day with confidence score

---

## 📁 Project Structure

```
13_Stock Market Predictor/
│
├── Code.ipynb          # Full ML pipeline
├── frontend.py         # Streamlit web application
├── requirements.txt     
└── README.md
```

---

## ⚙️ Getting Started


### 1. Clone the repository

```bash
git clone https://github.com/aryanguptacsvtu/Machine-Learning-Projects.git
cd "Machine-Learning-Projects/13_Stock Market Predictor"
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```


### 3. Train the Model

Open and run all cells in `Code.ipynb`. This will:
1. Fetch historical S&P 500 data
2. Engineer features
3. Train the Random Forest model
4. Save the model as `rf_model.pkl`


### 4. Launch the App

```bash
streamlit run frontend.py
```

---

## ⚠️ Disclaimer

This project is for **educational purposes only**. The predictions generated are based on historical price patterns and do **not** constitute financial advice. Do not use this tool for real-world trading decisions.

---

## 👨‍💻 Author

**Aryan Gupta**
🔗 [GitHub Profile](https://github.com/aryanguptacsvtu)

---

## ⭐ Support

If you found this project useful, please leave a ⭐ and share it with others!
