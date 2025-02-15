import streamlit as st
import pickle
from scipy.spatial import distance

# Redefine the compute_distance function in the script
def compute_distance(a, b):
    description_distance = distance.cosine(a[1], b[1])  # Compute cosine distance between descriptions
    popularity_distance = abs(a[2] - b[2])  # Difference in ratings size
    return description_distance + popularity_distance

# Load the movie dictionary and the top correlated movies function
with open('movie_dict.pkl', 'rb') as f:
    movie_dict = pickle.load(f)

# Create a reverse mapping for ID to name and name to ID
id_to_name = {movie_info[0]: movie_id for movie_id, movie_info in movie_dict.items()}
name_to_id = {name: movie_id for movie_id, (name, _, _, _) in movie_dict.items()}

def get_top_correlated_movies(movie_dict, input_movie_id, top_n=10):
    # Ensure the input movie exists in the dictionary
    if input_movie_id not in movie_dict:
        print(f"Movie with ID {input_movie_id} not found.")
        return []

    input_movie = movie_dict[input_movie_id]
    distances = []

    # Calculate the distance between the input movie and all other movies
    for movie_id, movie_info in movie_dict.items():
        if movie_id != input_movie_id:  # Avoid comparing the movie with itself
            distance = compute_distance(input_movie, movie_info)
            distances.append((movie_id, distance))
    
    # Sort by distance and get the top N closest movies
    distances.sort(key=lambda x: x[1])
    top_correlated_movies = distances[:top_n]
    
    return top_correlated_movies

# Streamlit app title and header
st.title("Movie Correlation Finder")
st.header("Choose between two modes: Compare two movies or find top 10 correlated movies")

# Option 1: Compare two movies
st.subheader("Compare Two Movies")
movie_names = list(name_to_id.keys())
movie_name_1 = st.selectbox("Select Movie 1", movie_names, key="movie_1")
movie_name_2 = st.selectbox("Select Movie 2", movie_names, key="movie_2")

if st.button("Compute Distance Between Movies"):
    movie_id_1 = name_to_id[movie_name_1]
    movie_id_2 = name_to_id[movie_name_2]
    
    movie_a = movie_dict[movie_id_1]
    movie_b = movie_dict[movie_id_2]
    
    distance_result = compute_distance(movie_a, movie_b)
    st.write(f"The correlation distance between {movie_name_1} and {movie_name_2} is {distance_result:.2f}")

# Option 2: Find top correlated movies for a given movie
st.subheader("Find Top Correlated Movies")
input_movie_name = st.selectbox("Select a Movie Name", movie_names, key="input_movie")
top_n = st.number_input("Number of top correlated movies", min_value=1, max_value=25, value=10)

if st.button("Find Correlated Movies"):
    input_movie_id = name_to_id[input_movie_name]
    top_correlated_movies = get_top_correlated_movies(movie_dict, input_movie_id, top_n)
    
    st.write(f"Top {top_n} movies correlated with {input_movie_name}:")
    for movie_id, distance_value in top_correlated_movies:
        correlated_movie_name = movie_dict[movie_id][0]  # Get movie name from ID
        st.write(f"{correlated_movie_name} has a correlation distance of {distance_value:.2f}")
