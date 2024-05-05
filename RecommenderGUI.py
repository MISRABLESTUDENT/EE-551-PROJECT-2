###     team project
###     By juncheng Zhou
###     2024/5/3
###     RecommenderGUI.py file
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Recommender import Recommender as rc

#import Recommender as rc

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

        self.loadshowsButton = tk.Button(self.buttonFrame, text="Load Shows", command=self.loadShows) #command = rc.loadShows)
        self.loadshowsButton.pack(side='left', padx=70)
        
        #self.loadbooksButton = tk.Button(self.buttonFrame, text="Load Books", command=rc.loadBooks) #command = rc.loadBooks)
        self.loadbooksButton = tk.Button(self.buttonFrame, text="Load Books", command=self.loadBooks)
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
        
        self.label_movies = ttk.Label(self.movies_frame)
        self.label_movies.pack(pady=20, padx=20)

        self.label_movies.smootTextArea = tk.Text(self.movies_frame, wrap=tk.WORD)
        self.label_movies.smootTextArea.pack(side=tk.TOP)
        #label_movies.smootInfo = ('need getmovielist and getmoviestats')
        #label_movies.smootTextArea = tk.Text(label_movies, wrap=tk.WORD)
        #label_movies.smootTextArea.insert(tk.END, label_movies.smootInfo)
        #label_movies.smootTextArea.config(state=tk.DISABLED)
        #label_movies.smootTextArea.pack(side=tk.TOP)
        
        #movie_listbox = tk.Listbox(self.movies_frame, width=50, height=10)
        #movie_listbox.pack(padx=20, pady=20)


    ## tvshows tab##
        
        self.tvshows_frame = ttk.Frame(notebook)
        notebook.add(self.tvshows_frame,text ='TV Shows')
        
        self.label_tvshows = ttk.Label(self.tvshows_frame)
        self.label_tvshows.pack(pady=20, padx=20)

        self.label_tvshows.smootInfo = ('need gettvlist and gettvstats')
        self.label_tvshows.smootTextArea = tk.Text(self.label_tvshows, wrap=tk.WORD)
        self.label_tvshows.smootTextArea.insert(tk.END, self.label_tvshows.smootInfo)
        self.label_tvshows.smootTextArea.config(state=tk.DISABLED)
        self.label_tvshows.smootTextArea.pack(side=tk.TOP)
        
        tvshows_listbox = tk.Listbox(self.tvshows_frame, width=50, height=10)
        tvshows_listbox.pack(padx=20, pady=20)
        
        
    ## books tab##
        
        self.books_frame = ttk.Frame(notebook)
        notebook.add(self.books_frame,text ='Books')
        
        self.label_books = ttk.Label(self.books_frame)
        self.label_books.pack(pady=20, padx=20)

        #label_books.smootInfo = ('need getbooklist and getbookstats')
        #label_books.smootTextArea = tk.Text(label_books, wrap=tk.WORD)
        #label_books.smootTextArea.insert(tk.END, label_books.smootInfo)
        #label_books.smootTextArea.config(state=tk.DISABLED)
        #label_books.smootTextArea.pack(side=tk.TOP)
        
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
        self.recommendations_frame = ttk.Frame(notebook)
        notebook.add(self.recommendations_frame,text ='Recommendations')
        
        label_recommendations = ttk.Label(self.recommendations_frame)
        self.getrc()

        
    #def loadShows(self):
     #   self.recommender.loadShows() 
    def loadShows(self):
        #try:
        self.recommender.loadShows()  # 假设这个方法加载电影数据
        #print("Loaded shows:", self.recommender.shows)
        self.update_movie_list()  # 更新电影列表显示
        self.update_tv_list()
        #except Exception as e:
         #   messagebox.showerror("Error", f"Failed to load shows: {str(e)}")

            #messagebox.showerror(' ','load shows! function not implemented yet')
    def update_movie_list(self):
        movie_list = self.recommender.getMovieList()  # 获取电影列表字符串
        print("Movie list:", movie_list)  # 查看返回的电影列表内容
        self.label_movies.smootTextArea.config(state=tk.NORMAL)  # 允许修改内容
        self.label_movies.smootTextArea.delete('1.0', tk.END)  # 清空现有内容
        self.label_movies.smootTextArea.insert(tk.END, movie_list)  # 插入新的电影列表
        self.label_movies.smootTextArea.config(state=tk.DISABLED)  # 禁止修改内容
    def update_tv_list(self):
        tv_list = self.recommender.getTVList()  # 获取电影列表字符串
        print("TV shows list:", tv_list)  # 查看返回的电影列表内容
        self.label_tvshows.smootTextArea.config(state=tk.NORMAL)  # 允许修改内容
        self.label_tvshows.smootTextArea.delete('1.0', tk.END)  # 清空现有内容
        self.label_tvshows.smootTextArea.insert(tk.END, tv_list)  # 插入新的电影列表
        self.label_tvshows.smootTextArea.config(state=tk.DISABLED)  # 禁止修改内容
        
    def update_books_list(self):
        book_list = self.recommender.getBookList()  # 获取电影列表字符串
        print("Book list:", book_list)  # 查看返回的电影列表内容
        self.label_books.smootTextArea.config(state=tk.NORMAL)  # 允许修改内容
        self.label_books.smootTextArea.delete('1.0', tk.END)  # 清空现有内容
        self.label_books.smootTextArea.insert(tk.END, book_list)  # 插入新的电影列表
        self.label_books.smootTextArea.config(state=tk.DISABLED)  # 禁止修改内容
    def loadBooks(self):
        self.recommender.loadBooks() 
        self.update_books_list()
    #def loadBooks(self):
     #       messagebox.showerror(' ','load books! function not implemented yet')
            
    def loadAssociations(self):
        self.recommender.loadAssociations() 
            #messagebox.showerror(' ','load recommendations! function not implemented yet')
            
    def creditInfoBox(self):
        message = 'Group members: Juncheng Zhou, Yujia Liu and Tianyu Sheng\n Completed on : May 7,2024'
        messagebox.showinfo('Credit Information',message)
        
    def searchShows(self):
            messagebox.showerror(' ','searchshows! function not implemented yet')
            
    def searchBooks(self):
            messagebox.showerror(' ','searchbooks! function not implemented yet')
            
    def getRecommendations(self):
            messagebox.showinfo(' ', 'get recommendations! function not implemented yet') 
   

    ###search tv/movies
    def searchmt(self):
        #TV or Movies combobox
        self.type = ttk.Label(self.searchmt_frame,text='Type')
        self.type.grid(row=0, column=0, padx=0, pady=10, sticky='w')
        self.type_combobox = ttk.Combobox(self.searchmt_frame,values=['Movie','TV Show'])
        self.type_combobox.grid(row=0, column=0, padx=50, pady=10, sticky='w')
        self.type_combobox.set('Movie')
        print("设置默认 show_type：", self.type_combobox.get())  # 验证设置是否成功
        # text entry#
        self.title = self.create_entry('Title:',1,self.searchmt_frame)
        self.director = self.create_entry("Director:", 2,self.searchmt_frame)
        self.actor = self.create_entry("Actor:", 3,self.searchmt_frame)
        self.genre = self.create_entry("Genre:", 4,self.searchmt_frame)
        

        #research button
        self.search_button = ttk.Button(self.searchmt_frame, text="Search", command=self.perform_search_mt)
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

        title= self.Title.get()
        publisher= self.Publisher.get()
        author= self.Author.get()
        #research button
        self.search_button = ttk.Button(self.searchb_frame, text="Search", command=lambda:self.perform_search_b(title,author, publisher))
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
    
    def perform_search_b(self,title, authors, publisher):
        #messagebox.showinfo('Warning','function unfinished')
        self.recommender.searchBooks(title, authors, publisher)
    def perform_search_mt(self):
        # 获取组合框中的值
        self.main_window.update()  # 更新 GUI 状态
        show_type = self.type_combobox.get()
        print("检索到的 show_type：", show_type)  # 打印检索到的 show_type 值
        title = self.title.get()
        director = self.director.get()
        actor = self.actor.get()
        genre = self.genre.get()

        print('good luck', show_type, title, director, actor, genre)

        self.recommender.searchTVMovies(show_type, title, director, actor, genre)
        
    #get recommendations##
    def getrc(self):
        ## Movie, TV Show or Book
        self.type = ttk.Label(self.recommendations_frame,text='Type')
        self.type.grid(row=0, column=0, padx=0, pady=10, sticky='w')
        self.type_combobox = ttk.Combobox(self.recommendations_frame,values=['Movie','TV Show','Book'])
        self.type_combobox.grid(row=0, column=0, padx=50, pady=10, sticky='w')
    ## search title
        # text entry#
        self.Title = self.create_entry('Title:',1,self.recommendations_frame)
        
        #research button
        self.search_button = ttk.Button(self.recommendations_frame, text="Get Recommendation", command=self.getRecommendations) #####
        self.search_button.grid(row=5, column=0, columnspan=2, pady=10, sticky='w')
        
        #result shown#
        self.result_text = tk.Text(self.recommendations_frame, state='disabled')
        self.result_text.grid(row=6, column=0, columnspan=2, padx=0, pady=10, sticky='nsew')
    
def main():
    app = RecommenderGUI()
    app.main_window.mainloop()

if __name__ == "__main__":
    main()