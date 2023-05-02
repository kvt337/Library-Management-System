import tkinter as tk

#menu
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # set number of rows and cols
        for i in range(6):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)

        label = tk.Label(self, text="Library Management System")
        label.grid(row=0, column=0, columnspan=1, pady=10)

        # width constant
        BTN_WIDTH:int = 20

        button1 = tk.Button(self, text="Check Out",
                            width=BTN_WIDTH,
                            command=lambda: controller.show_frame("CheckoutPage"))
        
        button2 = tk.Button(self, text="Sign Up",
                            width=BTN_WIDTH,
                            command=lambda: controller.show_frame("SignupPage"))
        
        button3 = tk.Button(self, text="Add a Book",
                            width=BTN_WIDTH,
                            command=lambda: controller.show_frame("AddPage"))
        
        button4 = tk.Button(self, text="Copies loaned",
                            width=BTN_WIDTH,
                            command=lambda: controller.show_frame("InventoryPage"))
        
        button5 = tk.Button(self, text="View Overdue Books",
                            width=BTN_WIDTH,
                            command=lambda: controller.show_frame("OverduePage"))
        
        button6 = tk.Button(self, text="Search Late Fees",
                            width=BTN_WIDTH,
                            command=lambda: controller.show_frame("LatePage"))

        #order buttons
        # padx = 10 -> 10 pixels
        button1.grid(row=1, column=0, padx=(0, 10))
        button2.grid(row=1, column=1)
        button3.grid(row=2, column=0, padx=(0, 10), pady=(10, 0))
        button4.grid(row=2, column=1, pady=(10, 0))
        button5.grid(row=3, column=0, padx=(0, 10), pady=(10, 0))
        button6.grid(row=3, column=1, pady=(10, 0))