import tkinter as tk
import sqlite3

#requirement 4
class InventoryPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        ####################################################

        # title frame
        title_frame = tk.Frame(self)

        label = tk.Label(title_frame, text="Copies loaned ")
        label.grid(row=0, column=0)

        title_frame.columnconfigure(0, weight=1)
        title_frame.rowconfigure(0, weight=1)

        # user input frame
        input_frame = tk.Frame(self)

        book_title_label = tk.Label(input_frame, text="Book Title")
        self.book_title = tk.Entry(input_frame, width = 30)
        book_title_label.grid(row=1, column=0)
        self.book_title.grid(row=1, column = 1)

        ############################################

        # submit button frame
        submit_frame = tk.Frame(self)

        add = tk.Button(submit_frame, text="List copies loaned", command=self.loaned_books)
        add.grid(row=4, column=0)
        ######################################################

        # Output of the query
        result_frame = tk.Frame(self)
        result_frame.grid(row=2, column=0)
        self.result_label = tk.Label(result_frame, text="")
        self.result_label.grid(row=0, column=0)

        #####################################################
    
        # menu button frame
        menu_frame = tk.Frame(self)
        button = tk.Button(menu_frame, text="Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=5, column=0)

        #####################################################

        # order of frames
        title_frame.grid(row=0, column=0)
        input_frame.grid(row=1, column=0)
        result_frame.grid(row=2, column=0)
        submit_frame.grid(row=3, column=0)
        menu_frame.grid(row=3,column=1)
    
    def loaned_books(self):

        # get user input
        book_title_input = self.book_title.get()

        # connect to database
        conn = sqlite3.connect('LMS.db')
        cursor = conn.cursor()

        # check if book exists in BOOK table
        cursor.execute('SELECT * FROM BOOK WHERE Title = ?', (book_title_input,))
        book = cursor.fetchone()

        # If not, print notification and close connection
        if book is None:
            self.result_label.config(text="Book not found in library")
            conn.close()
            return

        # search for number of loaned copies per branch
        cursor.execute("""SELECT Branch_Name, COUNT(*) 
                        FROM BOOK_LOANS BL 
                        JOIN LIBRARY_BRANCH LB ON BL.Branch_Id = LB.Branch_Id 
                        JOIN BOOK B ON BL.Book_Id = B.Book_Id 
                        WHERE B.Title = ? GROUP BY Branch_Name""", (book_title_input,))
        copies = cursor.fetchall()

        # if book copies not loaned, display message
        if len(copies) == 0:
            self.result_label.config(text="The book is not loaned in any branch")

        # update label with output of query
        result_text = ""
        for copy in copies:
            result_text += copy[0] + ": " + str(copy[1]) + "\n"
        self.result_label.config(text=result_text)

        # close connection
        conn.close()
