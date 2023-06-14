from tkinter import *

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.withdraw()

        login_window = Toplevel()
        login_window.title("Login")
        login_window.resizable(0, 0)
        login_window.geometry("300x100")
        login_window.configure(background='white')

        login_label = Label(login_window, text="Please login before continuing.")
        login_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.name_label = Label(login_window, text="Name:")
        self.name_label.pack()

        self.name_entry = Entry(login_window)
        self.name_entry.pack()

        login_button = Button(login_window, text="Login", command=lambda: self.goAhead(self.name_entry.get()))
        login_button.pack()

        self.window.mainloop()

    def goAhead(self, name):
        self.login_window.destroy()
        # Start receive thread here

        self.username = name

    def receive(self):
        while True:
            # Receive and process messages
            pass

GUI()
