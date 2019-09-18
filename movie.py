"""..."""


# TODO: Create your Movie class in this file


class Movie:
    def __init__(self, title="", year=0, category="", watched=False):
        self.title = title
        self.year = year
        self.category = category
        self.watched = watched

    def __str__(self):
        return "{} ({}) from {}".format(self.title, self.category, self.year)

    def is_watched(self):
        if self.watched:
            return "this movie is watched"




