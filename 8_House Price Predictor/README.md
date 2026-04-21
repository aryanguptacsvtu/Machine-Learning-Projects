# 🏡 California Housing Price Predictor

A machine learning web application that predicts **median house values** in California based on block-level housing features. 
The project comes with a user-friendly Streamlit prediction interface.

---

## 🗂️ Project Structure

```
House-Price-Predictor/
├── housing.csv          # Raw dataset
├── notebook.ipynb       # Full ML pipeline 
├── app.py               # Streamlit web application
├── model.pkl            # Serialized trained model
└── README.md
```

---

## 📊 Dataset

The dataset contains **20,640 records**, each representing a California census block group, with the following features:

| Feature | Description |
|---|---|
| `longitude` | How far west the house is (higher = farther west) |
| `latitude` | How far north the house is (higher = farther north) |
| `housing_median_age` | Median age of houses in the block |
| `total_rooms` | Total rooms within the block |
| `total_bedrooms` | Total bedrooms within the block |
| `population` | Total residents in the block |
| `households` | Total households in the block |
| `median_income` | Median household income (in tens of thousands USD) |
| `ocean_proximity` | Location relative to the ocean |
| `median_house_value` | ⭐ **Target** — Median house value (USD) |

---

## ⚙️ ML Pipeline

### 1. Exploratory Data Analysis
- Distribution plots for all numerical features
- Box plots for outlier detection
- Correlation heatmap with target variable
- Count plots for categorical features

### 2. Preprocessing
- **Numerical:** Median imputation + Standard Scaling
- **Categorical:** Most-frequent imputation + One-Hot Encoding

### 3. Model Selection (5-Fold Cross-Validation)

| Model | CV RMSE |
|---|---|
| Linear Regression | ~68,600 |
| Ridge | ~68,600 |
| Lasso | ~68,600 |
| Random Forest | ~49,300 |
| **HistGradientBoosting** | **~48,000** ✅ |

### 4. Hyperparameter Tuning (GridSearchCV)

Tuned `HistGradientBoostingRegressor` using GridSearch CV for best results.

### 5. Final Model Performance

| Split | RMSE | MAE | R² |
|---|---|---|---|
| Train | ~35,900 | ~24,000 | ~0.90 |
| Test | ~46,000 | ~30,000 | ~0.83 |

---

## 📦 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/aryanguptacsvtu/Machine-Learning-Projects.git
cd "Machine-Learning-Projects/House Price Predictor"
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the model

If you want to train the model from scratch, run all cells in:

```bash
jupyter notebook Code.ipynb
```

This will regenerate `model.pkl`

### 4. Launch the Streamlit app

```bash
streamlit run frontend.py
```

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
## 👨‍💻 Author

**Aryan Gupta**
🔗 [GitHub Profile](https://github.com/aryanguptacsvtu)

---

## ⭐ Support

If you found this project useful, please leave a ⭐ and share it with others!
