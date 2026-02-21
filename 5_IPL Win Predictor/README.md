# 🏏 IPL Win Predictor

A machine learning model that predicts the **win probability** of IPL teams during the second innings - ball by ball - based on live match conditions.

---

## 📌 Overview

This project uses historical IPL match data (2008–2019) to train a **Logistic Regression** classifier. Given the current state of a second-innings chase, the model outputs the probability of the batting team winning.

---

## 🎯 Features Used for Prediction

| Feature | Description |
|---|---|
| `batting_team` | Team currently batting |
| `bowling_team` | Team currently bowling |
| `city` | Venue city |
| `runs_left` | Runs still needed to win |
| `balls_left` | Deliveries remaining |
| `wickets` | Wickets in hand |
| `total_runs_x` | Target set by 1st innings team |
| `crr` | Current Run Rate |
| `rrr` | Required Run Rate |

---

## 📂 Dataset

Two CSV files are used:

- **`matches.csv`** --- Match-level data (756 matches across IPL 2008–2019): teams, toss, winner, venue, etc.
- **`deliveries.csv`** --- Ball-by-ball data (179,078 deliveries): runs, wickets, batsman, bowler, etc.

### Teams Included

> Only 8 active IPL franchises are retained for training:

```
Sunrisers Hyderabad     Mumbai Indians
Royal Challengers Bangalore    Kolkata Knight Riders
Kings XI Punjab         Chennai Super Kings
Rajasthan Royals        Delhi Capitals
```

*Defunct/renamed teams (Deccan Chargers → SRH, Delhi Daredevils → Delhi Capitals) are remapped. Teams like Gujarat Lions, Pune Warriors, and Kochi Tuskers Kerala are excluded.*

---
## 🚀 Tech Stack

* **Core:** Python, Scikit-Learn
* **Web Framework:** Streamlit
* **Data Handling:** NumPy, Pandas, Pickle
---

## 📦 Setup and Installation

### 1. Clone the repository
```bash
git clone https://github.com/aryanguptacsvtu/Machine-Learning-Projects.git
cd "Machine-Learning-Projects/5_IPL Win Predictor"
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the notebook
```bash
jupyter notebook Code.ipynb
```

### 4.  **Ensure Model Files are Present:**
   
  You must have the following file in the same directory: `pipe.pkl`


### 5.  **Run the application:**
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
