import tkinter as tk
import sqlite3

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

        book_title_label = tk.Label(input_frame, text="Book Title")
        self.book_title = tk.Entry(input_frame, width=30)
        book_title_label.grid(row=1, column=0)
        self.book_title.grid(row=1, column=1)

        author_label = tk.Label(input_frame, text="Author")
        self.author = tk.Entry(input_frame, width=30)
        author_label.grid(row=2, column=0)
        self.author.grid(row=2, column=1)

        branch_label = tk.Label(input_frame, text="Branch")
        self.branch = tk.Entry(input_frame, width=30)
        branch_label.grid(row=3, column=0)
        self.branch.grid(row=3, column=1)

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
        branch_input = self.branch.get()

        conn = sqlite3.connect('LMS.db')
        cursor = conn.cursor()

        # Checkout book and update Book_Copies table
        cursor.execute('''
            UPDATE BOOK_COPIES
            SET No_Of_Copies = No_Of_Copies - 1
            WHERE Book_Id IN (
                SELECT BOOK.Book_Id
                FROM BOOK
                JOIN BOOK_AUTHORS ON BOOK.Book_Id = BOOK_AUTHORS.Book_Id
                WHERE Title = ? AND Author_Name = ?)
            AND Branch_Id IN (
                SELECT Branch_Id
                FROM LIBRARY_BRANCH
                WHERE Branch_Name = ?)
        ''', (book_title_input, author_input, branch_input))
        conn.commit()

        # Get the updated number of copies
        cursor.execute('''
            SELECT No_Of_Copies
            FROM BOOK_COPIES
            WHERE Book_Id IN (
                SELECT BOOK.Book_Id
                FROM BOOK
                JOIN BOOK_AUTHORS ON BOOK.Book_Id = BOOK_AUTHORS.Book_Id
                WHERE Title = ? AND Author_Name = ?)
            AND Branch_Id IN (
                SELECT Branch_Id
                FROM LIBRARY_BRANCH
                WHERE Branch_Name = ?)
        ''', (book_title_input, author_input, branch_input))
        
        result = cursor.fetchone()
        if result is not None:
            updated_copies = result[0]
            self.result_label.config(text=f"Updated number of copies: {updated_copies}")
        else:
            self.result_label.config(text="No matching records found.")

        # Close the connection
        conn.close()
