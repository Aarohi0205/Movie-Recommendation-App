
import pandas as pd
import ast
import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


movies = pd.read_csv('dataset/second_cleaned_movies.csv')

movies['release_date'] = pd.to_datetime(movies['release_date'])
# print(movies['release_date'])  # now format display in teminal - yyyy-mm-dd

# Using strftime to change the format
# To change the format of a date column in a Pandas DataFrame to "dd-mm-yyyy", you can use the dt.strftime method.

# movies['release_date'] = movies['release_date'].dt.strftime('%d-%m-%Y') # at a time this line use or below line use
movies['release_date'] = movies['release_date'].dt.strftime('%d-%B-%Y')  
# Hint -  %B = full month name = December and %b = short month name = Dec

# print(movies['release_date'])


# use for library 
# using text vectorization (Extract top 5000 features, remove English stop words)
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray() 

print("Vectors Shape: ", vectors.shape)     # Vectors Shape:  (4805, 5000)


# use for library # Cosine Similarity 

similarity = cosine_similarity(vectors) 
print("Similarity Matrix shape: ", similarity.shape)   # Similarity Matrix shape:  (4805, 4805)


sorted(list(enumerate(similarity[0])),reverse=True, key=lambda x: x[1])[1:11]

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x: x[1])[1:11] 

    for i in movies_list:
            print(movies.iloc[i[0]].title)


# print(recommend('Avatar'))     


# Now we Save Model

pickle.dump(
      movies, open('models/movies.pkl','wb') 
)

pickle.dump(
      similarity, open('models/similarity.pkl','wb') 
)

print(movies['title'].values)

pickle.dump(
      movies.to_dict(), open('models/movie_dict.pkl','wb')
)         


print('Models Saved Successfully')

# Third file 


