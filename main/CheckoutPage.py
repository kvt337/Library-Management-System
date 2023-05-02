import tkinter as tk
import sqlite3
import datetime

class CheckoutPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Title
        title_frame = tk.Frame(self)
        label = tk.Label(title_frame, text="Check Out")
        label.grid(row=0, column=0)
        title_frame.columnconfigure(0, weight=1)
        title_frame.rowconfigure(0, weight=1)

        # User input
        input_frame = tk.Frame(self)

        # book title input
        book_title_label = tk.Label(input_frame, text="Book Title")
        self.book_title = tk.Entry(input_frame, width=30)
        book_title_label.grid(row=1, column=0)
        self.book_title.grid(row=1, column=1)

        # Author input
        author_label = tk.Label(input_frame, text="Author")
        self.author = tk.Entry(input_frame, width=30)
        author_label.grid(row=2, column=0)
        self.author.grid(row=2, column=1)
        
        # Branch input
        branch_label = tk.Label(input_frame, text="Branch")
        self.branch = tk.Entry(input_frame, width=30)
        branch_label.grid(row=3, column=0)
        self.branch.grid(row=3, column=1)

        # Card_No input
        card_no_label = tk.Label(input_frame, text="Card No")
        self.card_no = tk.Entry(input_frame, width=30)
        card_no_label.grid(row=4, column=0)
        self.card_no.grid(row=4, column=1)

        # Output of the query
        result_frame = tk.Frame(self)
        self.result_label = tk.Label(result_frame, text="")
        self.result_label.grid(row=0, column=0)

        # Submit button
        submit_frame = tk.Frame(self)
        checkout = tk.Button(submit_frame, text="Check Out", command=self.checkout_book)
        checkout.grid(row=4, column=0)

        # Menu button
        menu_frame = tk.Frame(self)
        button = tk.Button(menu_frame, text="Menu", command=lambda: controller.show_frame("StartPage"))
        button.grid(row=5, column=0)

        # Order the frames
        title_frame.grid(row=0, column=0)
        input_frame.grid(row=1, column=0)
        result_frame.grid(row=2, column=0)
        submit_frame.grid(row=4, column=0)
        menu_frame.grid(row=4, column=1)

    def checkout_book(self):
        book_title_input = self.book_title.get()
        author_input = self.author.get()
        branch_input = int(self.branch.get())
        card_no_input = int(self.card_no.get())

        # connect to the database
        conn = sqlite3.connect('LMS.db')
        cursor = conn.cursor()

        # Find book id
        cursor.execute('SELECT Book_Id FROM BOOK WHERE Title = ? AND Book_Id IN (SELECT Book_Id FROM BOOK_AUTHORS WHERE Author_Name = ?)', (book_title_input, author_input))
        book_id = cursor.fetchone()

        if book_id is None:
            self.result_label.config(text="Book not found")
            return
        
        # Check if the book has already been checked out by the borrower
        cursor.execute('SELECT Book_Id FROM BOOK_LOANS WHERE Book_Id = ? AND Card_No = ?', (book_id[0], card_no_input))
        existing_loan = cursor.fetchone()
        if existing_loan is not None:
            self.result_label.config(text="Book already checked out by the borrower")
            return

        # Find the number of copies at the branch
        cursor.execute('SELECT No_Of_Copies FROM BOOK_COPIES WHERE Book_Id = ? AND Branch_Id = ?', (int(book_id[0]), int(branch_input),))
        copies = cursor.fetchone()

        if copies is None or copies[0] < 1:
            self.result_label.config(text="No copies available at this branch")
            return
        
        # Add a new loan
        date_out = datetime.date.today()
        due_date = date_out + datetime.timedelta(days=14)

        cursor.execute('INSERT INTO BOOK_LOANS (Book_Id, Branch_Id, Card_No, Date_Out, Due_Date) VALUES (?, ?, ?, ?, ?)', (int(book_id[0]), int(branch_input), int(card_no_input), date_out, due_date))

        # Update the number of copies in BOOK_COPIES
        updated_copies = copies[0] - 1
        cursor.execute('UPDATE BOOK_COPIES SET No_Of_Copies = ? WHERE Book_Id = ? AND Branch_Id = ?', (int(updated_copies), int(book_id[0]), int(branch_input)))


        # commit changes and close the connection
        conn.commit()
        conn.close()

        # success message
        self.result_label.config(text="Book checked out successfully. Updated number of copies: {}".format(updated_copies))

        # clean
        self.book_title.delete(0, 'end')
        self.author.delete(0, 'end')
        self.branch.delete(0, 'end')
        self.card_no.delete(0, 'end')
