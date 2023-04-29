import tkinter as tk

#menu
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to the Library Database Management System!")
        label.grid(row=0, column=0, pady=10)

        button1 = tk.Button(self, text="Check Out",
                            command=lambda: controller.show_frame("CheckoutPage"))
        button2 = tk.Button(self, text="Sign Up",
                            command=lambda: controller.show_frame("SignupPage"))
        button3 = tk.Button(self, text="Add a Book",
                            command=lambda: controller.show_frame("AddPage"))
        button4 = tk.Button(self, text="View Book Inventory",
                            command=lambda: controller.show_frame("InventoryPage"))
        button5 = tk.Button(self, text="View Overdue Books",
                            command=lambda: controller.show_frame("OverduePage"))
        button6 = tk.Button(self, text="Search Late Fees",
                            command=lambda: controller.show_frame("LatePage"))

        #order buttons
        button1.grid(row=1, column=0)
        button2.grid(row=2, column=0)
        button3.grid(row=3, column=0)
        button4.grid(row=4, column=0)
        button5.grid(row=5, column=0)
        button6.grid(row=6, column=0)