
import pandas as pd
import ast
import pickle


# Now we load first_cleaned_movies.csv file

movies = pd.read_csv("dataset/first_cleaned_movies.csv") 


# Helper Functions

def convert_genres(text):
    """
    Extract names from JSON like genres columns.
    [{'id': 28, 'name': 'Action'},
    {'id': 12, 'name': 'Adventure'},
    {'id': 14, 'name': 'Fantasy'},
    {'id': 878, 'name': 'Science Fiction'}]

    """

    L = []  # empty list

    try:
        for i in ast.literal_eval(text):
            L.append(i['name'])
    except:
        pass 

    return L 


def conver_cast(text):
    """
    Extract only top 3 cast members because very large collection given of cast members.
    """
    L = []

    try:
        counter = 0   # 0,1,2
        for i in ast.literal_eval(text):
            if counter < 3:
                L.append(i['name'])
                counter += 1
            else:
                break
    except:
        pass

    return L 


def fetch_director(text):
    """
    Extract Director name from crew column.
    """

    L = []

    try:
        for i in ast.literal_eval(text):
            if i['job'] == 'Director':
                L.append(i['name'])
                break
    except:
        pass

    return L 


# Feature Engineering 

movies["genres"] = movies["genres"].apply(convert_genres)
movies["keywords"] = movies["keywords"].apply(convert_genres)
movies["cast"] = movies["cast"].apply(conver_cast) 
movies["crew"] = movies["crew"].apply(fetch_director) 


# Convert overview string to a list of words 
movies["overview"] = movies["overview"].apply(lambda x: x.split())


# Remove space from names/words like treat multi-words as a single tags 
# like = multi-words - Sam Worthington before and after single tags - SamWorthington 
# another example = multi-words - Science Fiction before and afte single tags - ScienceFiction
# we apply columns are - overview, genres, keywords, cast and crew 

movies["genres"] = movies["genres"].apply(
    lambda x: [i.replace(" ","") for i in x] 
)


movies["keywords"] = movies["keywords"].apply(
    lambda x: [i.replace(" ","") for i in x] 
)


movies["cast"] = movies["cast"].apply(
    lambda x: [i.replace(" ","") for i in x] 
)

movies["crew"] = movies["crew"].apply(
    lambda x: [i.replace(" ","") for i in x] 
)



# Now, We combine all features into a single 'tags' column
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew'] 


movies = movies[['movie_id','title','tags','release_date','vote_average']]

movies['tags'] = movies['tags'].apply(lambda x: " ".join(x)) 
# movies['tags'] = movies['tags'].apply(lambda x: x.lower()) 
movies['tags'] = movies['tags'].str.lower() 

movies.to_csv('dataset/second_cleaned_movies.csv', index=False)
print("\n merged column successfully") 

# second file 