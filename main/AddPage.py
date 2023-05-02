import tkinter as tk
import sqlite3

#requirement 3
class AddPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        ############################################
        # frame to hold the title
        title_frame = tk.Frame(self)

        label = tk.Label(title_frame, text="Add a Book")
        label.grid(row=0, column=0)

        title_frame.columnconfigure(0, weight=1)
        title_frame.rowconfigure(0, weight=1)

        ###########################################

        # frame to hold user input
        input_frame = tk.Frame(self)

        book_title_label = tk.Label(input_frame, text="Book Title")
        self.book_title = tk.Entry(input_frame, width = 30)
        book_title_label.grid(row=1, column=0)
        self.book_title.grid(row=1, column = 1)

        author_label = tk.Label(input_frame, text="Author")
        self.author = tk.Entry(input_frame, width = 30)
        author_label.grid(row=2, column=0)
        self.author.grid(row=2, column=1)

        publisher_label = tk.Label(input_frame, text="Publisher")
        self.publisher = tk.Entry(input_frame, width = 30)
        publisher_label.grid(row=3, column=0)
        self.publisher.grid(row=3, column=1)

        # Output of the query
        result_frame = tk.Frame(self)
        result_frame.grid(row=2, column=0)
        self.result_label = tk.Label(result_frame, text="")
        self.result_label.grid(row=0, column=0)

        ############################################

        #frame to hold submit button
        submit_frame = tk.Frame(self)

        add = tk.Button(submit_frame, text="Add Book", command=self.add_Book)
        add.grid(row=4, column=0)

        ############################################
    
        #frame to hold menu button
        menu_frame = tk.Frame(self)

        button = tk.Button(menu_frame, text="Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=5, column=0)

        ###########################################

        #order the frames
        title_frame.grid(row=0, column=0)
        input_frame.grid(row=1, column=0)
        self.result_label.grid(row=2, column=0)
        submit_frame.grid(row=3, column=0)
        menu_frame.grid(row=3,column=1)
        

    def add_Book(self):
        
        # connect to database
        conn = sqlite3.connect('LMS.db')
        cursor = conn.cursor()

        # get input from user
        book_title_input = self.book_title.get()
        author_input = self.author.get()
        publisher_input = self.publisher.get()

        # Get publisher id
        cursor.execute('SELECT Publisher_Name FROM PUBLISHER WHERE Publisher_Name = ?', (publisher_input,))
        publisher_id = cursor.fetchone()

        # check if publisher on file
        if publisher_id is None:
            self.result_label.config(text="Publisher not found")
            return
        
        # Get the maximum book id in the BOOK table
        cursor.execute('SELECT MAX(Book_Id) FROM BOOK')
        max_book_id = cursor.fetchone()[0]

        # Generate a new book id
        new_book_id = max_book_id + 1

        # Add the book to BOOK table
        cursor.execute('INSERT INTO BOOK (Book_Id, Title, Publisher_Name) VALUES (?, ?, ?)', (int(new_book_id), book_title_input, publisher_input,))
        
        # Add the author BOOK_AUTHORS table
        cursor.execute('INSERT INTO BOOK_AUTHORS (Book_Id, Author_Name) VALUES (?, ?)', (new_book_id, author_input,))

        # Add 5 copies of the book to each library branch in BOOK_COPIES table
        branches = cursor.execute('SELECT Branch_Id FROM LIBRARY_BRANCH').fetchall()
        for branch in branches:
            cursor.execute('INSERT INTO BOOK_COPIES (Book_Id, Branch_Id, No_Of_Copies) VALUES (?, ?, ?)', (int(new_book_id), int(branch[0]), 5))
        
        # commit changes and close the connection
        conn.commit()
        conn.close()

        # success message
        self.result_label.config(text="Book added successfully")

        # clean
        self.book_title.delete(0, 'end')
        self.author.delete(0, 'end')
        self.publisher.delete(0, 'end')