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
            if os.path.exists(filepath):
                break
        book_file = open(filepath, "r")
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
        show_file = open(filepath, "r")
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
        movies = [show for show in self.shows.get_show() if show.get_show() == "Movie"]
        max_title_length = max((len(movie.get_title()) for movie in movies), default=20)
        header = f"{'Title'.ljust(max_title_length)} {'Runtime'}"
        movie_list = [header]
        for movie in movies:
            movie_list.append(f"{movie.get_title().ljust(max_title_length)} {movie.get_duration()}")
        return "\n".join(movie_list)

    def getBookList(self):
        books = [book for book in self.books.get_authors()]
        max_title_length = max((len(book.get_authors()) for book in books), default=20)
        header = f"{'Title'.ljust(max_title_length)} {'Author(s)'}"
        book_list = [header]
        for book in books:
            # Ensure all author names are included, assuming multiple authors can be split by commas
            authors = ", ".join(book.get_authors().split(','))
            book_list.append(f"{book.get_authors().ljust(max_title_length)} {authors}")
        return "\n".join(book_list)

    def getTVList(self):
        tv_shows = [show for show in self.shows.get_show() if show.get_show() == "TV Show"]
        # Determine maximum lengths for pretty printing
        max_title_length = max((len(tv.get_title()) for tv in tv_shows), default=20)
        max_seasons_length = max((len(tv.get_duration().split()[0]) for tv in tv_shows if 'Season' in tv.get_duration()), default=7)

        # Format the header
        header = f"{'Title'.ljust(max_title_length)} {'Seasons'.ljust(max_seasons_length)}"
        tv_list = [header]

        # Format each TV show entry
        for tv in tv_shows:
            seasons = tv.get_duration().split()[0]  # Assuming the duration is like "2 Seasons"
            tv_list.append(f"{tv.get_title().ljust(max_title_length)} {seasons.ljust(max_seasons_length)}")

        return "\n".join(tv_list)


    def getMovieStats(self):
        movies = [show for show in self.shows.get_show() if show.get_show() == "Movie"]
        durations = []
        for movie in movies:
            duration_parts = movie.get_duration().split()
            if duration_parts and duration_parts[0].isdigit():
                durations.append(int(duration_parts[0]))
        average_duration = sum(durations) / len(durations) if durations else 0
        rating_counts = Counter(movie.get_rating() for movie in movies)
        total_ratings = sum(rating_counts.get_rating())
        rating_distribution = {rating: f"{(count / total_ratings * 100):.2f}%" for rating, count in
                               rating_counts.items()}
        
        directors = Counter(director for movie in movies for director in movie.get_directors().split(', '))
        actors = Counter(actor for movie in movies for actor in movie.get_actors().split(', '))
        genres = Counter(genre for movie in movies for genre in movie.get_genres().split(', '))

        most_common_director = directors.most_common(1)[0][0] if directors else None
        most_common_actor = actors.most_common(1)[0][0] if actors else None
        most_common_genre = genres.most_common(1)[0][0] if genres else None

        stats = {
            "Ratings Distribution": rating_distribution,
            "Average Movie Duration": f"{average_duration:.2f} minutes",
            "Most Prolific Director": most_common_director,
            "Most Featured Actor": most_common_actor,
            "Most Frequent Genre": most_common_genre
        }
        return stats

    def getTVStats(self):
        tv_shows = [show for show in self.shows.get_show() if show.get_show() == "TV Show"]

        # Compute the average number of seasons
        season_counts = []
        for tv in tv_shows:
            season_number = tv.get_duration().split()[0]
            if season_number.isdigit():  # ensure the season number is a digit
                season_counts.append(int(season_number))

        average_seasons = sum(season_counts) / len(season_counts) if season_counts else 0

        # Count ratings
        rating_counts = Counter(tv.get_rating() for tv in tv_shows)
        total_ratings = sum(rating_counts.get_rating())
        rating_distribution = {rating: f"{(count / total_ratings * 100):.2f}%" for rating, count in
                               rating_counts.items()}

        # Most frequent actor and genre
        actors = Counter(actor.strip() for tv in tv_shows for actor in tv.get_actors().split(','))
        genres = Counter(genre.strip() for tv in tv_shows for genre in tv.get_genres().split(','))

        most_common_actor = actors.most_common(1)[0][0] if actors else 'None'
        most_common_genre = genres.most_common(1)[0][0] if genres else 'None'

        stats = {
            "Ratings Distribution": rating_distribution,
            "Average Number of Seasons": f"{average_seasons:.2f} seasons",
            "Most Prolific Actor": most_common_actor,
            "Most Frequent Genre": most_common_genre
        }
        return stats


    def getBookStats(self):
        books = [book for book in self.books.get_authors()]

        # Compute average page count
        total_pages = sum(int(book.get_pages()) for book in books)
        average_page_count = round(total_pages / len(books), 2) if books else 0

        # Count author book counts
        authors = Counter(author.strip() for book in books for author in book.get_authors().split(','))
        most_prolific_author = authors.most_common(1)[0][0] if authors else 'None'

        # Count publishers
        publishers = Counter(book.get_publisher() for book in books)
        most_books_publisher = publishers.most_common(1)[0][0] if publishers else 'None'

        stats = {
            "Average Page Count": f"{average_page_count} pages",
            "Most Prolific Author": most_prolific_author,
            "Most Prolific Publisher": most_books_publisher
        }
        return stats
    
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
            if value.get_show() == show_type and (title in value.get_title() or
                                                  director in value.get_directors() or
                                                  actor in value.get_actors() or
                                                  genre in value.get_genres()):
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
                return "No results"
            recommend = ""
            for id2 in self.associations[show_id]:
                book = self.books[id2]
                id_str = (f"Title:\n{book.get_title()}\nAuthor:\n{book.get_authors()}\nAverage Rating:\n"
                          f"{book.get_average_rating()}\nISBN:\n{book.get_isbn()}\nISBN13:\n"
                          f"{book.get_isbn13()}\nLanguage Code:\n{book.get_language()}\nPages:\n"
                          f"{book.get_pages()}\nRating Count:\n{book.get_ratings()}\nPublication Date:\n"
                          f"{book.get_publication_date()}\nPublisher:\n{book.get_publisher()}\n\n"
                          f"**************************************************\n\n")
                recommend += id_str
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
            for id4 in self.associations[book_id]:
                show = self.shows[id4]
                id_str = (f"Type:\n{show.get_show()}\nTitle:\n{show.get_title()}\nDirector:\n"
                          f"{show.get_directors()}\nCast:\n{show.get_actors()}\nAverage Rating:\n"
                          f"{show.get_average_rating()}\nCountry:\n{show.get_country()}\nDate Added:\n"
                          f"{show.get_date()}\nRelease Year:\n{show.get_year()}\nRating:\n"
                          f"{show.get_rating()}\nDuration:\n{show.get_duration()}\nListed In:\n"
                          f"{show.get_genres()}\nDescription:\n{show.get_description()}\n\n"
                          f"**************************************************\n\n")
                recommend += id_str
            return recommend
