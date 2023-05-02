import tkinter as tk
import sqlite3

#requirement 6
class LatePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        ##########################################

        #frame to hold title
        title_frame = tk.Frame(self)

        #title 1
        user_label=tk.Label(title_frame, text="Search by User")
        user_label.grid(row=0, column=0, padx=50)

        #title 2
        book_label=tk.Label(title_frame, text="Search by Book")
        book_label.grid(row=0, column=1, padx=10)

        title_frame.columnconfigure(0, weight=1)
        title_frame.rowconfigure(0, weight=1)

        ###########################################

        #frame to hold user input
        input_frame = tk.Frame(self)

        #by user
        borrower_id_label = tk.Label(input_frame, text="User ID")
        self.borrower = tk.Entry(input_frame, width = 15)
        borrower_id_label.grid(row=1, column=0)
        self.borrower.grid(row=1, column = 1);

        name_label = tk.Label(input_frame, text="Name")
        self.name = tk.Entry(input_frame, width = 15)
        name_label.grid(row=2, column=0)
        self.name.grid(row=2, column=1);

        #by book
        book_id_label = tk.Label(input_frame, text="Book ID")
        self.book_id = tk.Entry(input_frame, width = 15)
        book_id_label.grid(row=1, column=2)
        self.book_id.grid(row=1, column = 3);

        title_label = tk.Label(input_frame, text="Title")
        self.title = tk.Entry(input_frame, width = 15)
        title_label.grid(row=2, column=2)
        self.title.grid(row=2, column=3);


        ############################################

        #frame to hold query output
        result_frame = tk.Frame(self)
        self.result_label = tk.Label(result_frame, text="")
        self.result_label.grid(row=0, column=0)


        ############################################

        #frame to hold submit buttons
        submit_frame = tk.Frame(self)

        #by user
        search_user = tk.Button(submit_frame, text="Search", command = self.searchUser)
        search_user.grid(row=4, column=0, padx=70)

        #by book
        search_book = tk.Button(submit_frame, text="Search", command = self.searchBook)
        search_book.grid(row=4, column=1, padx=30)

        ############################################
    
        #frame to hold menu button
        menu_frame = tk.Frame(self)

        button = tk.Button(menu_frame, text="Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=5, column=0)

        ###########################################

        #order frames
        title_frame.grid(row=0, column=0)
        input_frame.grid(row=1, column=0)
        result_frame.grid(row=2, column=0)
        submit_frame.grid(row=3, column=0)
        menu_frame.grid(row=4,column=0)

    def searchUser(self):
        conn = sqlite3.connect('LMS.db')
        cursor = conn.cursor()

        uid_in = self.borrower.get()
        name_in = self.name.get()

        if uid_in and name_in:
            cursor.execute('select Card_No, Borrower_Name, LateFeeBalance from vBookLoanInfo where Card_No = ? and Borrower_Name LIKE ?', (uid_in, '%'+name_in+'%',))
        elif uid_in:
            cursor.execute('select Card_No, Borrower_Name, LateFeeBalance from vBookLoanInfo where Card_No = ?', (uid_in,))
        elif name_in:
            cursor.execute("select Card_No, Borrower_Name, LateFeeBalance from vBookLoanInfo where Borrower_Name LIKE ?", ('%'+name_in+'%',))
        else:
            cursor.execute('select Card_No, Borrower_Name, LateFeeBalance from vBookLoanInfo order by LateFeeBalance desc')
        temp = cursor.fetchall()
        if(temp):
            result_text = ""
            for i in temp:
                result_text += f"Card No.: {i[0]}\t Name: {i[1]}\t Late Fee: ${i[2]:.2f}\n"
            self.result_label.config(text=result_text)
        else:
            self.result_label.config(text="User Not Found")
        conn.close()


    def searchBook(self):
        conn = sqlite3.connect('LMS.db')
        cursor = conn.cursor()

        bid_in = self.book_id.get()
        title_in = self.title.get()

        if bid_in and title_in:
            cursor.execute('select Book_Title, LateFeeBalance from vBookLoanInfo vbli join Book b on b.Title = vbli.Book_Title where Book_Id = ? and Book_Title LIKE ?', (bid_in, '%'+title_in+'%',))
        elif bid_in:
            cursor.execute('select Book_Title, LateFeeBalance from vBookLoanInfo vbli join Book b on b.Title = vbli.Book_Title where Book_Id = ?', (bid_in,))
        elif title_in:
            cursor.execute("select Book_Title, LateFeeBalance from vBookLoanInfo where Book_Title LIKE ?", ('%'+title_in+'%',))
        else:
            cursor.execute('select Book_Title, LateFeeBalance from vBookLoanInfo order by LateFeeBalance desc')
        temp = cursor.fetchall()
        if(temp):
            result_text = ""
            for i in temp:
                result_text += f"Book: {i[0]}\t Late Fee: ${i[1]:.2f}\n"
            self.result_label.config(text=result_text)
        else:
            self.result_label.config(text="Book Not Found")
        conn.close()
        