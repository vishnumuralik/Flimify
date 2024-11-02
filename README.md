Here's a breakdown of what each of these Python files does:

### 1. **Cal Missing.py**
   - **Purpose**: This script calculates the percentage of missing values in each column of a dataset.
   - **Key Code**:
     - Loads a dataset called `rotten_tomatoes_movie_reviews.csv`.
     - Uses `df.isnull().mean() * 100` to calculate the percentage of missing values for each column.
     - Prints the missing percentages for each column to help identify where data may be incomplete.

### 2. **Collabarative Ideas.py**
   - **Purpose**: This script creates a GUI application for searching movies by director using the `tkinter` library.
   - **Key Code**:
     - Loads `rotten_tomatoes_movies.csv`, fills any missing director values with "Unknown."
     - Implements `find_movies_by_director()`, which takes a director's name and returns a list of their movies from the dataset.
     - Creates a GUI with an input field for the director’s name and displays the search results in a text box.
     - Provides an interactive way to search for movies directed by a specific person.

### 3. **Collabrative filtering.py**
   - **Purpose**: This script implements collaborative filtering to recommend movies based on similarity.
   - **Key Code**:
     - Loads a movie dataset and selects features like `audienceScore`, `tomatoMeter`, and `runtimeMinutes` for similarity calculations.
     - Standardizes these features and computes the cosine similarity between movies.
     - `recommend_similar_movies()` function takes a movie title and returns a list of movies with the highest similarity scores.
     - Example given in the code recommends similar movies to "The Dark Knight."

### 4. **Contentbasedfilteringreview.py**
   - **Purpose**: This script uses content-based filtering to recommend similar reviews based on text analysis.
   - **Key Code**:
     - Loads a dataset of movie reviews and ensures there’s a column called `reviewText`.
     - Creates a TF-IDF matrix to represent the review texts numerically.
     - Computes cosine similarity between reviews, allowing for recommendations based on text similarity.
     - The function `recommend_similar_reviews()` recommends reviews similar to a given review (default example: review at index 0). 
