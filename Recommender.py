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
