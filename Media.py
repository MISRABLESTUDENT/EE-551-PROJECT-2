# Author: Tianyu Sheng
# Date: 5/3/2024
# Description: Media class.
class Media:
    def __init__(self, id1, title, average_rating):
        self._id = id1
        self._title = title
        self._average_rating = average_rating

    def get_id(self):
        return self._id

    def set_id(self, id1):
        self._id = id1

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_average_rating(self):
        return self._average_rating

    def set_average_rating(self, average_rating):
        self._average_rating = average_rating
