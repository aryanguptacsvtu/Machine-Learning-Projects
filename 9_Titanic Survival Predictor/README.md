# 🚢 Titanic Survival Predictor

A machine learning project that predicts whether a Titanic passenger would have survived, based on passenger details. The project comes with a user-friendly Streamlit prediction interface.

---

## 🗂️ Project Structure

```
Titanic-Survival-Predictor/
│
├── Code.ipynb          # Jupyter Notebook
├── frontend.py         # Streamlit web app 
├── train.csv           # Titanic training dataset
└── README.md
```

---

## 🔍 Workflow

### 1. Exploratory Data Analysis (EDA)
- Examined survival distribution, class distribution, and gender-survival relationship
- Visualized patterns using `seaborn` and `matplotlib`

### 2. Data Preprocessing
- Dropped the `Cabin` column (too many missing values)
- Filled missing `Age` values with the column mean
- Filled missing `Embarked` values with the mode
- Label-encoded categorical features:
  - `Sex`: male → 0, female → 1
  - `Embarked`: S → 0, C → 1, Q → 2
- Dropped non-predictive columns: `PassengerId`, `Name`, `Ticket`

### 3. Model Training & Evaluation
Four classifiers were trained and evaluated on an 80/20 train-test split:

| Model                  | Test Accuracy |
|------------------------|--------------|
| Logistic Regression    | ~80%         |
| Decision Tree          | ~78%         |
| **Random Forest** ✅   | **~81%**     |
| Support Vector Machine | ~65%         |

> **Random Forest** was selected as the best model and serialized using `pickle`.

### 4. Deployment
The trained model is served via a Streamlit app that accepts passenger inputs and returns a real-time survival prediction.

---

## 🧠 Features Used for Prediction

| Feature    | Description                                              |
|------------|----------------------------------------------------------|
| `Pclass`   | Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)                |
| `Sex`      | Gender of the passenger                                  |
| `Age`      | Age of the passenger in years                            |
| `SibSp`    | Number of siblings/spouses aboard                        |
| `Parch`    | Number of parents/children aboard                        |
| `Fare`     | Ticket fare paid                                         |
| `Embarked` | Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton) |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Scikit-learn | ML pipeline, models, evaluation |
| Pandas / NumPy | Data manipulation |
| Matplotlib / Seaborn | Visualization |
| Streamlit | Web app frontend |
| Pickle | Model serialization |

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/aryanguptacsvtu/Machine-Learning-Projects.git
cd Machine-Learning-Projects/Titanic-Survival-Predictor
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the Model
Open and run `Code.ipynb` end-to-end. This will generate the `rf_model.pkl` file in the same directory.

### 4. Launch the Web App
```bash
streamlit run frontend.py
```


---
## 👨‍💻 Author

**Aryan Gupta**
🔗 [GitHub Profile](https://github.com/aryanguptacsvtu)

---

## ⭐ Support

If you found this project useful, please leave a ⭐ and share it with others!
