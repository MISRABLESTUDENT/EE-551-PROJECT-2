import tkinter as tk
from tkinter import filedialog, messagebox
import csv


class Book:
    def __init__(self, book_id, title, authors):
        self.book_id = book_id
        self.title = title
        self.authors = authors


class Show:
    def __init__(self, show_id, title, runtime):
        self.show_id = show_id
        self.title = title
        self.runtime = runtime


class Recommender:
    def __init__(self):
        self.books = {}
        self.shows = {}
        self.associations = {}

    def loadBooks(self):
        root = tk.Tk()
        root.withdraw()
        while True:
            file_path = filedialog.askopenfilename()
            if not file_path:
                continue
            break

        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                book_id, title, authors = row
                self.books[book_id] = Book(book_id, title, authors)
        root.destroy()

    def loadShows(self):
        root = tk.Tk()
        root.withdraw()
        while True:
            file_path = filedialog.askopenfilename()
            if not file_path:
                continue
            break

        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                show_id, title, runtime = row
                self.shows[show_id] = Show(show_id, title, runtime)
        root.destroy()

    def loadAssociations(self):
        root = tk.Tk()
        root.withdraw()
        while True:
            file_path = filedialog.askopenfilename()
            if not file_path:
                continue
            break

        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                id1, id2 = row
                if id1 not in self.associations:
                    self.associations[id1] = {}
                if id2 not in self.associations[id1]:
                    self.associations[id1][id2] = 0
                self.associations[id1][id2] += 1

                if id2 not in self.associations:
                    self.associations[id2] = {}
                if id1 not in self.associations[id2]:
                    self.associations[id2][id1] = 0
                self.associations[id2][id1] += 1
        root.destroy()
