"""..."""


class Movie:
    def __init__(self, title="", year=0, category="", is_watched=False):
        self.title = title
        self.year = int(year)
        self.category = category
        self.is_watched = is_watched

    def __str__(self):
        if self.is_watched:
            watched_string = "watched"
        else:
            watched_string = ""
        return "{} ({} from {}) {}".format(self.title, self.category, self.year, watched_string)

    def watch(self):
        self.is_watched = True

    def unwatch(self):
        self.is_watched = False
