"""..."""

from movie import Movie
from moviecollection import MovieCollection


def main():
    """
    """
    MENU = "Menu:\nL - List movies\nA - Add new movie\nW - Watch a movie\nQ - Quit"

    movie_collection = MovieCollection()
    movie_collection.load_movies("movies.csv")

    print("Movies To Watch 2.0 - by Jonache Hilton\n{} movies loaded\n\n{}".format(len(movie_collection.movies), MENU))
    menu_choice = input(">>>").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            display_list(movie_collection.movies, calculate_dynamic_width(movie_collection.movies), movie_collection)

        elif menu_choice == "A":
            movie_name = ""
            is_valid_input = False
            while not is_valid_input:
                print("Title:")
                movie_name = input(">>>")
                is_valid_input = check_string_error(movie_name)

            print("Year:")
            movie_year = check_integer_error()

            print("Category:")
            movie_category = ""
            is_valid_input = False
            while not is_valid_input:
                movie_category = input(">>>")
                is_valid_input = check_string_error(movie_category)

            movie_to_add = Movie(movie_name, movie_year, movie_category, False)
            movie_collection.add_movie(movie_to_add)
            print("{} ({} from {}) added to movie list".format(movie_name, movie_category, movie_year))

        elif menu_choice == "W":
            if movie_collection.get_number_of_watched_movies() == len(movie_collection.movies):
                print("No more movies to watch!")
            else:
                print("Enter the number of a movie to mark as watched")
                watch_movie(movie_collection.movies)
        else:
            print("Invalid menu choice")

        print(MENU)
        menu_choice = input(">>>").upper()

    movie_collection.save_movies("movies.csv")


def display_list(movies, width, movie_collection):
    """
    Prints out a list of the movies and their characteristics which is sorted by year.
    Additionally prints out how many movies have been watched and how many are yet to be watched.
    """
    movie_collection.sort("year")
    for i in range(0, len(movies)):
        star_value = " "
        if not movies[i].is_watched:
            star_value = "*"
        print("{:2}. {} {:{}} -  {:>4} ({})".format(i, star_value, movies[i].title, width, movies[i].year,
                                                    movies[i].category))
    print("{} movies watched, {} movies still to watch".format(movie_collection.get_number_of_watched_movies(),
                                                               movie_collection.get_number_of_required_movies()))


def calculate_dynamic_width(movies):
    """Returns the length of the longest movie name in the movie list."""
    dynamic_width = 0
    for movie in movies:
        current_width = len(str(movie.title))
        if current_width > dynamic_width:
            dynamic_width = current_width
    return dynamic_width + 1


def check_string_error(string):
    """Determines whether a string is empty or not."""
    if string == "":
        print("Input can not be blank")
        return False
    return True


def check_integer_error():
    """
    Check if an integer is not negative.
    Prevents the program from crashing by try and excepting for a value error.
    Returns the integer when there are no errors.
    """
    is_valid_input = False
    while not is_valid_input:
        try:
            integer = int(input(">>>"))
            while integer < 0:
                print("Number must be >= 0")
                integer = int(input(">>>"))
            is_valid_input = True
            return integer
        except ValueError:
            print("Invalid input; enter a valid number")


def watch_movie(movies):
    """
    Gets an movie choice from the user.
    Prevents the program from crashing by try and excepting for an index error.
    Checks whether the choice has already been watched and prints respectively if so.
    Changes the movies value to watched if it is chosen and not watched and prints the respective message.
    """
    is_valid_input = False
    while not is_valid_input:
        try:
            chosen_movie_to_watch = int(check_integer_error())
            if movies[chosen_movie_to_watch].is_watched:
                print("You have already watched", movies[chosen_movie_to_watch].title)
                is_valid_input = True
            else:
                movies[chosen_movie_to_watch].watch()
                print("{} from {} watched".format(movies[chosen_movie_to_watch].title,
                                                  movies[chosen_movie_to_watch].year))
                is_valid_input = True
        except IndexError:
            print("Invalid movie number")


if __name__ == '__main__':
    main()
