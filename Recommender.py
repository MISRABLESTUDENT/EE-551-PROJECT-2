from Book import Book
from Show import Show
from tkinter import filedialog
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
