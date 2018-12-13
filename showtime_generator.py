# project
from showtime import Showtime
from common.theatre_open_times import TheatreOpenTimes
from common.service_times import CLEANUP, OPENUP

# std
from datetime import timedelta


def subtract_minutes(date, minutes):
    return date - timedelta(minutes=minutes)


def add_minutes(date, minutes):
    return date + timedelta(minutes=minutes)


def theatre_is_still_serviceable(theatre_open_time, showtime_start_time):
    theatre_open_time = add_minutes(theatre_open_time, OPENUP)
    return theatre_open_time < showtime_start_time


class ShowtimeGenerator(object):
    def __init__(self, date, film):
        """

        :type date:
        :param film:
        """
        self.date = date
        self.film = film
        self.showtimes = list()

    def _generate_showtimes(self):
        today_open_hours = TheatreOpenTimes(self.date).get_hours()
        today_open_time = self.date.replace(
            hour=today_open_hours.OPEN_TIME.hour,
            minute=today_open_hours.OPEN_TIME.minute
        )
        today_close_time = self.date.replace(
            hour=today_open_hours.CLOSE_TIME.hour,
            minute=today_open_hours.CLOSE_TIME.minute
        )
        previous_showing_start_time = today_close_time
        while True:
            next_showing_start_time = subtract_minutes(previous_showing_start_time, self.film.minutes)
            if theatre_is_still_serviceable(today_open_time, next_showing_start_time):
                showtime = Showtime(next_showing_start_time, add_minutes(next_showing_start_time, self.film.minutes))
                self.showtimes.append(showtime)
                previous_showing_start_time = subtract_minutes(next_showing_start_time, CLEANUP)
            else:
                break

    def run(self):
        self._generate_showtimes()
        return self.showtimes
