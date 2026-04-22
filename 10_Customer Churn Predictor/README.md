# 📞 Telco Customer Churn Predictor

A machine learning-powered web application that predicts whether a telecom customer is likely to **churn** (cancel their subscription). Built with a Random Forest classifier trained on the IBM Telco Customer Churn dataset and served via an interactive Streamlit interface.

| Safe Customer | High-Risk Customer |
|:---:|:---:|
| ✅ Likely to Stay | ⚠️ Likely to Churn |

---

## 🗂️ Project Structure

```
Telco_Customer_Churn_Predictor/
│
├── Code.ipynb                   # Full ML pipeline
├── frontend.py                  # Streamlit web application
├── Telco-Customer-data.csv      # Dataset 
└── README.md
```

---

## 📊 Dataset

**Source:** [IBM Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

| Property | Detail |
|---|---|
| Rows | ~7,043 customers |
| Features | 20 (demographics, services, account info) |
| Target | `Churn` — Yes / No |

**Key Features:**

- **Demographics:** Gender, Senior Citizen, Partner, Dependents
- **Account Info:** Tenure, Contract Type, Billing Method, Monthly & Total Charges
- **Services:** Phone, Internet, Streaming, Security, Tech Support, and more

---

## 📚 ML Pipeline

### 1. Exploratory Data Analysis (EDA)
- Distribution plots  for numerical features
- Box plots for outlier detection
- Correlation heatmap for numerical columns
- Count plots segmented by churn for all categorical features

### 2. Data Preprocessing
- Cleaned whitespace entries in `TotalCharges` and cast to `float`
- Dropped `customerID` (non-informative)
- Applied `LabelEncoder` to all categorical columns 

### 3. Handling Class Imbalance
- Used **SMOTE** (Synthetic Minority Oversampling Technique) on the training set to balance churn vs. non-churn classes before model training

### 4. Model Training & Evaluation

Three models were benchmarked using **5-fold cross-validation**:

| Model | CV Accuracy |
|---|---|
| Decision Tree | ~78% |
| **Random Forest** | **~84%** ✅ |
| XGBoost | ~83% |

> **Random Forest** was selected as the final model for its superior accuracy and robustness.

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install -r requirements.txt
```

### Run the App

```bash
# Clone the repo
git clone https://github.com/aryanguptacsvtu/Machine-Learning-Projects.git
cd "Machine-Learning-Projects/7_Telco_Customer_Churn_Predictor"
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the Model
Open and run `Code.ipynb` end-to-end. This will generate the  `encoders.pkl` ,  `customer_churn_model.pkl` file in the same directory.

### 4. Launch the Web App
```bash
streamlit run frontend.py
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| `pandas` / `numpy` | Data manipulation |
| `matplotlib` / `seaborn` | EDA & visualization |
| `scikit-learn` | ML models, Label Encoding, train-test split |
| `imbalanced-learn` | SMOTE oversampling |
| `xgboost` | Gradient boosting benchmark |
| `pickle` | Model & encoder serialization |
| `streamlit` | Interactive web UI |

---

## 👨‍💻 Author

**Aryan Gupta**
🔗 [GitHub Profile](https://github.com/aryanguptacsvtu)

---

## ⭐ Support

If you found this project useful, please leave a ⭐ and share it with others!
