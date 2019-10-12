"""..."""

from operator import attrgetter

from movie import Movie


class MovieCollection:
    """..."""

    def __init__(self):
        self.movies = []

    def __str__(self):
        return str([str(movie) for movie in self.movies])

    def load_movies(self, file_name):
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
        self.movies.append(movie)

    def sort(self, sort_choice):
        self.movies.sort(key=attrgetter(sort_choice, "title"))

    def get_number_of_watched_movies(self):
        count_of_watched_movies = 0
        for movie in self.movies:
            if not movie.is_watched:
                count_of_watched_movies += 1
        return count_of_watched_movies

    def get_number_of_required_movies(self):
        count_of_required_movies = 0
        for movie in self.movies:
            if movie.is_watched:
                count_of_required_movies += 1
        return count_of_required_movies
