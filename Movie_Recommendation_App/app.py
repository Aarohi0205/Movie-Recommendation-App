

import streamlit as st
import numpy as np
import pandas as pd
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=4ece3aff6e946ebe2b31607357e6ff16&language=en-US'.format(movie_id))
    data = response.json()  
    
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path'] 


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x: x[1])[1:11] 

    recommended_movies = []
    recommend_movies_posters = []
    release_dates = []
    vote_averages = []  
    tags_fill = []  

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id 
                
        recommended_movies.append(movies.iloc[i[0]].title)
        release_dates.append(movies.iloc[i[0]].release_date)
        vote_averages.append(movies.iloc[i[0]].vote_average)  
        tags_fill.append(movies.iloc[i[0]].tags)  
        print("Movie ID:", movie_id, type(movie_id))
        # fetch poster from API 
        recommend_movies_posters.append(fetch_poster(movie_id))  
    return recommended_movies, recommend_movies_posters, release_dates, vote_averages, tags_fill





movies_dict = pickle.load(open("models/movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("models/similarity.pkl", "rb"))


# page configuartion  
st.set_page_config(
    page_title="Movie Recommendation App",
    page_icon="🎬",
    layout="wide"
)




st.title('Movie Recommender App') 

selected_movie_name = st.selectbox('Search the Movies Names ', movies["title"].values)


if st.button('Recommend'):
    names, posters, dates, ratings, tags_fill = recommend(selected_movie_name)

    # ---------- First Row ----------
    cols = st.columns(5)

    for i in range(5):
        with cols[i]:

            if posters[i]:
                st.image(posters[i], width="stretch")
            else:
                st.write("Poster Not Available")  

            stars = round(ratings[i] / 2)
            star_text = "⭐" * stars  


            st.markdown(
                f"""
                <div style="
                    height:130px;
                    text-align:center;
                    overflow:hidden;
                ">

                <div style="
                    color:gold;
                    font-size:18px;
                    font-weight:bold;
                ">
                    {star_text} ({ratings[i]:.1f}/10)
                </div>

                <div style="
                    font-weight:bold;
                    font-size:16px;
                    margin-top:5px;
                ">
                    {names[i]}
                </div>

                <div style="
                    color:gray;
                    font-size:14px;
                ">
                    Release: {dates[i]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )
            
            st.markdown("<br>", unsafe_allow_html=True)

            st.caption(tags_fill[i][:100] + "...")


    # ---------- Second Row ----------
    cols = st.columns(5)

    for i in range(5, 10):
       with cols[i-5]:

            st.image(posters[i], width="stretch")

            st.markdown(
                f"""
                <div style="
                    height:130px;
                    text-align:center;
                    overflow:hidden;
                ">

                <div style="
                    color:gold;
                    font-size:18px;
                    font-weight:bold;
                ">
                    {star_text} ({ratings[i]:.1f}/10)
                </div>

                <div style="
                    font-weight:bold;
                    font-size:16px;
                    margin-top:5px;
                ">
                    {names[i]}
                </div>

                <div style="
                    color:gray;
                    font-size:14px;
                ">
                    Release: {dates[i]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )


            st.caption(tags_fill[i][:100] + "...")


# fourth file 


