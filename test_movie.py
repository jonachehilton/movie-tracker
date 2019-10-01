"""(Incomplete) Tests for Movie class."""
from movie import Movie


def run_tests():
    """Test Movie class."""

    # Test empty movie (defaults)
    print("Test empty movie:")
    default_movie = Movie()
    print(default_movie)
    assert default_movie.title == ""
    assert default_movie.category == ""
    assert default_movie.year == 0
    assert not default_movie.is_watched

    # Test initial-value movie
    initial_movie = Movie("Thor: Ragnarok", 2017, "Comedy", True)
    test_movie = Movie("Blood Diamond", 2006, "Drama", False)

    print(initial_movie)

    initial_movie.unwatch()
    print("{} unwatch() - Expected False. Got {}".format(initial_movie, initial_movie.is_watched))

    initial_movie.watch()
    print("{} watch() - Expected True. Got {}\n".format(initial_movie, initial_movie.is_watched))

    print(test_movie)

    test_movie.watch()
    print("{} watch() - Expected True. Got {}".format(test_movie, test_movie.is_watched))

    test_movie.unwatch()
    print("{} unwatch() - Expected False. Got {}".format(test_movie, test_movie.is_watched))
run_tests()
