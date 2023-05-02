import tkinter as tk
import sqlite3

#requirment 5
class OverduePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #####################################################

        #frame to hold title
        title_frame = tk.Frame(self)

        label = tk.Label(title_frame, text="Overdue Books")
        label.grid(row=0, column=0)

        title_frame.columnconfigure(0, weight=1)
        title_frame.rowconfigure(0, weight=1)

        ######################################################

        # User input
        input_frame = tk.Frame(self)

        # Date out
        date_out_label = tk.Label(input_frame, text="Date Out")
        self.date_out = tk.Entry(input_frame, width=30)
        date_out_label.grid(row=1, column=0)
        self.date_out.grid(row=1, column=1)

        # Due date
        due_date_label = tk.Label(input_frame, text="Due Date")
        self.due_date = tk.Entry(input_frame, width=30)
        due_date_label.grid(row=2, column=0)
        self.due_date.grid(row=2, column=1)

        ######################################################

        #frame to hold output of query
        self.result_frame = tk.Frame(self)

        #####################################################
    
        #frame to hold menu button
        menu_frame = tk.Frame(self)

        button = tk.Button(menu_frame, text="Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=5, column=0)

        submit_frame = tk.Frame(self)
        checkout = tk.Button(submit_frame, text="Check", command=self.check_Overdue)
        checkout.grid(row=4, column=0)

        #####################################################

        #order frames
        title_frame.grid(row=0, column=0)
        input_frame.grid(row=1, column=0)
        self.result_frame.grid(row=2, column=0)
        submit_frame.grid(row=4, column=0)
        menu_frame.grid(row=4,column=1)
    
    def check_Overdue(self):
        
        # connect to the database
        conn = sqlite3.connect('LMS.db')
        cursor = conn.cursor()

        # get input from user
        date_out_input = self.date_out.get()
        due_date_input = self.due_date.get()

        # Get Book_Loans based on date out and due date
        cursor.execute("""SELECT Card_No, Book_Id, 
                        Branch_Id, Date_Out, 
                        Due_Date, Returned_Date, 
                        julianday(Returned_Date) - julianday(Due_Date) AS Days_Late
                        FROM BOOK_LOANS
                        WHERE Returned_Date > Due_Date 
                        AND Due_Date BETWEEN ? AND ?""", (date_out_input, due_date_input))
        late_books = cursor.fetchall()

        # Clean previous table
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        # Print table with result

        # if values iin late_books, print table
        if late_books:

            # columns headers
            headers = ['Card No', 'Book ID', 'Branch ID', 'Date Out', 'Due Date', 'Returned Date', 'Days Late']
            for i, col in enumerate(headers):

                # create label column header 
                label = tk.Label(self.result_frame, text=col, font='bold')
                label.grid(row=0, column=i)

            # row info
            for i, row in enumerate(late_books):
                for j, val in enumerate(row):

                    # create label for row data
                    label = tk.Label(self.result_frame, text=val)
                    label.grid(row=i+1, column=j)

        # if the late_books is empty, print no results message
        else:
            label = tk.Label(self.result_frame, text='No results found.')
            label.pack()

        # close database connection
        conn.close()