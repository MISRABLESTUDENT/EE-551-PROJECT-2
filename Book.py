from Media import Media


class Book(Media):
    def __init__(self, id1, title, average_rating, authors, isbn, isbn13, language, pages,
                 ratings, publication_date, publisher):
        Media.__init__(self, id1, title, average_rating)
        self.__authors = authors
        self.__isbn = isbn
        self.__isbn13 = isbn13
        self.__language = language
        self.__pages = pages
        self.__ratings = ratings
        self.__publication_date = publication_date
        self.__publisher = publisher

    def get_authors(self):
        return self.__authors

    def set_authors(self, authors):
        self.__authors = authors

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def get_isbn13(self):
        return self.__isbn13

    def set_isbn13(self, isbn13):
        self.__isbn13 = isbn13

    def get_language(self):
        return self.__language

    def set_language(self, language):
        self.__language = language

    def get_pages(self):
        return self.__pages

    def set_pages(self, pages):
        self.__pages = pages

    def get_ratings(self):
        return self.__ratings

    def set_ratings(self, ratings):
        self.__ratings = ratings

    def get_publication_date(self):
        return self.__publication_date

    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date

    def get_publisher(self):
        return self.__publisher

    def set_publisher(self, publisher):
        self.__publisher = publisher
