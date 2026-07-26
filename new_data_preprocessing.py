
import pandas as pd

# I will do Load the Dataset csv file
# download the Kaggle website
movies = pd.read_csv("dataset/tmdb_5000_movies.csv")
credits = pd.read_csv("dataset/tmdb_5000_credits.csv")  

print("Movies Shape: ", movies.shape)
# Movie Shape:  (4803, 20)      # 4803 rows and 20 columns 

print("Credits Shape: ", credits.shape) 
# Credits Shape: (4803, 4)      # 4803 rows and 4 columns 


# Now, I will both different dataset to convert Single dataset 
# to simplication on progress 
# Use pandas, property merge 

# Both dataset common columns is title then behave of title 
# column merge 
movies = movies.merge(credits, on="title")
print("New Dataset Shape:", movies.shape) 
# New Dataset Shape: (4809, 23) 


# And, Now will 23 total columns then I will have
# only some important columns to find movies in search box
# related necessary information 


movies = movies[["movie_id","title","overview","genres","keywords","cast","crew","release_date","vote_average"]]

print("Important Columns:", movies.columns)

# print(type("movies"))  # <class 'str'>


# We find missing values and total rows are 4809
print("Missing Values: \n",movies.isnull().sum())

# we find overview = 3, release_date = 1 missing values 
# we drop missing values
movies.dropna(inplace=True) 

print("Removing Missing values: ", movies.shape)
# removing total 4 missing values then total rows are 4805


# Now we remove duplicate values
movies.duplicated().sum()  
movies.drop_duplicates(inplace=True)  
print("Duplicate Rows after: ", movies.shape)

# No duplicated value find, now still rows are 4805 

# Saved Cleaned Data
movies.to_csv('dataset/first_cleaned_movies.csv', index=False)
print("\nData Preprocessing Saved Successfully!\n")
print("Clean Dataset Saved Successfully!\n")  



# first file 



