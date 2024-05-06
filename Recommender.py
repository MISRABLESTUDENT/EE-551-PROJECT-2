# Author: Yujia Liu, Tianyu Sheng
# Date: 5/5/2024
# Description: In this Python file and the Recommender class,
# Tianyu Sheng contributed the functions loadBooks(), loadAssociations(), searchTVMovies(),
# searchBooks(), and getRecommendations().
# The other functions, including the __init__() function, were contributed by Yujia Liu.
from Book import Book
from Show import Show
from tkinter import filedialog
from tkinter import messagebox
from collections import Counter
import os


class Recommender:
    def __init__(self):
        self.books = {}
        self.shows = {}
        self.associations = {}

    def loadBooks(self):
        while True:
            filepath = filedialog.askopenfilename(title="Please select a book file.", initialdir=os.getcwd())
            if os.path.exists(filepath,):
                break
        book_file = open(filepath, "r",encoding='utf-8')
        for line in book_file:
            line = line.strip()
            line_list = line.split(",")
            book_project = Book(line_list[0], line_list[1], line_list[2], line_list[3],
                                line_list[4], line_list[5], line_list[6], line_list[7], line_list[8],
                                line_list[9], line_list[10])
            self.books[line_list[0]] = book_project
        book_file.close()

    def loadShows(self):
        while True:
            filepath = filedialog.askopenfilename(title="Please select a show file.", initialdir=os.getcwd())
            if os.path.exists(filepath):
                break
        show_file = open(filepath, "r",encoding='utf-8')
        for line in show_file:
            line = line.strip()
            line_list = line.split(",")
            show_project = Show(line_list[0], line_list[1], line_list[2], line_list[3],
                                line_list[4], line_list[5], line_list[6], line_list[7],
                                line_list[8], line_list[9], line_list[10], line_list[11],
                                line_list[12])
            self.shows[line_list[0]] = show_project
        show_file.close()

    def loadAssociations(self):
        while True:
            filepath = filedialog.askopenfilename(title="Please select an associations file.", initialdir=os.getcwd())
            if os.path.exists(filepath):
                break
        association_file = open(filepath, "r")
        for line in association_file:
            line = line.strip()
            line_list = line.split(",")
            id1, id2 = line_list[0], line_list[1]
            if id1 not in self.associations:
                self.associations[id1] = {id2: 1}
            elif id2 in self.associations[id1]:
                self.associations[id1][id2] += 1
            else:
                self.associations[id1][id2] = 1
            if id2 not in self.associations:
                self.associations[id2] = {id1: 1}
            elif id1 in self.associations[id2]:
                self.associations[id2][id1] += 1
            else:
                self.associations[id2][id1] = 1
        association_file.close()

    def getMovieList(self):
        result = [["Title", "Runtime"]]
        for value in self.shows.values():
            if value.get_show() == "Movie":
                result.append([value.get_title(), value.get_duration()])
        column_widths = [max(len(str(item)) for item in col) for col in zip(*result)]
        formatted_rows = []
        for row in result:
            formatted_row = " ".join(str(item).ljust(column_widths[i]) for i, item in enumerate(row))
            formatted_rows.append(formatted_row)
        result_str = "\n".join(formatted_rows)
        return result_str
    #def getMovieList(self):
    #    movies = [show for show in self.shows if show.get_show() == "Movie"]
    #    max_title_length = max((len(movie.get_title()) for movie in movies), default=20)
    #    header = f"{'Title'.ljust(max_title_length)} {'Runtime'}"
    #    movie_list = [header]
    #    for movie in movies:
    #        movie_list.append(f"{movie.get_title().ljust(max_title_length)} {movie.get_duration()}")
    #    return "\n".join(movie_list)
    def getBookList(self):
        result = [["Title", "Author(s)"]]
        for value in self.books.values():
            result.append([value.get_title(), value.get_authors()])
        del result[1]
        column_widths = [max(len(str(item)) for item in col) for col in zip(*result)]
        formatted_rows = []
        for row in result:
            formatted_row = " ".join(str(item).ljust(column_widths[i]) for i, item in enumerate(row))
            formatted_rows.append(formatted_row)
        result_str = "\n".join(formatted_rows)
        return result_str
    #def getBookList(self):
    #    books = [book for book in self.books]
    #    max_title_length = max((len(book.get_title()) for book in books), default=20)
    #    max_authors_length = max((len(book.get_authors()) for book in books), default=20)
    #    header = f"{'Title'.ljust(max_title_length)} {'Author(s)'.ljust(max_authors_length)}"
    #    book_list = [header]
    #    for book in books:
    #        authors = ", ".join(book.get_authors().split(','))
    #        book_list.append(f"{book.get_title().ljust(max_title_length)} {authors.ljust(max_authors_length)}")
    #    return "\n".join(book_list)

    def getTVList(self):
        result = [["Title", "Seasons"]]
        for value in self.shows.values():
            if value.get_show() == "TV Show":
                result.append([value.get_title(), value.get_duration()])
        column_widths = [max(len(str(item)) for item in col) for col in zip(*result)]
        formatted_rows = []
        for row in result:
            formatted_row = " ".join(str(item).ljust(column_widths[i]) for i, item in enumerate(row))
            formatted_rows.append(formatted_row)
        result_str = "\n".join(formatted_rows)
        return result_str

    def getMovieStats(self):
        count_all = 0
        ratings_count = {}
        duration = 0
        director_count = {}
        actor_count = {}
        genre_count = {}
        for value in self.shows.values():
            if value.get_show() == "Movie":
                count_all += 1
                duration_list = value.get_duration().split(" ")
                duration += float(duration_list[0])
                rating = value.get_rating()
                director_list = value.get_directors().split("\\")
                actor_list = value.get_actors().split("\\")
                genre_list = value.get_genres().split("\\")
                if rating in ratings_count:
                    ratings_count[rating] += 1
                else:
                    ratings_count[rating] = 1
                for director in director_list:
                    if director in director_count:
                        director_count[director] += 1
                    else:
                        director_count[director] = 1
                for actor in actor_list:
                    if actor in actor_count:
                        actor_count[actor] += 1
                    else:
                        actor_count[actor] = 1
                for genre in genre_list:
                    if genre in genre_count:
                        genre_count[genre] += 1
                    else:
                        genre_count[genre] = 1
        average_duration = duration / count_all
        if "" in director_count:
            del director_count[""]
        if "" in actor_count:
            del actor_count[""]
        if "" in genre_count:
            del genre_count[""]
        common_director = max(director_count, key=lambda k: director_count[k])
        common_actor = max(actor_count, key=lambda k: actor_count[k])
        common_genre = max(genre_count, key=lambda k: genre_count[k])
        result = "Ratings\n"
        for key in ratings_count:
            ratings_count[key] /= count_all
            ratings_count[key] *= 100
            if key == "":
                result += f"None {ratings_count[key]:.2f}%\n"
            else:
                result += f"{key} {ratings_count[key]:.2f}%\n"
        result += (f"\nAverage Movie Duration: {average_duration:.2f} minutes\n\n"
                   f"Most Prolific Director: {common_director}\n\n"
                   f"Most Prolific Actor: {common_actor}\n\n"
                   f"Most Frequent Genre: {common_genre}")
        return result,ratings_count

    def getTVStats(self):
        count_all = 0
        ratings_count = {}
        total_seasons = 0
        actor_count = {}
        genre_count = {}

        for value in self.shows.values():
            if value.get_show() == "TV Show":
                count_all += 1
                seasons_list = value.get_duration().split(" ")
                total_seasons += float(seasons_list[0])
                rating = value.get_rating()
                actor1_list = value.get_actors().split("\\")
                genre1_list = value.get_genres().split("\\")

                if rating in ratings_count:
                    ratings_count[rating] += 1
                else:
                    ratings_count[rating] = 1
                for actor in actor1_list:
                    if actor in actor_count:
                        actor_count[actor] += 1
                    else:
                        actor_count[actor] = 1
                for genre in genre1_list:
                    if genre in genre_count:
                        genre_count[genre] += 1
                    else:
                        genre_count[genre] = 1

        average_seasons = total_seasons / count_all if count_all else 0

        if "" in actor_count:
            del actor_count[""]

        common_actor = max(actor_count, key=lambda k: actor_count[k])
        common_genre = max(genre_count, key=lambda k: genre_count[k])

        result = "Ratings\n"
        for key in ratings_count:
            ratings_count[key] /= count_all
            ratings_count[key] *= 100
            if key == "":
                result += f"None {ratings_count[key]:.2f}%\n"
            else:
                result += f"{key} {ratings_count[key]:.2f}%\n"

        result += f"\nAverage Number of Seasons: {average_seasons:.2f} seasons \n\n"
        result += f"Most Prolific Actor: {common_actor}\n\n"
        result += f"Most Frequent Genre: {common_genre}\n"

        return result,ratings_count

    def getBookStats(self):
        count_all = 0
        total_pages = 0
        author_count = {}
        publisher_count = {}

        for value in self.books.values():
            if value.get_pages() == 'num_pages':
                pass
            else:
                count_all += 1
                pages = int(value.get_pages())
                total_pages += pages
                author_list = value.get_authors().split("\\")
                publisher = value.get_publisher()
                for author in author_list:
                    if author in author_count:
                        author_count[author] += 1
                    else:
                        author_count[author] = 1

                if publisher in publisher_count:
                    publisher_count[publisher] += 1
                else:
                    publisher_count[publisher] = 1

        average_pages = total_pages / count_all if count_all else 0

        if "" in author_count:
            del author_count[""]
        if "" in publisher_count:
            del publisher_count[""]

        common_author = max(author_count, key=lambda k: author_count[k])
        common_publisher = max(publisher_count, key=lambda k: publisher_count[k])

        result = f"Average Page Count: {average_pages:.2f} pages\n\n"
        result += f"Most Prolific Author: {common_author}\n\n"
        result += f"Most Prolific Publisher: {common_publisher}\n"

        return result

    def searchTVMovies(self, show_type, title, director, actor, genre):
        if show_type not in ["Movie", "TV Show"]:
            messagebox.showerror(title="Error", message="Please select 'Movie' or 'TV Show' from Type first.")
            return "No Results"
        if title == "" and director == "" and actor == "" and genre == "":
            messagebox.showerror(title="Error", message="Please enter information for the Title, "
                                                        "Director, Actor and/or Genre first.")
            return "No Results"
        result = [["Title", "Director", "Actor", "Genre"]]
        for value in self.shows.values():
            if value.get_show() == show_type and title in value.get_title() and \
               director in value.get_directors() and actor in value.get_actors() and \
               genre in value.get_genres():
                result.append([value.get_title(), value.get_directors(), value.get_actors(), value.get_genres()])
        column_widths = [max(len(str(item)) for item in col) for col in zip(*result)]
        formatted_rows = []
        for row in result:
            formatted_row = " ".join(str(item).ljust(column_widths[i]) for i, item in enumerate(row))
            formatted_rows.append(formatted_row)
        result_str = "\n".join(formatted_rows)
        return result_str

    def searchBooks(self, title, authors, publisher):
        if title == "" and authors == "" and publisher == "":
            messagebox.showerror(title="Error", message="Please enter information for the Title,"
                                                        " Author, and/or Publisher first")
            return "No Results"
        result = [["Title", "Author", "Publisher"]]
        for value in self.books.values():
            if title in value.get_title() and authors in value.get_authors() and \
               publisher in value.get_publisher():
                result.append([value.get_title(), value.get_authors(), value.get_publisher()])
        column_widths = [max(len(str(item)) for item in col) for col in zip(*result)]
        formatted_rows = []
        for row in result:
            formatted_row = " ".join(str(item).ljust(column_widths[i]) for i, item in enumerate(row))
            formatted_rows.append(formatted_row)
        result_str = "\n".join(formatted_rows)
        return result_str

    def getRecommendations(self, type1, title):
        if type1 in ["Movie", "TV Show"]:
            show_id = None
            for id1, show in self.shows.items():
                if title in show.get_title():
                    show_id = id1
                    break
            if not show_id:
                messagebox.showwarning(title="Warning", message="There are no recommendations for this title.")
                return "No Results"
            recommend = ""
            if show_id in self.associations:
                for id2 in self.associations[show_id]:
                    if id2 in self.books:
                        book = self.books[id2]
                        id_str = (f"Title:\n{book.get_title()}\nAuthor:\n{book.get_authors()}\nAverage Rating:\n"
                                  f"{book.get_average_rating()}\nISBN:\n{book.get_isbn()}\nISBN13:\n"
                                  f"{book.get_isbn13()}\nLanguage Code:\n{book.get_language()}\nPages:\n"
                                  f"{book.get_pages()}\nRating Count:\n{book.get_ratings()}\nPublication Date:\n"
                                  f"{book.get_publication_date()}\nPublisher:\n{book.get_publisher()}\n\n"
                                  f"**************************************************\n\n")
                        recommend += id_str
            if recommend == "":
                return "No Results"
            return recommend
        if type1 == "Book":
            book_id = None
            for id3, book in self.books.items():
                if title in book.get_title():
                    book_id = id3
                    break
            if not book_id:
                messagebox.showwarning(title="Warning", message="There are no recommendations for this title.")
                return "No Results"
            recommend = ""
            if book_id in self.associations:
                for id4 in self.associations[book_id]:
                    if id4 in self.shows:
                        show = self.shows[id4]
                        id_str = (f"Type:\n{show.get_show()}\nTitle:\n{show.get_title()}\nDirector:\n"
                                  f"{show.get_directors()}\nCast:\n{show.get_actors()}\nAverage Rating:\n"
                                  f"{show.get_average_rating()}\nCountry:\n{show.get_country()}\nDate Added:\n"
                                  f"{show.get_date()}\nRelease Year:\n{show.get_year()}\nRating:\n"
                                  f"{show.get_rating()}\nDuration:\n{show.get_duration()}\nListed In:\n"
                                  f"{show.get_genres()}\nDescription:\n{show.get_description()}\n\n"
                                  f"**************************************************\n\n")
                        recommend += id_str
            if recommend == "":
                return "No Results"
            return recommend