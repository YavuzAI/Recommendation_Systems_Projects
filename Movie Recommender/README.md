# Movie Recommendation System

This project focuses on building a **movie recommendation system** that computes similarity between films based on their **descriptions** and **popularity** metrics. By vectorizing movie descriptions and measuring **cosine distance**, the system can suggest which movies are most similar to a given film.

---

## Table of Contents
1. [Overview](#overview)  
2. [Data Processing](#data-processing)  
3. [Cosine Distance & Recommendation Logic](#cosine-distance--recommendation-logic)  
4. [Usage](#usage)  
5. [Future Improvements](#future-improvements)

---

## Overview
- **Goal**: Provide recommendations by identifying which movies are “closest” to a user-selected film.  
- **Method**: Leverage text-based similarity (movie descriptions) and an additional numeric metric (e.g., popularity) to compute an overall “distance” between pairs of movies.  
- **Libraries**: Primarily **pandas**, **numpy**, and **scipy** for data manipulation and distance calculations.

---

## Data Processing
1. **Reading & Cleaning**:  
   - Utilized libraries like **pandas** and **neattext** to clean and preprocess movie descriptions.  
   - Removed special characters, handled stop words, and standardized text.

2. **Vectorizing Descriptions**:  
   - Generated numerical representations (vectors) of movie descriptions.  
   - Created a **sparse matrix** to store these vectors efficiently, later converting it to a **DataFrame** for convenience.

3. **Data Structure**:  
   - Maintained a dictionary (`movie_dict`) or similar structure mapping each **movie ID** to its **title**, **vector representation**, and **popularity** score (or other numeric feature).

---

## Cosine Distance & Recommendation Logic
1. **Cosine Distance**:  
   - Measured how similar two movies are by comparing their description vectors.  
   - **Lower** cosine distance indicates **higher** similarity in text content.

2. **Popularity Distance**:  
   - Calculated the absolute difference in popularity scores between two movies.  
   - Summed this value with the description-based distance to get a final “distance” metric.

3. **Recommendation Steps**:  
   - **Compute Distance**: For any pair of movies, add up the **description distance** + **popularity distance**.  
   - **Sort Movies**: Identify the top “closest” or “most correlated” films by sorting distances in ascending order.  
   - **Select Top N**: Return the top N most similar movies for a given input film.

---

## Usage
1. **Load Data**: Import your movies and their descriptions/popularity data.  
2. **Vectorize Descriptions**: Use your preferred vectorization method (e.g., TF-IDF) to generate numeric representations.  
3. **Compute Distances**:  
   - Implement the distance function to compare movies.  
   - Loop through a set of candidate movies to find which ones are most similar.  
4. **Get Recommendations**:  
   - Use a function (e.g., `get_top_correlated_movies`) to fetch the top N similar movies given an **input movie ID**.  
   - The result includes the **distance** metric, allowing you to gauge how close two movies are.

---

## Future Improvements
1. **Embedding Models**: Replace TF-IDF with advanced **embedding techniques** (e.g., Word2Vec, BERT) to capture deeper semantic relationships.  
2. **Additional Features**: Incorporate other metadata like **genres**, **actors**, or **release dates** to refine the distance calculation.  
3. **Hybrid Systems**: Combine content-based approaches (like this) with collaborative filtering for even more personalized recommendations.


