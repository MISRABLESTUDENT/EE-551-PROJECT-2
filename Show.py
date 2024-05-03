# Author: Tianyu Sheng
# Date: 5/3/2024
# Description: Show class.
from Media import Media


class Show(Media):
    def __init__(self, id1, title, average_rating, show, directors, actors, country, date, year,
                 rating, duration, genres, description):
        Media.__init__(self, id1, title, average_rating)
        self.__show = show
        self.__directors = directors
        self.__actors = actors
        self.__country = country
        self.__date = date
        self.__year = year
        self.__rating = rating
        self.__duration = duration
        self.__genres = genres
        self.__description = description

    def get_show(self):
        return self.__show

    def set_show(self, show):
        self.__show = show

    def get_directors(self):
        return self.__directors

    def set_directors(self, directors):
        self.__directors = directors

    def get_actors(self):
        return self.__actors

    def set_actors(self, actors):
        self.__actors = actors

    def get_country(self):
        return self.__country

    def set_country(self, country):
        self.__country = country

    def get_date(self):
        return self.__date

    def set_date(self, date):
        self.__date = date

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_rating(self):
        return self.__rating

    def set_rating(self, rating):
        self.__rating = rating

    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        self.__duration = duration

    def get_genres(self):
        return self.__genres

    def set_genres(self, genres):
        self.__genres = genres

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description
