import tkinter as tk

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

        #frame to hold output of query
        result_frame = tk.Frame(self)

        #####################################################
    
        #frame to hold menu button
        menu_frame = tk.Frame(self)

        button = tk.Button(menu_frame, text="Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=5, column=0)

        #####################################################

        #order frames
        title_frame.grid(row=0, column=0)
        result_frame.grid(row=1, column=0)
        menu_frame.grid(row=2,column=0)