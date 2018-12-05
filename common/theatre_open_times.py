# std
from datetime import datetime, time
import calendar


WEEKDAYS = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
]

WEEKENDS = [
    'Friday',
    'Saturday',
    'Sunday',
]

class WeekdayHours(object):
    OPEN_TIME = time(hour=8)
    CLOSE_TIME = time(hour=23)


class WeekendHours(object):
    OPEN_TIME = time(hour=10, minute=30)
    CLOSE_TIME = time(hour=23, minute=30)


class TheatreOpenTimes(object):
    def __init__(self, date):
        """

        :type date: datetime
        """
        self.date = date

    def get_hours(self):
        day_of_week = calendar.day_name[self.date.weekday()]
        if day_of_week in WEEKDAYS:
            return WeekdayHours
        return WeekendHours
