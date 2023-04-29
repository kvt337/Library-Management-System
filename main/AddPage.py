import tkinter as tk

#requirement 3
class AddPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        ############################################
        #frame to hold the title
        title_frame = tk.Frame(self)

        label = tk.Label(title_frame, text="Add a Book")
        label.grid(row=0, column=0)

        title_frame.columnconfigure(0, weight=1)
        title_frame.rowconfigure(0, weight=1)

        ###########################################

        #frame to hold user input
        input_frame = tk.Frame(self)

        book_title_label = tk.Label(input_frame, text="Book Title")
        book_title = tk.Entry(input_frame, width = 30)
        book_title_label.grid(row=1, column=0)
        book_title.grid(row=1, column = 1);

        author_label = tk.Label(input_frame, text="Author")
        author = tk.Entry(input_frame, width = 30)
        author_label.grid(row=2, column=0)
        author.grid(row=2, column=1);

        publisher_label = tk.Label(input_frame, text="Publisher")
        publisher = tk.Entry(input_frame, width = 30)
        publisher_label.grid(row=3, column=0)
        publisher.grid(row=3, column=1);

        ############################################

        #frame to hold submit button
        submit_frame = tk.Frame(self)

        add = tk.Button(submit_frame, text="Add Book")
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
        submit_frame.grid(row=2, column=0)
        menu_frame.grid(row=3,column=0)