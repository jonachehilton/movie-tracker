"""(Incomplete) Tests for MovieCollection class."""
from movie import Movie
from moviecollection import MovieCollection


def run_tests():
    """Test MovieCollection class."""

    # Test empty MovieCollection (defaults)
    print("Test empty MovieCollection:")
    movie_collection = MovieCollection()
    print(movie_collection)
    assert not movie_collection.movies  # an empty list is considered False

    # Test loading movies
    print("Test loading movies:")
    movie_collection.load_movies('movies.csv')
    print(movie_collection)
    assert movie_collection.movies  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Movie with values
    print("Test adding new movie:")
    movie_collection.add_movie(Movie("Amazing Grace", 2006, "Drama", False))
    print(movie_collection)

    # Test sorting movies
    print("Test sorting - year:")
    movie_collection.sort("year")
    print(movie_collection)

    print("Test sorting - title:")
    movie_collection.sort("title")
    print(movie_collection)

    print("Test sorting - category:")
    movie_collection.sort("category")
    print(movie_collection)

    print("Test sorting - watched:")
    movie_collection.sort("is_watched")
    print(movie_collection)

    print("Test getting number of watched movies:")
    print(movie_collection.get_number_of_watched_movies())

    print("Test getting number of unwatched movies:")
    print(movie_collection.get_number_of_required_movies())

    print("Test saving movies (check file):")
    movie_collection.save_movies("movies.csv")


run_tests()
