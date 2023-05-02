
#run code from here

# modules
import tkinter as tk
import sqlite3

#import pages
from StartPage import *
from CheckoutPage import *
from SignupPage import *
from AddPage import *
from InventoryPage import *
from OverduePage import *
from LatePage import *

class SampleApp(tk.Tk):

    # constructor
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Connect to the database
        # Connect to the database
        # use self.controller.db_conn to connect in other pages
        self.db_conn = sqlite3.connect('LMS.db')

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="nswe")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Set window size
        self.geometry('350x350')

        self.frames = {} #define frames array
        for F in (StartPage, CheckoutPage, SignupPage, AddPage, InventoryPage, OverduePage, LatePage): #loop that goes thru frames
            page_name = F.__name__ #page name variable
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        #page that will appear when the app is opened
        self.show_frame("StartPage")
        
    #show a frame for the given page name
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = SampleApp()

    app.tk.call("source", "azure.tcl")
    app.tk.call("set_theme", "dark")
    
    app.mainloop()

    