"""
Name: Jonache Hilton
Date: 25/10/2019
Brief Project Description: A Kivy program which dynamically creates movie buttons based on a list of movie objects and
allows the user to toggle the watched status, add new movies and sort the movies.
GitHub URL: https://github.com/cp1404-students/2019-2-a2-jonachehilton
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

from movie import Movie
from moviecollection import MovieCollection

GREEN_COLOUR = 0.08235294117, 1, 0, 1
RED_COLOUR = 1, 0, 0.18431372549, 1


class MoviesToWatchApp(App):
    """MoviesToWatchApp is a Kivy App for keeping track of movies from a file """
    bottom_status_text = StringProperty()
    top_status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.movie_collection = MovieCollection()
        self.movie_collection.load_movies("movies.csv")
        self.sorted_by = "category"

    def build(self):
        """
        Build the Kivy GUI.
        :return: reference to the root Kivy widget
        """
        self.title = "Movies To Watch 2.0 - by Jonache Hilton"
        self.root = Builder.load_file('app.kv')
        self.sort_movies(self.sorted_by)
        return self.root

    def create_widgets(self):
        """
        Create buttons from list of Movie objects and add them to the GUI.
        :return: None
        """
        self.clear_movie_widgets()
        self.top_status_text = "To watch: {}. Watched: {}".format(self.movie_collection.
                                                                  get_number_of_unwatched_movies(), self.
                                                                  movie_collection.get_number_of_watched_movies())
        for movie in self.movie_collection.movies:
            # Create a button for each Movie object, specifying the text
            temp_button = Button(text=str(movie))
            temp_button.bind(on_release=self.press_movie)
            # Store a reference to the movie object in the button object
            temp_button.movie = movie
            self.root.ids.movie_box.add_widget(temp_button)
            if movie.is_watched:
                temp_button.background_color = GREEN_COLOUR
            else:
                temp_button.background_color = RED_COLOUR

    def press_movie(self, instance):
        """
        Handle pressing movie buttons, changing watched status of a Movie and updating display.
        :param instance: the Kivy button instance
        :return: None
        """
        # Each button was given its own ".movie" object reference, so we can get it directly

        movie = instance.movie
        if movie.is_watched:
            movie.unwatch()
            watched_string = "You need to watch"
        else:
            movie.watch()
            watched_string = "You have watched"
        # Update button text
        instance.text = str(movie)
        self.sort_movies(self.sorted_by)
        self.bottom_status_text = "{} {}".format(watched_string, movie.title)

    def press_add_movie(self):
        """
        Handle pressing add movie button, adding Movie object to list and updating display.
        :return: None
        """
        is_valid_input = self.check_text_input_errors()
        if is_valid_input:
            movie_to_add = Movie(self.root.ids.title_input.text, int(self.root.ids.year_input.text),
                                 self.root.ids.category_input.text.title(), False)
            self.movie_collection.add_movie(movie_to_add)
            self.clear_fields()
            self.sort_movies(self.sorted_by)
            self.clear_bottom_status_text()

    def check_text_input_errors(self):
        """Check text inputs for a range of errors and returns True if no errors have occurred."""
        try:
            if self.root.ids.title_input.text == "" or self.root.ids.year_input.text == "" or \
                    self.root.ids.category_input.text == "":
                self.bottom_status_text = "All fields must be completed"
                return False

            elif int(self.root.ids.year_input.text) < 0:
                self.bottom_status_text = "Year must be >= 0"
                return False

            elif self.root.ids.category_input.text.title() not in ["Action", "Comedy", "Documentary", "Drama",
                                                                   "Fantasy", "Thriller"]:
                self.bottom_status_text = "The category must be one of the following: Action, Comedy, Documentary," \
                                          " Drama, Fantasy, Thriller"
                return False
        except ValueError:
            self.bottom_status_text = "Please enter a valid number"
        else:
            return True

    def sort_movies(self, sorted_by):
        """
        Sort the movie widgets based on the sorted_by parameter.
        :param sorted_by: the selected sorting method from the GUI spinner
        :return: None
        """
        self.sorted_by = sorted_by.lower()
        if self.sorted_by == "watched":
            self.sorted_by = "is_watched"
        self.movie_collection.sort(self.sorted_by)
        self.create_widgets()

    def clear_fields(self):
        """
        Clear the text input fields.
        :return: None
        """
        self.root.ids.title_input.text = ""
        self.root.ids.category_input.text = ""
        self.root.ids.year_input.text = ""

    def clear_movie_widgets(self):
        """
        Clear all of the widgets that are children of the "movie_box" layout widget.
        :return: None
        """
        self.root.ids.movie_box.clear_widgets()

    def clear_bottom_status_text(self):
        """
        Clear the bottom status text.
        :return: None
        """
        self.bottom_status_text = ""

    def on_stop(self):
        """
        Save movies back to file when GUI is closed.
        :return: None
        """
        self.movie_collection.save_movies("movies.csv")


if __name__ == '__main__':
    MoviesToWatchApp().run()
