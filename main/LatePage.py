import tkinter as tk

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
        borrower = tk.Entry(input_frame, width = 15)
        borrower_id_label.grid(row=1, column=0)
        borrower.grid(row=1, column = 1);

        name_label = tk.Label(input_frame, text="Name")
        name = tk.Entry(input_frame, width = 15)
        name_label.grid(row=2, column=0)
        name.grid(row=2, column=1);

        #by book
        book_id_label = tk.Label(input_frame, text="Book ID")
        book_id = tk.Entry(input_frame, width = 15)
        book_id_label.grid(row=1, column=2)
        book_id.grid(row=1, column = 3);

        title_label = tk.Label(input_frame, text="Author")
        title = tk.Entry(input_frame, width = 15)
        title_label.grid(row=2, column=2)
        title.grid(row=2, column=3);


        ############################################

        #frame to hold query output
        result_frame = tk.Frame(self)

        ############################################

        #frame to hold submit buttons
        submit_frame = tk.Frame(self)

        #by user
        search_user = tk.Button(submit_frame, text="Search")
        search_user.grid(row=4, column=0, padx=70)

        #by book
        search_book = tk.Button(submit_frame, text="Search")
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