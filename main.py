import requests
import streamlit as st
import pickle
import pandas as pd

def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=a1a92a51f514dcf758ee98489b8f9787&language=en-US")
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
def fetch_time(movie_id):
    response = requests.get(
        "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
            movie_id))
    data = response.json()
    return data['runtime']

def fetch_rating(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
            movie_id))
    data = response.json()
    return data['vote_average']


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_runtime = []
    votes = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_runtime.append(fetch_time(movie_id))
        votes.append(fetch_rating(movie_id))

    return recommended_movie_names, recommended_movie_posters, recommended_movie_runtime, votes


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))
st.title("Movies By Choice")

selected_movie_name = st.selectbox('What would you like to watch?', movies['title'].values)

if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters,runtime, votes = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
        st.text(f"{runtime[0]} mins")
        st.text(f"{votes[0]} rating")
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
        st.text(f"{runtime[1]} mins")
        st.text(f"{votes[1]} rating")
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
        st.text(f"{runtime[2]} mins")
        st.text(f"{votes[2]} rating")
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
        st.text(f"{runtime[3]} mins")
        st.text(f"{votes[3]} rating")
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
        st.text(f"{runtime[4]} mins")
        st.text(f"{votes[4]} rating")