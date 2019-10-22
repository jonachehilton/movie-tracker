"""
Name:
Date:
Brief Project Description:
GitHub URL:
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
    """..."""
    bottom_status_text = StringProperty()
    top_status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.movie_collection = MovieCollection()
        self.movie_collection.load_movies("movies.csv")
        self.movies = self.movie_collection.movies
        self.sorted_by = "Category"

    def build(self):
        self.title = "Movies To Watch 2.0 - by Jonache Hilton"
        self.root = Builder.load_file('app.kv')
        self.sort_movies(self.sorted_by)
        return self.root

    def create_widgets(self):
        """"""
        self.clear_widgets()
        self.clear_bottom_status_text()
        self.top_status_text = "To watch: {}. Watched: {}".format(self.movie_collection.
                                                                  get_number_of_unwatched_movies(), self.
                                                                  movie_collection.get_number_of_watched_movies())
        for movie in self.movies:
            # Create a button for each Movie object, specifying the text
            temp_button = Button(text=str(movie))
            temp_button.bind(on_release=self.press_movie)
            # Store a reference to the movie object in the button object
            temp_button.movie = movie
            self.root.ids.entries_box.add_widget(temp_button)
            if movie.is_watched:
                temp_button.background_color = GREEN_COLOUR
            else:
                temp_button.background_color = RED_COLOUR

    def press_movie(self, instance):
        """"""
        # Each button was given its own ".movie" object reference, so we can get it directly
        # Update button text and label
        movie = instance.movie
        if movie.is_watched:
            movie.unwatch()
            instance.background_color = RED_COLOUR
            watched_string = "You need to watch"
        else:
            movie.watch()
            instance.background_color = GREEN_COLOUR
            watched_string = "You have watched"
        instance.text = str(movie)
        self.sort_movies(self.sorted_by)
        self.bottom_status_text = "{} {}".format(watched_string, movie.title)
        self.top_status_text = "To watch: {}. Watched: {}".format(self.movie_collection.
                                                                  get_number_of_unwatched_movies(),
                                                                  self.
                                                                  movie_collection.get_number_of_watched_movies())

    def press_add_movie(self):
        is_valid_input = self.check_text_input_errors()
        if is_valid_input:
            movie_to_add = Movie(self.root.ids.added_title.text, int(self.root.ids.added_year.text),
                                 self.root.ids.added_category.text.title(), False)
            self.movie_collection.add_movie(movie_to_add)
            self.clear_fields()
            self.sort_movies(self.sorted_by)
            self.clear_bottom_status_text()

    def check_text_input_errors(self):
        try:
            if self.root.ids.added_title.text == "" or self.root.ids.added_year.text == "" or \
                    self.root.ids.added_category.text == "":
                self.bottom_status_text = "All fields must be completed"

            elif int(self.root.ids.added_year.text) < 0:
                self.bottom_status_text = "Year must be >= 0"

            elif self.root.ids.added_category.text.title() not in ["Action", "Comedy", "Documentary", "Drama",
                                                                   "Fantasy", "Thriller"]:
                self.bottom_status_text = "The category must be one of the following: Action, Comedy, Documentary," \
                                          " Drama, Fantasy, Thriller"
            else:
                return True
        except ValueError:
            self.bottom_status_text = "Please enter a valid number"

    def sort_movies(self, sorted_by):
        self.sorted_by = sorted_by
        if sorted_by == "Category":
            self.movie_collection.sort("category")
        elif sorted_by == "Title":
            self.movie_collection.sort("title")
        elif sorted_by == "Year":
            self.movie_collection.sort("year")
        else:
            self.movie_collection.sort("is_watched")
        self.create_widgets()

    def clear_fields(self):
        """
        Clear the text input fields
        :return: None
        """
        self.root.ids.added_title.text = ""
        self.root.ids.added_category.text = ""
        self.root.ids.added_year.text = ""

    def clear_widgets(self):
        """Clear all of the widgets that are children of the "entries_box" layout widget."""
        self.root.ids.entries_box.clear_widgets()

    def clear_bottom_status_text(self):
        self.bottom_status_text = ""


if __name__ == '__main__':
    MoviesToWatchApp().run()
