"""
Name: Jonache Hilton
Date: 25/10/2019
Movie Class
GitHub URL: https://github.com/cp1404-students/2019-2-a2-jonachehilton
"""


class Movie:
    """"Represent a Movie object."""
    def __init__(self, title="", year=0, category="", is_watched=False):
        self.title = title
        self.year = int(year)
        self.category = category
        self.is_watched = is_watched

    def __str__(self):
        """Return a string representation of a Movie object."""
        if self.is_watched:
            watched_string = "watched"
        else:
            watched_string = ""
        return "{} ({} from {}) {}".format(self.title, self.category, self.year, watched_string)

    def watch(self):
        """Change the watched status to True for a Movie object."""
        self.is_watched = True

    def unwatch(self):
        """Change the watched status to False for a Movie object."""
        self.is_watched = False
