"""..."""


class Movie:
    def __init__(self, title="", year=0, category="", is_watched=False):
        self.title = title
        self.year = int(year)
        self.category = category
        self.is_watched = is_watched

    def __str__(self):
        return "{} ({}) from {} {}".format(self.title, self.category, self.year, self.is_watched)

    def watch(self):
        self.is_watched = True

    def unwatch(self):
        self.is_watched = False

