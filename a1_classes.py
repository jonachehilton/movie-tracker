"""..."""

# from movie import Movie
from moviecollection import MovieCollection

# from operator import itemgetter

WATCHED = "w"
UNWATCHED = "u"


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

            append_movie_to_list(movie_category, movie_name, movie_year, movies)

        elif menu_choice == "W":
            if check_all_movies_watched(movies):
                print("No more movies to watch!")
            else:
                print("Enter the number of a movie to mark as watched")
                watch_movie(movies)
        else:
            print("Invalid menu choice")

        print(MENU)
        menu_choice = input(">>>").upper()

    movies = convert_integer_to_string(movies)
    save_movies(movies)


def display_list(movies, width, movie_collection):
    """
    Prints out a list of the movies and their characteristics which is sorted by year.
    Additionally prints out how many movies have been watched and how many are yet to be watched.
    """
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


def append_movie_to_list(movie_category, movie_name, movie_year, movies):
    movies.append([movie_name, movie_year, movie_category, UNWATCHED])
    print("{} ({} from {}) added to movie list".format(movie_name, movie_category, movie_year))


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
    valid_input = False
    while not valid_input:
        try:
            integer = int(input(">>>"))
            while integer < 0:
                print("Number must be >= 0")
                integer = int(input(">>>"))
            valid_input = True
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
    valid_input = False
    while not valid_input:
        try:
            chosen_movie_to_watch = int(check_integer_error())
            if WATCHED in movies[chosen_movie_to_watch][-1]:
                print("You have already watched", movies[chosen_movie_to_watch][0])
                valid_input = True
            else:
                movies[chosen_movie_to_watch][-1] = WATCHED
                print("{} from {} watched".format(movies[chosen_movie_to_watch][0], movies[chosen_movie_to_watch][1]))
                valid_input = True
        except IndexError:
            print("Invalid movie number")


def check_all_movies_watched(movies):
    """Checks if there are no more movies to watch and returns boolean value."""
    total_movies_watch = 0
    for movie in movies:
        if movie[3] == WATCHED:
            total_movies_watch += 1
    if total_movies_watch == len(movies):
        return True


def convert_string_to_integer(movies):
    """Converts the year string's from the list into integers and returns the new list."""
    for movie in movies:
        movie[1] = int(movie[1])
    return movies


def convert_integer_to_string(movies):
    """Converts the year integer from the list into a string for the file and returns the new list."""
    for movie in movies:
        movie[1] = str(movie[1])
    return movies


def save_movies(movies):
    """Writes the list back to the file with the relevant formatting."""
    movie_file = open("movies.csv", "w")
    for line in movies:
        movie_file.write("{}\n".format(",".join(line)))
    movie_file.close()
    print("{} movies saved to {}".format(len(movies), movie_file.name))


if __name__ == '__main__':
    main()
