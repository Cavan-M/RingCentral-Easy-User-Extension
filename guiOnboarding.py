# Cavan McLellan's Tkinter Quick Start
# To Use: Copy and Paste the code below and modified the copied code as per your project
from tkinter import *
import tkinter
import tkinter.ttk
from ringCentral import CreateExtension
import os


class Application:
    def __init__(self):

        os.environ['clientId'] = 'clientId'
        os.environ['clientSecret'] = 'clientSecret'
        os.environ['serverURL'] = 'serverURL'
        os.environ['username'] = 'username'
        os.environ['extension'] = 'extension'
        os.environ['password'] = 'password'
        self.account = CreateExtension()

        # Tkinter Window
        self.root = tkinter.Tk()
        self.root.iconbitmap('icon.ico')
        self.root.title('Create Ring Central Extension')
        self.window = tkinter.Frame(self.root, bg='#ffffff')

        # Make app not-resizable; Params: (x, y)
        self.root.resizable(False, False)

        # Set the minimum size of the Application
        self.root.minsize(400, 200)

        # equivalent of tkinter.Tk().mainloop()
        self.root.update_idletasks()
        self.root.update()

        # Fonts
        self.hev16B = ("Helvetica", 16, "bold")
        self.hev18B = ("Helvetica", 18, "bold")
        self.hev12N = ("Helvetica", 12, "normal")
        self.hev12B = ("Helvetica", 12, "bold")

        # Styling
        self.style = tkinter.ttk.Style()

        # Orange button
        self.style.configure('orange.TButton', font=self.hev12B, foreground='orange', background="orange")
        # Blue Button
        self.style.configure('blue.TButton', font=self.hev12B, foreground='blue', background="blue")

        # Widgets
        self.firstName = StringVar(self.window, value='First Name')
        self.lastName = StringVar(self.window, value='Last Name')
        self.emailAdd = StringVar(self.window, value='Email Address')
        self.nameLabel = tkinter.ttk.Label(self.window, font=self.hev16B, text="First Name:")
        self.nameEntry = tkinter.ttk.Entry(self.window, exportselection=0, font=self.hev12N)
        self.surnameLabel = tkinter.ttk.Label(self.window, font=self.hev16B, text="Last Name:")
        self.surnameEntry = tkinter.ttk.Entry(self.window, exportselection=0, font=self.hev12N)
        self.emailLabel = tkinter.ttk.Label(self.window, font=self.hev16B, text="Email:")
        self.emailEntry = tkinter.ttk.Entry(self.window, exportselection=0, font=self.hev12N)
        self.extLabel = tkinter.ttk.Label(self.window, font=self.hev16B, text="Extension:")
        self.extEntry = tkinter.ttk.Entry(self.window, exportselection=0, font=self.hev12N)
        self.button1 = tkinter.ttk.Button(self.window, text="Orange Button", command=self.buttonfunction, style='orange.TButton')
        self.button2 = tkinter.ttk.Button(self.window, text="Create Extension", command=self.buttonfunction, style='blue.TButton')

        # Widget placement
        self.window.pack(fill='both', expand=True, padx=0, pady=0)
        self.nameLabel.grid(row=1, column=0)
        self.nameEntry.grid(row=1, column=1)
        self.surnameLabel.grid(row=2, column=0)
        self.surnameEntry.grid(row=2, column=1)
        self.emailLabel.grid(row=3, column=0)
        self.emailEntry.grid(row=3, column=1)
        self.extLabel.grid(row=4, column=0)
        self.extEntry.grid(row=4, column=1)
        #self.button1.grid(row=0, column=0)
        self.button2.grid(row=5, column=1)

        # Application Variables
        self.running = True

        # Run Application
        self.run()

    def run(self):
        while self.running:
            """
            Put your looping code here
            """

            # Update Application
            try:
                self.root.update_idletasks()
                self.root.update()
            except tkinter.TclError:
                print("Exiting")
                exit(0)

    def buttonfunction(self):
        self.account.setContact(self.nameEntry.get(), self.surnameEntry.get(), self.emailEntry.get())
        self.account.setExtension(self.extEntry.get())
        print(self.account.getBody())
        
        self.account.login()
        self.account.send()




# call the class to run
Application()
