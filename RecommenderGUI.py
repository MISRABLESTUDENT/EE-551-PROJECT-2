###     team project
###     By juncheng Zhou
###     2024/5/3
###     RecommenderGUI.py file
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Recommender import Recommender as rc
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class RecommenderGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Media Recommender")    ##main window title
        self.main_window.geometry("1200x800")    #main window size
        notebook = ttk.Notebook(self.main_window)
        notebook.pack(side='top', fill='both', expand=True)
        self.recommender = rc()
        
    ## bottom button
        
        self.buttonFrame = tk.Frame(self.main_window)
        self.buttonFrame.pack(side='bottom', fill='x', expand=False)

        self.loadshowsButton = tk.Button(self.buttonFrame, text="Load Shows", command=self.loadShows)   ##Load Shows
        self.loadshowsButton.pack(side='left', padx=60)
        

        self.loadbooksButton = tk.Button(self.buttonFrame, text="Load Books", command=self.loadBooks)  ## Load Books
        self.loadbooksButton.pack(side='left', padx=60)
        
        self.loadrecommendationsButton = tk.Button(self.buttonFrame, text="Load Recommendations", command=self.loadAssociations)
        self.loadrecommendationsButton.pack(side='left', padx=60)    # Load Recommendations
        
        self.informationButton = tk.Button(self.buttonFrame, text="Information", command=self.creditInfoBox) ## Information
        self.informationButton.pack(side='left', padx=60)

        self.ratingsButton = tk.Button(self.buttonFrame, text="Ratings",command=self.piecharts)  ## pie charts
        self.ratingsButton.pack(side='left', padx=60)
        
        self.quitButton = tk.Button(self.buttonFrame, text="Quit", command=self.main_window.destroy)
        self.quitButton.pack(side='left', padx=60)   ## Quit
            

        
    ## movies tab##
              
        self.movies_frame = ttk.Frame(notebook)
        notebook.add(self.movies_frame,text = 'Movies')
        self.moviewelcome = tk.Label(self.movies_frame, text='Please load show file')
        self.moviewelcome.grid(row=0, column=0, padx=10, pady=10)



    ## tvshows tab##

        self.tvshows_frame = ttk.Frame(notebook)
        notebook.add(self.tvshows_frame,text ='TV Shows')
        self.tvwelcome = tk.Label(self.tvshows_frame, text='Please load show file')
        self.tvwelcome.grid(row=0, column=0, padx=10, pady=10)

        
        
    ## books tab##
        
        self.books_frame = ttk.Frame(notebook)
        notebook.add(self.books_frame,text ='Books')
        self.bookwelcome= tk.Label(self.books_frame, text='Please load book file')
        self.bookwelcome.grid(row=0, column=0, padx=10, pady=10)


        
    ## search movies/tv tab ##
    
        self.searchmt_frame = ttk.Frame(notebook)
        notebook.add(self.searchmt_frame,text ='Search Movies/TV')
        
        label_searchmt = ttk.Label(self.searchmt_frame)
        self.searchmt()   #########################

        

        
        
    ## search books tab ##
        self.searchb_frame = ttk.Frame(notebook)
        notebook.add(self.searchb_frame,text ='Search Books')
        
        self.label_searchb = ttk.Label(self.searchb_frame)
        self.searchb_result = 'You can search something here'
        self.searchb()


        
        
    ## recommendations tab ##
        self.recommendations_frame = ttk.Frame(notebook)
        notebook.add(self.recommendations_frame,text ='Recommendations')
        
        label_recommendations = ttk.Label(self.recommendations_frame)
        self.getrc()

        

    def loadShows(self):
        #try:
        self.recommender.loadShows()
        #print("Loaded shows:", self.recommender.shows)
        self.update_movie_list()
        self.update_tv_list()

    def update_movie_list(self):
        self.moviewelcome.destroy()

        self.smootTextArea = tk.Text(self.movies_frame,height=20,width=200,state='normal')
        self.smootTextArea.grid(row=6, column=0, columnspan=2, padx=0, pady=10, sticky='nsew')
        self.smootTextArea.config(state=tk.NORMAL)
        self.smootTextArea.delete('1.0', tk.END)
        self.smootTextArea.insert(tk.END, self.recommender.getMovieList())
        self.smootTextArea.config(state=tk.DISABLED)
       ###ratings

        self.moviesrating = tk.Text(self.movies_frame, height=30, width=200, state='normal')
        self.moviesrating.grid(row=7, column=0, columnspan=2, padx=0, pady=10, sticky='nsew')
        self.moviesrating.config(state=tk.NORMAL)
        self.moviesrating.delete('1.0', tk.END)
        self.moviesrating.insert(tk.END,self.recommender.getMovieStats()[0])
        self.moviesrating.config(state=tk.DISABLED)
    def update_tv_list(self):

        self.tvwelcome.destroy()
        #print("TV shows list:", tv_list)
        self.TVTextArea = tk.Text(self.tvshows_frame,height=20,width=200,state='normal')
        self.TVTextArea.grid(row=6, column=0, columnspan=2, padx=0, pady=10, sticky='nsew')
        self.TVTextArea.delete('1.0', tk.END)
        #print(self.recommender.shows)
        self.TVTextArea.insert(tk.END, self.recommender.getTVList())
        self.TVTextArea.config(state=tk.DISABLED)
        ###ratings
        self.TVrating = tk.Text(self.tvshows_frame, height=30, width=200, state='normal')
        self.TVrating.grid(row=7, column=0, columnspan=2, padx=0, pady=10, sticky='nsew')
        self.TVrating.config(state=tk.NORMAL)
        self.TVrating.delete('1.0', tk.END)
        self.TVrating.insert(tk.END, self.recommender.getTVStats()[0])
        self.TVrating.config(state=tk.DISABLED)
    def update_books_list(self):
        ###########books list
        self.bookwelcome.destroy()
        self.Booklist = tk.Text(self.books_frame, height=20, width=200, state='normal')
        self.Booklist.grid(row=6, column=0, columnspan=2, padx=0, pady=10, sticky='nsew')
        self.Booklist.config(state=tk.NORMAL)
        self.Booklist.delete('1.0', tk.END)
        self.Booklist.insert(tk.END, self.recommender.getBookList())
        self.Booklist.config(state=tk.DISABLED)
        ####Average page ####
        self.Booksrating = tk.Text(self.books_frame, height=30, width=200, state='normal')
        self.Booksrating.grid(row=7, column=0, columnspan=2, padx=0, pady=10, sticky='nsew')
        self.Booksrating.config(state=tk.NORMAL)  #
        self.Booksrating.delete('1.0', tk.END)
        self.Booksrating.insert(tk.END,self.recommender.getBookStats())
        self.Booksrating.config(state=tk.DISABLED)

    def loadBooks(self):
        self.recommender.loadBooks() 
        self.update_books_list()

            
    def loadAssociations(self):
        self.recommender.loadAssociations() 

    def creditInfoBox(self):
        message = 'Group members: Juncheng Zhou, Yujia Liu and Tianyu Sheng\n Completed on : May 5,2024'
        messagebox.showinfo('Credit Information',message)

    def piecharts(self):
        ratings_tab = ttk.Frame(ttk.Notebook(self.main_window))
        movies_ratings = self.recommender.getMovieStats()[1]
        tv_ratings = self.recommender.getTVStats()[1]


        #first piechart
        fig1, ax1 = plt.subplots()
        ax1.pie(movies_ratings.values(), labels=movies_ratings.keys(), autopct='%1.2f%%', startangle=90)
        ax1.axis('equal')

        canvas = FigureCanvasTkAgg(fig1,master=ratings_tab)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        ## second pie chart
        fig2, ax2 = plt.subplots()
        ax2.pie(tv_ratings.values(), labels=tv_ratings.keys(), autopct='%1.2f%%', startangle=90)
        ax2.axis('equal')

        canvas = FigureCanvasTkAgg(fig2, master=ratings_tab)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)



    ###search tv/movies
    def searchmt(self):
        #TV or Movies combobox
        self.type = ttk.Label(self.searchmt_frame,text='Type')
        self.type.grid(row=0, column=0, padx=0, pady=10, sticky='w')
        self.type_combobox = ttk.Combobox(self.searchmt_frame,values=['Movie','TV Show'])
        self.type_combobox.grid(row=0, column=0, padx=50, pady=10, sticky='w')
        self.type_combobox.set('Movie')

        # text entry#
        self.title = self.create_entry('Title:',1,self.searchmt_frame)
        self.director = self.create_entry("Director:", 2,self.searchmt_frame)
        self.actor = self.create_entry("Actor:", 3,self.searchmt_frame)
        self.genre = self.create_entry("Genre:", 4,self.searchmt_frame)


        #research button
        self.search_button = ttk.Button(self.searchmt_frame, text="Search", command=self.perform_search_mt)
        self.search_button.grid(row=5, column=0, columnspan=2, pady=10, sticky='w')

   

    ###search books
    def searchb(self):
        # text entry#
        self.Title = self.create_entry('Title:',1,self.searchb_frame)
        self.Author = self.create_entry("Author:", 2,self.searchb_frame)
        self.Publisher = self.create_entry("Publisher", 3,self.searchb_frame)

        title= self.Title.get()
        publisher= self.Publisher.get()
        author= self.Author.get()



        #research button
        self.search_button = ttk.Button(self.searchb_frame, text="Search", command=self.perform_search_b)
        self.search_button.grid(row=5, column=0, columnspan=2, pady=10, sticky='w')
        

    
    
    
    def create_entry(self,label_text,row,frame):
        label = ttk.Label(frame,text=label_text)
        label.grid(row=row, column=0, padx=0, pady=5, sticky='w')
        entry = ttk.Entry(frame)
        entry.grid(row=row, column=0, padx=len(label_text*7), pady=5, sticky='w')
        return entry
    
    def perform_search_b(self):
        title = self.Title.get()
        author = self.Author.get()
        publisher = self.Publisher.get()
        self.searchb_result = self.recommender.searchBooks(title, author, publisher)
        self.result_text = tk.Text(self.searchb_frame, height=30,width=200,state='normal')
        self.result_text.grid(row=6, column=0, columnspan=2, padx=0, pady=10, sticky='nsew')

        self.result_text.delete('1.0', tk.END)
        self.result_text.insert(tk.END, self.searchb_result)
        self.result_text.config(state='disabled')
    def perform_search_mt(self):
        show_type = self.type_combobox.get()
        title = self.title.get()
        director = self.director.get()
        actor = self.actor.get()
        genre = self.genre.get()
        #print('good luck', show_type, title, director, actor, genre)
        self.searchmt_result=self.recommender.searchTVMovies(show_type, title, director, actor, genre)
        self.result_text_mt = tk.Text(self.searchmt_frame, height=30, width=200, state='normal')
        self.result_text_mt.grid(row=6, column=0, columnspan=2, padx=0, pady=10, sticky='nsew')
        self.result_text.delete('1.0', tk.END)
        #print(self.searchmt_result)
        self.result_text_mt.insert(tk.END, self.searchmt_result)
        self.result_text_mt.config(state='disabled')
    #get recommendations##
    def getrc(self):
        ## Movie, TV Show or Book
        self.type = ttk.Label(self.recommendations_frame,text='Type')
        self.type.grid(row=0, column=0, padx=0, pady=10, sticky='w')
        self.type_combobox3 = ttk.Combobox(self.recommendations_frame,values=['Movie','TV Show','Book'])
        self.type_combobox3.grid(row=0, column=0, padx=50, pady=10, sticky='w')
    ## search title
        # text entry#
        self.Title3 = self.create_entry('Title:',1,self.recommendations_frame)
        
        #research button
        self.search_button = ttk.Button(self.recommendations_frame, text="Get Recommendation", command=self.getRecommendations) #####
        self.search_button.grid(row=5, column=0, columnspan=2, pady=10, sticky='w')
        
        #result shown#
        self.result_text = tk.Text(self.recommendations_frame, state='disabled')
        self.result_text.grid(row=6, column=0, columnspan=2, padx=0, pady=10, sticky='nsew')

    def getRecommendations(self):
            #messagebox.showinfo(' ', 'get recommendations! function not implemented yet')
            title = self.Title3.get()
            type1 = self.type_combobox3.get()
            self.getrc_result = self.recommender.getRecommendations(type1, title)
            self.result_text_mt = tk.Text(self.recommendations_frame, height=30, width=200, state='normal')
            self.result_text_mt.grid(row=6, column=0, columnspan=2, padx=0, pady=10, sticky='nsew')
            self.result_text.delete('1.0', tk.END)
            #print(self.getrc_result)
            self.result_text_mt.insert(tk.END, self.getrc_result)
            self.result_text_mt.config(state='disabled')


def main():
    app = RecommenderGUI()
    app.main_window.mainloop()

if __name__ == "__main__":
    main()