# 🩺 Diabetes Prediction System

A machine learning web application that predicts the likelihood of diabetes in a patient based on key health indicators. The trained model is served through an intuitive, interactive Streamlit web interface.

---

## 🧠 Model Details

| Property | Value |
|---|---|
| **Algorithm** | Support Vector Machine (SVM) |
| **Preprocessing** | Standard Scaler (zero mean, unit variance) |
| **Dataset** | [PIMA Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)|
| **Target** | Binary - `1` (Diabetic) / `0` (Not Diabetic) |
| **Saved Artifacts** | `svc_model.pkl`, `scaler.pkl` |

---

## 📊 Features Used

| Feature | Description | Typical Range |
|---|---|---|
| **Pregnancies** | Number of times pregnant | 0 – 17 |
| **Glucose** | Plasma glucose concentration (mg/dL) | 0 – 199 |
| **Blood Pressure** | Diastolic blood pressure (mm Hg) | 0 – 122 |
| **Skin Thickness** | Triceps skin fold thickness (mm) | 0 – 99 |
| **Insulin** | 2-hour serum insulin (mu U/ml) | 0 – 846 |
| **BMI** | Body Mass Index (kg/m²) | 0 – 67.1 |
| **Diabetes Pedigree Function** | Genetic risk score based on family history | 0.08 – 2.42 |
| **Age** | Age in years | 21 – 81 |

---

## 🗂️ Project Structure

```
7_Diabetes Predictor/
│
├── Code.ipynb          # Data analysis, model training & evaluation
├── frontend.py         # Streamlit web application
├── requirements.txt        
└── README.md           # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/aryanguptacsvtu/Machine-Learning-Projects.git
cd "Machine-Learning-Projects/7_Diabetes Predictor"
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the model

Open and run all cells in `Code.ipynb`. This will generate the two required pickle files:
 `svc_model.pkl` , `scaler.pkl`


### 4. Launch the app

```bash
streamlit run frontend.py
```

---

## 🔬 ML Pipeline

The notebook covers the full ML pipeline:

1. **Data Loading & Exploration** - shape, data types, null values, statistical summary
2. **Exploratory Data Analysis (EDA)** - distribution plots, correlation heatmaps, class balance check
3. **Preprocessing** - feature scaling with `StandardScaler`, train/test split
4. **Model Training** - SVM classifier with appropriate kernel and hyperparameters
5. **Evaluation** - accuracy score, confusion matrix, classification report
6. **Model Export** - saving model and scaler as `.pkl` files using `pickle`

---
## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| `pandas` / `numpy` | Data manipulation |
| `matplotlib` / `seaborn` | EDA & visualization |
| `scikit-learn` | ML models, Standardization, train-test split |
| `pickle` | Serialization |
| `streamlit` | Interactive web UI |

---

## ⚠️ Disclaimer

This application is built for **educational purposes only**. It is not intended to be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical concerns.

---

## 👨‍💻 Author

**Aryan Gupta**
🔗 [GitHub Profile](https://github.com/aryanguptacsvtu)

---

## ⭐ Support

If you found this project useful, please leave a ⭐ and share it with others!
