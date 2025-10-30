import streamlit as st
import pickle
import pandas as pd
import requests

# --- Page Configuration ---
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# --- CSS Styling ---
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
:root {
    --primary-color: #3498db; /* A nice blue */
    --background-color: #f0f2f6; /* Light grey background */
    --card-bg-color: #ffffff; /* White cards */
    --text-color: #333333; /* Dark grey text */
    --subtle-text-color: #555555;
    --shadow-color: rgba(0, 0, 0, 0.1);
}
body {
    font-family: 'Poppins', sans-serif;
    background-color: var(--background-color);
    color: var(--text-color);
}
.card {
    background-color: var(--card-bg-color);
    border-radius: 10px;
    box-shadow: 0 4px 8px var(--shadow-color);
    transition: all 0.3s ease;
    overflow: hidden;
    height: 100%;
    display: flex;
    flex-direction: column;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px var(--shadow-color);
}
.card img {
    width: 100%;
    height: auto;
}
.card-text {
    padding: 15px;
    text-align: center;
    flex-grow: 1;
}
.card-text h5 { margin: 0; font-weight: 600; font-size: 1rem; }
.card-text p { margin: 5px 0 0 0; font-size: 0.8rem; color: var(--subtle-text-color); }
.stButton > button {
    border-radius: 20px;
    border: 1px solid var(--primary-color);
    background-color: var(--primary-color);
    color: white;
    padding: 10px 24px;
    font-weight: 600;
    transition: all 0.3s ease;
}
.stButton > button:hover {
    background-color: white;
    color: var(--primary-color);
    border: 1px solid var(--primary-color);
}
h1 { color: var(--primary-color); text-align: center; }
"""
st.markdown(f'<style>{CSS}</style>', unsafe_allow_html=True)

# --- Load Data ---
@st.cache_data
def load_data():
    movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity

movies, similarity = load_data()


# --- API Call and HTML Template Functions ---
def fetch_movie_details(movie_title):
    try: api_key = st.secrets["omdb_api_key"]
    except (FileNotFoundError, KeyError): api_key = 'your_api_key_here' # Fallback key

    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get('Response') == 'True':
            poster = data.get('Poster', "https://via.placeholder.com/500x750.png?text=No+Poster")
            if poster == 'N/A': poster = "https://via.placeholder.com/500x750.png?text=No+Poster"
            return {"title": data.get('Title'), "year": data.get('Year'), "plot": data.get('Plot'), "poster": poster}
        return None
    except requests.exceptions.RequestException: return None

# Added **kwargs to accept and ignore extra arguments like 'plot'
def recommendation_card_html(title, year, poster, **kwargs):
    return f'<div class="card"><img src="{poster}" alt="{title} poster"><div class="card-text"><h5>{title}</h5><p>{year}</p></div></div>'

def selected_movie_html(title, year, plot, poster):
    return f'<div style="display: flex; gap: 20px; align-items: center; background-color: var(--card-bg-color); padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px var(--shadow-color);"><div style="flex: 1;"><img src="{poster}" style="width: 100%; max-width: 200px; border-radius: 8px;"></div><div style="flex: 3;"><h2 style="color: var(--primary-color);">{title} ({year})</h2><p style="color: var(--subtle-text-color); text-align: justify;">{plot}</p></div></div>'

# --- Recommendation Logic ---
def recommend(movie, num_recommendations=5):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:num_recommendations+1]
    recommended_movies_details = [fetch_movie_details(movies.iloc[i[0]].title) for i in movies_list]
    return [m for m in recommended_movies_details if m] # Filter out None values

# ***************************** MAIN UI **********************************************************************

st.title("🎬 Movie Recommender System")
st.markdown("---")

# --- Sidebar ---
with st.sidebar:
    st.header("Controls")
    num_recommendations = st.slider("Number of Recommendations", min_value=3, max_value=9, value=5, step=2)
    st.markdown("---")
    st.markdown("""
    This app uses a content-based filtering approach to recommend movies.
    Select a movie to see others with similar cast, crew, genre, and keywords.
    """)

# --- Movie Selection ---
selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown to get recommendations.",
    movies['title'].values,
    index=None,
    placeholder="Select a movie..."
)

# --- Display Recommendations ---
if selected_movie_name:
    selected_details = fetch_movie_details(selected_movie_name)
    if selected_details:
        st.markdown(selected_movie_html(**selected_details), unsafe_allow_html=True)
    else:
        st.error("Could not fetch details for the selected movie.")

    st.markdown("<br>", unsafe_allow_html=True) # Adding some space

    if st.button('Show Recommendations'):
        with st.spinner('Finding similar movies for you...'):
            recommendations = recommend(selected_movie_name, num_recommendations)
        
        st.markdown("---")
        st.subheader("Recommended For You")
        
        if recommendations:
            cols = st.columns(num_recommendations)
            for i, movie in enumerate(recommendations):
                with cols[i]:
                    st.markdown(recommendation_card_html(**movie), unsafe_allow_html=True)
        else:
            st.warning("Could not find any recommendations.")