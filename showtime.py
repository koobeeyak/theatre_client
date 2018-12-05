class Showtime(object):
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return "%s:%s - %s:%s" % (
            self.start_time.hour,
            self.start_time.minute,
            self.end_time.hour,
            self.end_time.minute,
        )

