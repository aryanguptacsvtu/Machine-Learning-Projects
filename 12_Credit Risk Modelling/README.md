# 💳 Credit Risk Modelling

This project tackles a binary classification problem in the financial domain. Given an applicant's demographic and financial profile, the model predicts whether they are likely to **repay reliably (GOOD)** or likely to **default (BAD)**.


---

## 📁 Project Structure

```
12_Credit Risk Modelling/
│
├── Code.ipynb                   # Full ML pipeline
├── frontend.py                  # Streamlit web application
├── german_credit_data.csv       # Source dataset 
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

**Source:** German Credit Data  
**Size:** 1,000 applicants · 10 features · 1 target

| Feature | Type | Description |
|---|---|---|
| Age | Numerical | Applicant's age |
| Sex | Categorical | male / female |
| Job | Ordinal | 0 = unskilled non-resident -> 3 = highly skilled |
| Housing | Categorical | own / rent / free |
| Saving accounts | Categorical | little / moderate / quite rich / rich |
| Checking account | Categorical | little / moderate / rich |
| Credit amount | Numerical | Loan amount in Deutsche Mark (DM) |
| Duration | Numerical | Loan term in months |
| Purpose | Categorical | car / furniture / radio/TV / education / etc. |
| **Risk** | **Target** | **good / bad** |


---

## ⚙️ ML Pipeline

### 1. Exploratory Data Analysis
- Distribution of target classes (700 good vs 300 bad - imbalanced)
- Feature distributions, correlation analysis, and categorical breakdowns via Matplotlib & Seaborn

### 2. Preprocessing
- Dropped the irrelevant index column
- Applied `LabelEncoder` per categorical column (encoders saved as `.pkl` for inference)
- Encoded target: `good -> 1`, `bad -> 0`

### 3. Model Training & Hyperparameter Tuning

All models tuned using `GridSearchCV` with `cv=5`. Class imbalance addressed via `class_weight='balanced'` (or `scale_pos_weight` for XGBoost).

| Model | Best Accuracy | 
|---|---|
| Decision Tree | 67.5% | 
| **Random Forest** ✅ |  75.0% |
| Extra Trees | 71.5% |
| XGBoost | 72.5% | 


### 5. Model Serialization
The best Random Forest model and all label encoders are saved with `pickle` for clean inference inside the Streamlit app.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/aryanguptacsvtu/Machine-Learning-Projects.git
cd "Machine-Learning-Projects/12_Credit Risk Modelling"
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the model 
Open `Code.ipynb` in Jupyter and run all cells to retrain and regenerate the `.pkl` files.

### 4. Launch the app
```bash
streamlit run frontend.py
```

---

## 🛠️ Tech Stack

| Library | Purpose |
|---|---|
| Pandas & NumPy | Data loading and preprocessing |
| Matplotlib & Seaborn | EDA and visualization |
| Scikit-learn | Model training, GridSearchCV, LabelEncoder |
| XGBoost | Gradient boosted classifier |
| Pickle | Model and encoder serialization |
| Streamlit | Interactive web application |

---

## 👨‍💻 Author

**Aryan Gupta**
🔗 [GitHub Profile](https://github.com/aryanguptacsvtu)

---

## ⭐ Support

If you found this project useful, please leave a ⭐ and share it with others!
