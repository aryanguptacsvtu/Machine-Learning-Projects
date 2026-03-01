import streamlit as st
import pickle
import numpy as np

# ---------------------------
# Load Data
# ---------------------------
popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

st.set_page_config(
    page_title="Book Recommender",
    layout="wide")

# ---------------------------
# Minimal Styling
# ---------------------------
st.markdown("""
<style>
.card {
    background-color: #ffffff;
    padding: 12px;
    border-radius: 12px;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.08);
    text-align: center;
    margin-bottom: 15px;
}
.title {
    font-size: 15px;
    font-weight: 600;
}
.author {
    font-size: 13px;
    color: #666;
}
.badge {
    font-size: 12px;
    color: #444;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Header
# ---------------------------
st.markdown("## 📚 Book Recommendation System")
st.caption("Simple and smart book discovery")

# ---------------------------
# Sidebar Navigation
# ---------------------------
menu = st.sidebar.radio("📌 Navigation", ["Home", "Recommend"])

# ---------------------------
# HOME PAGE
# ---------------------------
if menu == "Home":
    st.subheader("🔥 Popular Books")

    cols = st.columns(5)

    for i in range(10):
        with cols[i % 5]:
            st.image(
                popular_df['Image-URL-M'].values[i],
                use_container_width=True
            )

            st.markdown(
                f"""
                <div class="card">
                    <div class="title">{popular_df['Book-Title'].values[i]}</div>
                    <div class="author">{popular_df['Book-Author'].values[i]}</div>
                    <div class="badge">⭐ {popular_df['avg_rating'].values[i]}</div>
                    <div class="badge">🗳 {popular_df['num_ratings'].values[i]} votes</div>
                </div>
                """,
                unsafe_allow_html=True
            )

# ---------------------------
# RECOMMEND PAGE
# ---------------------------
else:
    st.subheader("🔍 Find Similar Books")

    user_input = st.selectbox(
        "Choose a book",
        pt.index.values
    )

    if st.button("✨ Recommend"):
        index = np.where(pt.index == user_input)[0][0]

        similar_items = sorted(
            list(enumerate(similarity_scores[index])),
            key=lambda x: x[1],
            reverse=True
        )[1:6]

        st.markdown("### 📖 You May Also Like")

        rec_cols = st.columns(5)

        for idx, i in enumerate(similar_items):
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]

            title = temp_df.drop_duplicates('Book-Title')['Book-Title'].values[0]
            author = temp_df.drop_duplicates('Book-Title')['Book-Author'].values[0]
            image = temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values[0]

            with rec_cols[idx]:
                st.image(image, use_container_width=True)

                st.markdown(
                    f"""
                    <div class="card">
                        <div class="title">{title}</div>
                        <div class="author">{author}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
