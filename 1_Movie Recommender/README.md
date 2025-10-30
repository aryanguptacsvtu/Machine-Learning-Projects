
# 🎬 Movie Recommender System

A content-based movie recommendation system built with Streamlit and Python. Select a movie you like, and the app will suggest similar films based on their content (cast, crew, genres, and keywords).

---
## ✨ Features

* **Interactive UI:** Select from thousands of movies in a user-friendly dropdown.
* **Detailed Movie Info:** View the selected movie's poster, plot, and release year, fetched live from the OMDb API.
* **Content-Based Recommendations:** Get personalized recommendations based on content similarity.
* **Customizable Output:** Use the sidebar slider to choose how many recommendations (3 to 9) you want to see.
* **Modern Design:** A clean, card-based layout with custom CSS for a polished look.

---

## 🛠️ How It Works

This recommender uses a **content-based filtering** model. The core logic is split into two parts:

1.  **Offline Preprocessing (The "Brain"):**
    * Key movie features (genres, keywords, cast, crew) are combined into a single "tags" vector for each film.
    * **Cosine Similarity** is calculated between all movie vectors to create a similarity matrix.
    * This matrix (the "brain" of the recommender) is saved as `similarity.pkl`.

2.  **Live Streamlit App (The "Face"):**
    * When you select a movie, the app finds its row in the pre-computed similarity matrix.
    * It sorts this row to find the top 'N' most similar movies.
    * The **OMDb API** is then called to fetch and display the posters, plots, and details for these recommendations in real-time.

---

## 🚀 Tech Stack

* **Core:** Python , Scikit-Learn
* **Web Framework:** Streamlit
* **Data Handling:** Numpy , Pandas, Pickle
* **API:** Requests (for OMDb API)
---

## 📦 Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
```bash
    git clone https://github.com/your-username/Machine-Learning-Projects.git
    cd your-repo-name
```

2.  **Install the required libraries:**
  
  You can install all Python packages using the provided requirements.txt file.
```bash
    pip install -r requirements.txt
```



3.  **Get Your API Key:**
    * This project uses the **OMDb API** to fetch movie posters and details.
    * Sign up for a free API key at [omdbapi.com/apikey.aspx](https://www.omdbapi.com/apikey.aspx).

4.  **Add API Key :**
   
```toml
    [omdb_api_key]
    api_key = "YOUR_API_KEY_HERE"
```
5.  **Run the application:**
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