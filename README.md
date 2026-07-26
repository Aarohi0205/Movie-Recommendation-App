
🎬 Movie Recommendation App using Machine Learning
📌 Project Overview
The Movie Recommendation App is a Machine Learning project that recommends movies similar to the movie selected by the user. The recommendation is based on Content-Based Filtering, where movies are compared using their genres, keywords, cast, director,  overview, release_date and ratings.
The project is developed using Python, Scikit-learn, and Streamlit and uses the TMDB 5000 Movies Dataset from Kaggle.
________________________________________
Features
•	Recommend Top 10 similar movies
•	User-friendly Streamlit interface
•	Display movie posters using TMDB API
•	Show movie ratings
•	Show release dates
•	Show movie overview
•	Fast recommendation using Cosine Similarity
•	Easy to extend with more features
________________________________________
Technologies Used
•	Python
•	Pandas
•	NumPy
•	Scikit-learn
•	Streamlit
•	Requests
•	Pickle
________________________________________
Machine Learning Algorithm
This project uses Content-Based Movie Recommendation.
Workflow
1.	Load Dataset
2.	Data Cleaning
3.	Feature Engineering
4.	Text Preprocessing
5.	CountVectorizer
6.	Cosine Similarity
7.	Recommend Similar Movies
________________________________________
Dataset
Dataset Source:
TMDB 5000 Movies Dataset (Kaggle)
Files Used
•	movies.csv
•	credits.csv
________________________________________
Project Structure
Movie_Recommendation_System/
│
├── app.py
├── model_building.py
├── model.py
├── data_preprocessing.py
├── requirements.txt
├── README.md
│
├── dataset/
│   ├── first_cleaned_movies.csv
│   ├── second_cleaned_movies.csv   
│   ├── tmdb_5000_credits.csv
│   └── tmdb_5000_movies.csv
│
├── models/

    ├── movies_dict.pkl
│   ├── movies.pkl
│   └── similarity.pkl
│
├
│
└── notebook/
    └── movie.ipynb  
________________________________________
Installation
<!-- Clone the repository
git clone https://github.com/yourusername/Movie_Recommendation_App.git
Move into the project directory
cd Movie_Recommendation_App -->
<!-- comment line check again some mistake feels -->
Install dependencies
pip install -r requirements.txt
________________________________________
Run Data Preprocessing
python data_preprocessing.py
________________________________________
Train the Model
python model.py
This creates:
•	movies_dict.pkl
•	movies.pkl
•	similarity.pkl

________________________________________
Run the Streamlit App
python -m streamlit run app.py
________________________________________
How It Works
1.	The user selects a movie.
2.	The application finds that movie in the dataset.
3.	CountVectorizer converts movie tags into vectors.
4.	Cosine Similarity measures similarity between movies.
5.	The top ten most similar movies are recommended.
6.	Movie posters and details are fetched using the TMDB API.
________________________________________
Libraries Used
•	streamlit
•	pandas
•	numpy
•	scikit-learn
•	ast
•	pickle
•	requests
________________________________________
Future Improvements
•	Add search suggestions
•	Add movie trailers
•	Add filtering by genre
•	Add actor-based recommendations
•	Add collaborative filtering
•	Improve UI with custom CSS

________________________________________
Output
The application displays:
•	Recommended movie names
•	Movie posters
•	Ratings
•	Release dates
•	Movie overview
________________________________________
Learning Outcomes
After completing this project, you will understand:
•	Data preprocessing
•	Feature engineering
•	Natural Language Processing basics
•	CountVectorizer
•	Cosine Similarity
•	Content-Based Recommendation Systems
•	Streamlit application development
•	Model serialization using Pickle
________________________________________
Author
Name: Aarohi Tripathi
Project: Movie Recommendation App using Machine Learning
________________________________________
License
This project is created for educational and learning purposes.

