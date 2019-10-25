"""
Name: Jonache Hilton
Date: 25/10/2019
MovieCollection Class
GitHub URL: https://github.com/cp1404-students/2019-2-a2-jonachehilton
"""

from operator import attrgetter

from movie import Movie


class MovieCollection:
    """Contain a collection of Movie objects."""

    def __init__(self):
        """Initialise a MovieCollection instance with an empty list."""
        self.movies = []

    def __str__(self):
        """Return a string representation of the list of Movie objects."""
        return str([str(movie) for movie in self.movies])

    def load_movies(self, file_name):
        """Load movies from a file into the movies list attribute."""
        movie_file = open(file_name, "r")
        for i, line in enumerate(movie_file):
            movie_to_add = line.strip().split(",")
            self.movies.append(Movie(movie_to_add[0], movie_to_add[1], movie_to_add[2], movie_to_add[3]))
            if self.movies[i].is_watched == "w":
                self.movies[i].is_watched = True
            else:
                self.movies[i].is_watched = False
        movie_file.close()

    def add_movie(self, movie):
        """Add new movie to movies list attribute."""
        self.movies.append(movie)

    def sort(self, sort_choice):
        """Sort the movies list attribute by sort_choice and then by title."""
        self.movies.sort(key=attrgetter(sort_choice, "title"))

    def get_number_of_watched_movies(self):
        """Return the number of movies in the list attribute which are watched."""
        count_of_watched_movies = 0
        for movie in self.movies:
            if movie.is_watched:
                count_of_watched_movies += 1
        return count_of_watched_movies

    def get_number_of_unwatched_movies(self):
        """Return the number of movies in the list attribute which are unwatched."""
        count_of_required_movies = 0
        for movie in self.movies:
            if not movie.is_watched:
                count_of_required_movies += 1
        return count_of_required_movies

    def save_movies(self, file_name):
        """Save movies from list attribute into a file."""
        movie_file = open(file_name, "w")
        for i, movie in enumerate(self.movies):
            # Convert boolean values back to "w" and "u"
            if self.movies[i].is_watched:
                self.movies[i].is_watched = "w"
            else:
                self.movies[i].is_watched = "u"
            movie_file.write("{},{},{},{}\n".format(movie.title, movie.year, movie.category, movie.is_watched))
