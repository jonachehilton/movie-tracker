"""..."""

from movie import Movie


# from operator import attrgetter

class MovieCollection:
    """..."""

    def __init__(self):
        self.movies = []

    def __str__(self):
        return str([str(movie) for movie in self.movies])

    def load_movies(self, file_name):
        movie_file = open(file_name, "r")
        for line in movie_file:
            movie_to_add = line.strip().split(",")
            self.movies.append(Movie(movie_to_add[0], movie_to_add[1], movie_to_add[2], movie_to_add[3]))
        movie_file.close()
