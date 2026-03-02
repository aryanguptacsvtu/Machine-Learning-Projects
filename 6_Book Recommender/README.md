# 📚 Book Recommendation System


A smart **Book Recommendation System** built with two complementary approaches -- **Popularity-Based Filtering** and **Collaborative Filtering**. The system helps users discover books they'll love, whether they're new to reading or already have a favourite in mind.

---

## 🎯 Features

- 🔥 **Popular Books Page** -- Displays the top books ranked by average user rating (with a minimum vote threshold for credibility)
- 🔍 **Personalised Recommendations** --- Enter any book title and get 5 similar books based on real reader behaviour
- 🖼️ Clean card-based UI with book covers, author names, ratings, and vote counts
- ⚡ Fast inference using pre-computed cosine similarity scores

---

## 🧠 How It Works

### 1. Popularity-Based Recommender
Recommends the most well-loved books across all users by:
- Counting total ratings per book
- Filtering books with **≥ 250 ratings** (to ensure statistical reliability)
- Sorting by **average rating** in descending order

### 2. Collaborative Filtering (Item-Based)
Finds books similar to a user's choice by:
- Filtering only **active users** (those with > 200 ratings) to reduce noise
- Keeping only **popular books** (rated by ≥ 50 active users)
- Building a **Book × User pivot table** of ratings
- Computing **Cosine Similarity** between all book vectors
- Returning the top 5 most similar books

---

## 📂 Project Structure

```
6_Book Recommender/
│
├── Code.ipynb              # Data preprocessing, model building & pickle export
├── frontend.py             # Streamlit web application
│
├── books.csv               # Book metadata (title, author, ISBN, image URL)
├── users.csv               # User demographics
├── ratings.csv             # User-book ratings (1.1M rows)
│
├── popular.pkl             # Serialised popularity DataFrame
├── pt.pkl                  # Serialised pivot table (Book × User)
├── books.pkl               # Serialised books DataFrame
└── similarity_scores.pkl   # Serialised cosine similarity matrix
```

---

## 📊 Dataset

The project uses the **Book-Crossing Dataset**, which contains:

| File | Records | Description |
|------|---------|-------------|
| `books.csv` | 271,360 | Book metadata -- title, author, year, publisher, cover images |
| `users.csv` | 278,858 | User info -- ID, location, age |
| `ratings.csv` | 1,149,780 | Explicit & implicit ratings (scale 0–10) |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/aryanguptacsvtu/Machine-Learning-Projects.git
cd "Machine-Learning-Projects/6_Book Recommender"
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate model files
Run the Jupyter notebook to process the data and produce the `.pkl` files:
```bash
jupyter notebook Code.ipynb
```

### 4. Launch the app
```bash
streamlit run frontend.py
```

---

## 🖥️ App Preview

| Home - Popular Books | Recommend - Similar Books |
|---|---|
| Displays top-rated books with cover art, author, ⭐ rating, and vote count | Select any book from the dropdown and click **✨ Recommend** to get 5 personalised suggestions |

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| **Python** | Core language |
| **Pandas & NumPy** | Data manipulation |
| **Scikit-learn** | Cosine similarity computation |
| **Streamlit** | Web application frontend |
| **Pickle** | Model serialisation |

---


## 👨‍💻 Author

**Aryan Gupta**  
📍 Bhilai, Chhattisgarh  
🔗 [GitHub Profile](https://github.com/aryanguptacsvtu)

---

## ⭐ Support

If you found this project helpful, please give it a ⭐ and share it with fellow readers!

---