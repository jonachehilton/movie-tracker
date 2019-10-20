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

# from moviecollection import MovieCollection

GREEN_COLOUR = 0.08235294117, 1, 0, 1
RED_COLOUR = 1, 0, 0.18431372549, 1


class MoviesToWatchApp(App):
    """..."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.movies = [Movie("Castaway", 1990, "Drama", True),
                       Movie("Star Wars", 2002, "Action", False),
                       Movie("King Kong", 2010, "Thriller", False),
                       Movie("Castaway", 1990, "Drama", True),
                       Movie("Castaway", 1990, "Drama", True)]

    def build(self):
        self.title = "Movies To Watch 2.0 - by Jonache Hilton"
        self.root = Builder.load_file('app.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """"""
        self.status_text = ""
        for movie in self.movies:
            # Create a button for each Movie object, specifying the text
            temp_button = Button(text=str(movie))
            temp_button.bind(on_release=self.press_movie)
            # Store a reference to the guitar object in the button object
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
        self.status_text = "{} {}".format(watched_string, movie.title)

    def clear_widgets(self):
        """Clear all of the widgets that are children of the "entries_box" layout widget."""
        self.root.ids.entries_box.clear_widgets()

    def clear_status_text(self):
        self.status_text = ""


if __name__ == '__main__':
    MoviesToWatchApp().run()
