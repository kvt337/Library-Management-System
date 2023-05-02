import tkinter as tk

import sqlite3

import random

#requirement 2
class SignupPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        ##########################################
       #sql queries

        def submit(self):
            submit_connect = sqlite3.connect('LMS.db')
            submit_cur = submit_connect.cursor()

            full_name = f_name.get() + " " + l_name.get()
            card_no = random.randint(100000, 999999)
            card_str = str(card_no)

            submit_cur.execute("INSERT INTO BORROWER (Card_No, Name, Address, Phone) VALUES (:card, :name, :address, :phone)",
                            {
                                'card': card_no,
                                'name': full_name,
                                'address': address.get(),
                                'phone': phone_number.get()
                            }    
                            )
            submit_connect.commit()
            submit_connect.close()

            card_output = "Your card number is " + card_str
            card_label = tk.Label(result_frame, text = card_output)
            card_label.grid(row=0, column=0)


        ##########################################

        #frame to hold title
        title_frame = tk.Frame(self)

        label = tk.Label(title_frame, text="Sign Up")
        label.grid(row=0, column=0)

        title_frame.columnconfigure(0, weight=1)
        title_frame.rowconfigure(0, weight=1)

        ###########################################

        #frame to hold user input fields
        input_frame = tk.Frame(self)

        f_name_label = tk.Label(input_frame, text="First Name")
        f_name = tk.Entry(input_frame, width = 30)
        f_name_label.grid(row=1, column=0)
        f_name.grid(row=1, column = 1)

        l_name_label = tk.Label(input_frame, text="Last Name")
        l_name = tk.Entry(input_frame, width = 30)
        l_name_label.grid(row=2, column=0)
        l_name.grid(row=2, column=1)

        phone_number_label = tk.Label(input_frame, text="Phone Number")
        phone_number = tk.Entry(input_frame, width = 30)
        phone_number_label.grid(row=3, column=0)
        phone_number.grid(row=3, column=1)

        address_label = tk.Label(input_frame, text="Address")
        address = tk.Entry(input_frame, width = 30)
        address_label.grid(row=4, column=0)
        address.grid(row=4, column=1)

        ############################################

        #frame to hold query output
        result_frame = tk.Frame(self)

        ############################################

        #frame to hold submit button
        submit_frame = tk.Frame(self)
        sign_up = tk.Button(submit_frame, text="Sign Up", command = lambda: submit(self))
        sign_up.grid(row=5, column=0)

        ############################################
    
        #frame to hold menu button
        menu_frame = tk.Frame(self)
        button = tk.Button(menu_frame, text="Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=6, column=0)

        ###########################################

        #order frames
        title_frame.grid(row=0, column=0)
        input_frame.grid(row=1, column=0)
        result_frame.grid(row=2, column=0)
        submit_frame.grid(row=3, column=0)
        menu_frame.grid(row=4,column=0)

       #############################################