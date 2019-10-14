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


class MoviesToWatchApp(App):
    """..."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.movies = [Movie("Castaway", 1990, "Drama", True),
                       Movie("Star Wars", 2002, "Action", False),
                       Movie("King Kong", 2010, "Thriller", False)]

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
            temp_button.bind(on_release=self.press_entry)
            # Store a reference to the guitar object in the button object
            temp_button.movie = movie
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        """"""
        # Each button was given its own ".guitar" object reference, so we can get it directly
        # Update button text and label
        movie = instance.movie
        instance.text = str(movie)
        self.status_text = "{} has been watched".format(movie.title)

    def clear_widgets(self):
        """Clear all of the widgets that are children of the "entries_box" layout widget."""
        self.root.ids.entries_box.clear_widgets()


if __name__ == '__main__':
    MoviesToWatchApp().run()
