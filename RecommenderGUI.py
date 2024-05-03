###     team project
###     By juncheng Zhou
###     2024/5/3
###     RecommenderGUI.py file
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
#import Recommender as rc

class RecommenderGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Media Recommender")    ##main window title
        self.main_window.geometry("1200x800")    #main window size
        notebook = ttk.Notebook(self.main_window)
        notebook.pack(side='top', fill='both', expand=True)
        
    ## bottom button
        
        self.buttonFrame = tk.Frame(self.main_window)
        self.buttonFrame.pack(side='bottom', fill='x', expand=False)

        self.loadshowsButton = tk.Button(self.buttonFrame, text="Load Shows", command=self.loadShows) #command = rc.loadShows)
        self.loadshowsButton.pack(side='left', padx=70)
        
        self.loadbooksButton = tk.Button(self.buttonFrame, text="Load Books", command=self.loadBooks) #command = rc.loadBooks)
        self.loadbooksButton.pack(side='left', padx=70)
        
        self.loadrecommendationsButton = tk.Button(self.buttonFrame, text="Load Recommendations", command=self.loadAssociations) #command = rc.loadAssocitaions)
        self.loadrecommendationsButton.pack(side='left', padx=70)
        
        self.informationButton = tk.Button(self.buttonFrame, text="Information", command=self.creditInfoBox)  #need to complete
        self.informationButton.pack(side='left', padx=70)
        
        self.quitButton = tk.Button(self.buttonFrame, text="Quit", command=self.main_window.destroy)
        self.quitButton.pack(side='left', padx=70)
            

        
    ## movies tab##
              
        movies_frame = ttk.Frame(notebook)
        notebook.add(movies_frame,text = 'Movies')
        
        label_movies = ttk.Label(movies_frame)
        label_movies.pack(pady=20, padx=20)

        label_movies.smootInfo = ('No data has been loaded yet')
        label_movies.smootTextArea = tk.Text(label_movies, wrap=tk.WORD)
        label_movies.smootTextArea.insert(tk.END, label_movies.smootInfo)
        label_movies.smootTextArea.config(state=tk.DISABLED)
        label_movies.smootTextArea.pack(side=tk.TOP)
        
        movie_listbox = tk.Listbox(movies_frame, width=50, height=10)
        movie_listbox.pack(padx=20, pady=20)
        movies = [("The Shawshank Redemption", 142),("The Godfather", 175),("The Dark Knight", 152),("Pulp Fiction", 154)]
        for movie, runtime in movies:      #fill listbox
            movie_listbox.insert(tk.END, f"{movie} - {runtime} minutes")

    ## tvshows tab##
        
        tvshows_frame = ttk.Frame(notebook)
        notebook.add(tvshows_frame,text ='TV Shows')
        
        label_tvshows = ttk.Label(tvshows_frame)
        label_tvshows.pack(pady=20, padx=20)

        label_tvshows.smootInfo = ('No data has been loaded yet')
        label_tvshows.smootTextArea = tk.Text(label_tvshows, wrap=tk.WORD)
        label_tvshows.smootTextArea.insert(tk.END, label_tvshows.smootInfo)
        label_tvshows.smootTextArea.config(state=tk.DISABLED)
        label_tvshows.smootTextArea.pack(side=tk.TOP)
        
        tvshows_listbox = tk.Listbox(tvshows_frame, width=50, height=10)
        tvshows_listbox.pack(padx=20, pady=20)
        
        
    ## books tab##
        
        books_frame = ttk.Frame(notebook)
        notebook.add(books_frame,text ='Books')
        
        label_books = ttk.Label(books_frame)
        label_books.pack(pady=20, padx=20)

        label_books.smootInfo = ('No data has been loaded yet')
        label_books.smootTextArea = tk.Text(label_books, wrap=tk.WORD)
        label_books.smootTextArea.insert(tk.END, label_books.smootInfo)
        label_books.smootTextArea.config(state=tk.DISABLED)
        label_books.smootTextArea.pack(side=tk.TOP)
        
        books_listbox = tk.Listbox(books_frame, width=50, height=10)
        books_listbox.pack(padx=20, pady=20)
        
    ## search movies/tv tab ##
    
        searchmt_frame = ttk.Frame(notebook)
        notebook.add(searchmt_frame,text ='Search Movies/TV')
        
        label_searchmt = ttk.Label(searchmt_frame)
        label_searchmt.pack(pady=20, padx=20)

        label_searchmt.smootInfo = ('No data has been loaded yet')
        label_searchmt.smootTextArea = tk.Text(label_searchmt, wrap=tk.WORD)
        label_searchmt.smootTextArea.insert(tk.END, label_searchmt.smootInfo)
        label_searchmt.smootTextArea.config(state=tk.DISABLED)
        label_searchmt.smootTextArea.pack(side=tk.TOP)
        
        books_listbox = tk.Listbox(searchmt_frame, width=50, height=10)
        books_listbox.pack(padx=20, pady=20)
        
        
    ## search books tab ##
        searchb_frame = ttk.Frame(notebook)
        notebook.add(searchb_frame,text ='Search Movies/TV')
        
        label_searchb = ttk.Label(searchb_frame)
        label_searchb.pack(pady=20, padx=20)

        label_searchb.smootInfo = ('No data has been loaded yet')
        label_searchb.smootTextArea = tk.Text(label_searchb, wrap=tk.WORD)
        label_searchb.smootTextArea.insert(tk.END, label_searchb.smootInfo)
        label_searchb.smootTextArea.config(state=tk.DISABLED)
        label_searchb.smootTextArea.pack(side=tk.TOP)
        
        books_listbox = tk.Listbox(searchb_frame, width=50, height=10)
        books_listbox.pack(padx=20, pady=20)
        
        
    ## recommendations tab ##
        recommendations_frame = ttk.Frame(notebook)
        notebook.add(recommendations_frame,text ='Recommendations')
        
        label_recommendations = ttk.Label(recommendations_frame)
        label_recommendations.pack(pady=20, padx=20)

        label_recommendations.smootInfo = ('No data has been loaded yet')
        label_recommendations.smootTextArea = tk.Text(label_recommendations, wrap=tk.WORD)
        label_recommendations.smootTextArea.insert(tk.END, label_recommendations.smootInfo)
        label_recommendations.smootTextArea.config(state=tk.DISABLED)
        label_recommendations.smootTextArea.pack(side=tk.TOP)
        
        books_listbox = tk.Listbox(recommendations_frame, width=50, height=10)
        books_listbox.pack(padx=20, pady=20)        

        
    def loadShows(self):
            messagebox.showerror(' ','load shows! function not implemented yet')
            
    def loadBooks(self):
            messagebox.showerror(' ','load books! function not implemented yet')
            
    def loadAssociations(self):
            messagebox.showerror(' ','load recommendations! function not implemented yet')
            
    def creditInfoBox(self):
        message = 'Group members: Juncheng Zhou, Yujia Liu and Tianyu Sheng\n Completed on : May 7,2024'
        messagebox.showinfo('Credit Information',message)
        
    def searchShows(self):
            messagebox.showerror(' ','searchshows! function not implemented yet')
            
    def searchBooks(self):
            messagebox.showerror(' ','searchbooks! function not implemented yet')
            
    def getRecommendations(self):
            messagebox.showerror(' ', 'getrecommendations! function not implemented yet') 


def main():
    app = RecommenderGUI()
    app.main_window.mainloop()

if __name__ == "__main__":
    main()