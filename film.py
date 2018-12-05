class Film(object):
    def __init__(self, movie_title, release_year, mpaa_rating, run_time):
        """

        :type movie_title: basestring
        :param release_year:
        :param mpaa_rating:
        :param run_time:
        """
        self.movie_title = movie_title
        self.release_year = release_year
        self.mpaa_rating = mpaa_rating
        self.run_time = run_time

    @property
    def minutes(self):
        hours, minutes = self.run_time.split(':')
        return int(hours) * 60 + int(minutes)

    def __str__(self):
        return "%s - Rated %s, %s" % (self.movie_title, self.mpaa_rating, self.run_time)
