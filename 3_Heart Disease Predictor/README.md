# 🫀 Heart Disease Predictor

A multi-model machine learning app built with Streamlit to predict the likelihood of heart disease based on patient data.

---

## ✨ Features

-   **Multi-Model Prediction:** Get simultaneous predictions from four different models (Logistic Regression, SVM, Decision Tree, and Random Forest).
-   **Single Prediction:** Fill out a simple web form with 11 patient features to get an instant, color-coded result.
-   **Bulk Prediction:** Upload a CSV file of multiple patients to get batch predictions and download the results.
-   **Model Insights:** An interactive Plotly chart displays the validation accuracies of all trained models.
-   **Polished UI:** A clean, tabbed interface built with Streamlit components and custom CSS for a "card" layout.

---

## 🛠️ How It Works

This classifier uses several **supervised machine learning** models. The core logic is split into two parts:

1.  **Model Training :**
    * Four different classifiers (Logistic Regression, Support Vector Machine, Decision Tree, and Random Forest) were trained on a heart disease dataset.
    * The models were trained to predict a binary outcome (0 for No Disease, 1 for Disease) based on 11 input features (Age, Sex, ChestPainType, etc.).
    * The trained models were serialized and saved as `.pkl` files (e.g., `LogisticRegression.pkl`, `RandomForest.pkl`).

2.  **Streamlit App (app.py):**
    * Loads all four pre-trained `.pkl` models.
    * **Predict Tab:** Takes 11 user inputs from sliders and dropdowns, converts them to the required numeric format, and feeds them to all four models. It then displays each model's result (e.g., "✅ Result: No Heart Disease Detected" or "⚠️ Result: Heart Disease Detected").
    * **Bulk Predict Tab:** Allows a user to upload a CSV. It validates the columns, then uses the `LogisticRegression.pkl` model to predict the outcome for each row, adding a new `Prediction LR` column to the DataFrame. The user can then download this new CSV.
    * **Model Information Tab:** Renders a `plotly.express` bar chart from a hard-coded dictionary of model accuracies for user reference.

---

## 🚀 Tech Stack

* **Core:** Python, Scikit-Learn
* **Web Framework:** Streamlit
* **Data Handling:** NumPy, Pandas, Pickle
* **Data Visualization:** Plotly

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

3.  **Run the Jupyter Notebook :**

    If you want to train the model yourself, run the `Code.ipynb` notebook. This will use the `heart.csv` file  to generate the pickle files.


4.  **Ensure Model Files are Present:**
   
    This app requires the pre-trained model files to be in the same root directory. Make sure you have:
    * `LogisticRegression.pkl`
    * `SVM.pkl`
    * `DecisionTree.pkl`
    * `RandomForest.pkl`


6.  **Run the application:**
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
