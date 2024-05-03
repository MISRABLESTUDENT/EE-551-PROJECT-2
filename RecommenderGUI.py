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
              
        self.movies_frame = ttk.Frame(notebook)
        notebook.add(self.movies_frame,text = 'Movies')
        
        label_movies = ttk.Label(self.movies_frame)
        label_movies.pack(pady=20, padx=20)

        label_movies.smootInfo = ('No data has been loaded yet')
        label_movies.smootTextArea = tk.Text(label_movies, wrap=tk.WORD)
        label_movies.smootTextArea.insert(tk.END, label_movies.smootInfo)
        label_movies.smootTextArea.config(state=tk.DISABLED)
        label_movies.smootTextArea.pack(side=tk.TOP)
        
        movie_listbox = tk.Listbox(self.movies_frame, width=50, height=10)
        movie_listbox.pack(padx=20, pady=20)
        movies = [("The Shawshank Redemption", 142),("The Godfather", 175),("The Dark Knight", 152),("Pulp Fiction", 154)]
        for movie, runtime in movies:      #fill listbox
            movie_listbox.insert(tk.END, f"{movie} - {runtime} minutes")

    ## tvshows tab##
        
        self.tvshows_frame = ttk.Frame(notebook)
        notebook.add(self.tvshows_frame,text ='TV Shows')
        
        label_tvshows = ttk.Label(self.tvshows_frame)
        label_tvshows.pack(pady=20, padx=20)

        label_tvshows.smootInfo = ('No data has been loaded yet')
        label_tvshows.smootTextArea = tk.Text(label_tvshows, wrap=tk.WORD)
        label_tvshows.smootTextArea.insert(tk.END, label_tvshows.smootInfo)
        label_tvshows.smootTextArea.config(state=tk.DISABLED)
        label_tvshows.smootTextArea.pack(side=tk.TOP)
        
        tvshows_listbox = tk.Listbox(self.tvshows_frame, width=50, height=10)
        tvshows_listbox.pack(padx=20, pady=20)
        
        
    ## books tab##
        
        self.books_frame = ttk.Frame(notebook)
        notebook.add(self.books_frame,text ='Books')
        
        label_books = ttk.Label(self.books_frame)
        label_books.pack(pady=20, padx=20)

        label_books.smootInfo = ('No data has been loaded yet')
        label_books.smootTextArea = tk.Text(label_books, wrap=tk.WORD)
        label_books.smootTextArea.insert(tk.END, label_books.smootInfo)
        label_books.smootTextArea.config(state=tk.DISABLED)
        label_books.smootTextArea.pack(side=tk.TOP)
        
        books_listbox = tk.Listbox(self.books_frame, width=50, height=10)
        books_listbox.pack(padx=20, pady=20)
        
    ## search movies/tv tab ##
    
        self.searchmt_frame = ttk.Frame(notebook)
        notebook.add(self.searchmt_frame,text ='Search Movies/TV')
        
        label_searchmt = ttk.Label(self.searchmt_frame)
        self.searchmt()   #########################

        

        
        
    ## search books tab ##
        self.searchb_frame = ttk.Frame(notebook)
        notebook.add(self.searchb_frame,text ='Search Books')
        
        label_searchb = ttk.Label(self.searchb_frame)
        self.searchb()

 
        
        
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
   

    ###search tv/movies
    def searchmt(self):
        
        #TV or Movies combobox
        self.type = ttk.Label(self.searchmt_frame,text='Type')
        self.type.grid(row=0, column=0, padx=0, pady=10, sticky='w')
        self.type_combobox = ttk.Combobox(self.searchmt_frame,values=['Movies','TV Show'])
        self.type_combobox.grid(row=0, column=0, padx=50, pady=10, sticky='w')
        # text entry#
        self.title = self.create_entry('Title:',1,self.searchmt_frame)
        self.director = self.create_entry("Director:", 2,self.searchmt_frame)
        self.actor = self.create_entry("Actor:", 3,self.searchmt_frame)
        self.genre = self.create_entry("Genre:", 4,self.searchmt_frame)
        
        #research button
        self.search_button = ttk.Button(self.searchmt_frame, text="Search", command=self.perform_search)
        self.search_button.grid(row=5, column=0, columnspan=2, pady=10, sticky='w')
        
        #result shown#
        self.result_text = tk.Text(self.searchmt_frame, state='disabled')
        self.result_text.grid(row=6, column=0, columnspan=2, padx=0, pady=10, sticky='nsew')
   

    ###search books
    def searchb(self):
        # text entry#
        self.Title = self.create_entry('Title:',1,self.searchb_frame)
        self.Author = self.create_entry("Author:", 2,self.searchb_frame)
        self.Publisher = self.create_entry("Publisher", 3,self.searchb_frame)

        
        #research button
        self.search_button = ttk.Button(self.searchb_frame, text="Search", command=self.perform_search)
        self.search_button.grid(row=5, column=0, columnspan=2, pady=10, sticky='w')
        
        #result shown#
        self.result_text = tk.Text(self.searchb_frame, state='disabled')
        self.result_text.grid(row=6, column=0, columnspan=2, padx=0, pady=10, sticky='nsew')
    
    
    
    def create_entry(self,label_text,row,frame):
        label = ttk.Label(frame,text=label_text)
        label.grid(row=row, column=0, padx=0, pady=5, sticky='w')
        entry = ttk.Entry(frame)
        entry.grid(row=row, column=0, padx=len(label_text*7), pady=5, sticky='w')
        return entry
    
    def perform_search(self):
        messagebox.showinfo('Warning','function unfinished')

def main():
    app = RecommenderGUI()
    app.main_window.mainloop()

if __name__ == "__main__":
    main()