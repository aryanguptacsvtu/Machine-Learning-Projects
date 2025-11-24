# 💻 Laptop Price Predictor

A machine learning–powered **Streamlit web application** that predicts laptop prices based on detailed hardware and software specifications.  

---

## ✨ Features

- **Interactive User Interface**  
  Organized into tabs for Core Specs, Hardware, and Display.

- **Automatic Feature Engineering**  
  Computes PPI, converts touchscreen/IPS flags, and parses screen resolution.

- **Preprocessing + Model Pipeline**  
  One `pipe.pkl` handles encoding, transformations, and prediction.

- **Dataset Preview**  
  View a sample of the training data (`df.pkl`) directly from the sidebar.

- **Modern Styled UI**  
  Includes gradient buttons, rounded cards, shadows, and custom CSS.

- **Realistic Pricing Output**  
  Model predicts log-price -> app returns actual price in Indian Rupees.

---

## 🛠️ How It Works

### 1. Training Pipeline (Code.ipynb)

The Jupyter notebook performs:

- Data cleaning and preprocessing  
- Feature extraction:
  - Company (Brand) , Type (Notebook/Gaming/Ultrabook etc.)
  - CPU brand , GPU brand
  - RAM , HDD & SSD storage
  - Operating system , Touchscreen & IPS flags
  - Resolution → **PPI calculation**
- Encoding categorical features using Label Encoding / One-Hot Encoding 
- Training various regression models (XGBRegressor, Random Forest, Gradient Boosting, etc.)
- Comparing performance and selecting the best pipeline
- Saving final artifacts:

```
pipe.pkl → Preprocessing + ML model
df.pkl → Cleaned dataset (used in Streamlit UI dropdowns)
```

### 2. Streamlit App (frontend.py)

The UI is built with Streamlit and includes custom CSS styling.  
It performs the following operations:

- Loads `pipe.pkl` and `df.pkl`  
- Displays selectable inputs for:
  - Brand, Laptop Type, CPU/GPU, OS  
  - RAM, HDD, SSD, Laptop Weight  
  - Screen Size, IPS Panel, Touchscreen  
  - Resolution (e.g., 1920x1080, 3840x2160)
- Computes internal features:
  - **Touchscreen → 0/1**
  - **IPS → 0/1**
  - **PPI → Derived pixel density**
  
- Formats the prediction:
  ```python
  prediction = int(np.exp(pipe.predict(query)[0]))
    ```
---

## 🚀 Tech Stack

* **Core:** Python, Scikit-Learn
* **Web Framework:** Streamlit
* **Data Handling:** NumPy, Pandas, Pickle
* **Data Visualization:** Matplotlib, Seaborn (Notebook)

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

    If you want to train the model yourself, run the `Code.ipynb` notebook. This will use the `laptop_data.csv` file  to generate the pickle files.


4.  **Ensure Model Files are Present:**
   
    You must have the following files in the same directory:

    - ```pipe.pkl```

    - ```df.pkl```

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
