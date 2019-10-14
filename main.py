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


class MoviesToWatchApp(App):
    """..."""
    status_text = StringProperty

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.movies = [Movie("Castaway", 1990, "Drama", True),
                       Movie("Star Wars", 2002, "Action", False),
                       Movie("King Kong", 2010, "Thriller", False)]

    def build(self):
        self.title = "Movies To Watch 2.0 - by Jonache Hilton"
        self.root = Builder.load_file('app.kv')
        return self.root


if __name__ == '__main__':
    MoviesToWatchApp().run()
