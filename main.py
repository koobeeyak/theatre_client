# std
from sys import argv
from datetime import datetime

# project
from film import Film
from showtime_generator import ShowtimeGenerator


def main():
    date = datetime.now()
    header = True
    with open(argv[1], 'r') as infile:
        for line in infile:
            if header:
                header = False
                continue
            film = Film(*line.split(', '))
            showtimes = ShowtimeGenerator(date, film).run()
            print(film)
            [print(showtime) for showtime in showtimes]


if __name__ == "__main__":
    main()
