import unittest
from datetime import datetime

# project
from showtime_generator import ShowtimeGenerator
from film import Film
from film import FilmValidationException


class ShowtimeGeneratorTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_showtime_generator__weekday__one_hour_forty_six_minutes(self):
        date = datetime(month=12, day=12, year=2018)
        film = Film(
            movie_title="Something About Mary",
            release_year="1992",
            mpaa_rating="R",
            run_time="1:46"
        )
        showtimes = ShowtimeGenerator(date, film).run()
        self.assertEqual(len(showtimes), 6)

    def test_showtime_generator__weekday__one_hour_forty_eight_minutes(self):
        date = datetime(month=12, day=12, year=2018)
        film = Film(
            movie_title="Something About Mary",
            release_year="1992",
            mpaa_rating="R",
            run_time="1:48"
        )
        showtimes = ShowtimeGenerator(date, film).run()
        self.assertEqual(len(showtimes), 6)

    def test_showtime_generator__weekend__one_hour_forty_eight_minutes(self):
        date = datetime(month=12, day=14, year=2018)
        film = Film(
            movie_title="Something About Mary",
            release_year="1992",
            mpaa_rating="R",
            run_time="1:48"
        )
        showtimes = ShowtimeGenerator(date, film).run()
        self.assertEqual(len(showtimes), 5)

    def test_showtime_generator__zero_hour_zero_minute(self):
        date = datetime(month=12, day=14, year=2018)
        with self.assertRaises(FilmValidationException):
            Film(
                movie_title="Something About Mary",
                release_year="1992",
                mpaa_rating="R",
                run_time="0:00"
            )

    def test_showtime_generator__twenty_hour(self):
        date = datetime(month=12, day=14, year=2018)
        film = Film(
            movie_title="Something About Mary",
            release_year="1992",
            mpaa_rating="R",
            run_time="20:00"
        )
        showtimes = ShowtimeGenerator(date, film).run()
        self.assertEqual(len(showtimes), 0)


unittest.main()
