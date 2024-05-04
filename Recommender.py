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
        root.withdraw()  # Hides the main window
        file_path = filedialog.askopenfilename(title="books10", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if not file_path:
            messagebox.showerror("Error", "No file selected")
            return
        try:
            with open(file_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    book = Book(row['id'], row['title'], row['average_rating'], row['authors'], row['isbn'], row['isbn13'], row['language'], int(row['pages']), int(row['ratings']), row['publication_date'], row['publisher'])
                    self.books[row['id']] = book
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {str(e)}")
        finally:
            root.destroy()

    def loadShows(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(title="shows10", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if not file_path:
            messagebox.showerror("Error", "No file selected")
            return
        try:
            with open(file_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    show = Show(row['id'], row['title'], row['average_rating'], row['show_type'], row['directors'], row['actors'], row['country'], row['date_added'], row['year_released'], row['rating'], row['duration'], row['genres'].split(','), row['description'])
                    self.shows[row['id']] = show
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {str(e)}")
        finally:
            root.destroy()

    def loadAssociations(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(title="associated10", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if not file_path:
            messagebox.showerror("Error", "No file selected")
            return
        try:
            with open(file_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    id1, id2 = row
                    if id1 not in self.associations:
                        self.associations[id1] = {}
                    if id2 not in self.associations[id1]:
                        self.associations[id1][id2] = 0
                    self.associations[id1][id2] += 1

                    # Ensure bidirectional association
                    if id2 not in self.associations:
                        self.associations[id2] = {}
                    if id1 not in self.associations[id2]:
                        self.associations[id2][id1] = 0
                    self.associations[id2][id1] += 1
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {str(e)}")
        finally:
            root.destroy()
