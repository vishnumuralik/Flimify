import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Load the movie dataset
movie_data = pd.read_csv('/Users/vishn/Downloads/rotten_tomatoes_movies.csv', nrows=50000)

# Fill missing values in the 'director' column with empty strings to avoid issues
movie_data['director'] = movie_data['director'].fillna('Unknown')


def find_movies_by_director(director_name, movie_data):
    """
    Function to find movies that are directed by a specific director.

    Args:
    - director_name: Name of the director to search for.
    - movie_data: The movie dataset as a pandas DataFrame.

    Returns:
    - List of movies directed by the given director or a message if no movies are found.
    """
    # Filter the dataset by the provided director name (case-insensitive)
    director_movies = movie_data[movie_data['director'].str.contains(director_name, case=False, na=False)]

    if director_movies.empty:
        return f"No movies found for director '{director_name}'."

    # Return the list of movie titles directed by the input director
    return director_movies['title'].tolist()


def search_movies():
    """Triggered when the user clicks the 'Search' button."""
    director_name = director_entry.get()  # Get the input from the entry widget
    if not director_name:
        messagebox.showwarning("Input Error", "Please enter a director's name.")
        return

    movies = find_movies_by_director(director_name, movie_data)

    # Clear the text area before displaying new results
    result_text.delete(1.0, tk.END)

    if isinstance(movies, list):
        result_text.insert(tk.END, f"Movies directed by '{director_name}':\n\n")
        result_text.insert(tk.END, ', '.join(movies))
    else:
        result_text.insert(tk.END, movies)


# Create the main application window
root = tk.Tk()
root.title("Movie Finder by Director")
root.geometry("500x400")  # Set window size

# Create a label for the director input
director_label = tk.Label(root, text="Enter Director's Name:", font=("Helvetica", 14))
director_label.pack(pady=10)

# Create an entry widget for user input
director_entry = tk.Entry(root, width=40, font=("Helvetica", 14))
director_entry.pack(pady=10)

# Create a search button
search_button = tk.Button(root, text="Search", command=search_movies, font=("Helvetica", 12), bg="lightblue")
search_button.pack(pady=10)

# Create a text widget to display the results
result_text = tk.Text(root, height=10, width=50, font=("Helvetica", 12))
result_text.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
