from tkinter import *
import tkinter.messagebox as tm


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_1 = Label(self, text="Username")#text
        self.label_2 = Label(self, text="Password")
        self.label_3 = Label(self, text="Welcome to Sphere")

        self.entry_1 = Entry(self)#textbox
        self.entry_2 = Entry(self, show="*")

        self.label_1.grid(row=0, sticky=E)##gridplacing
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)
        self.label_3.grid(row=0, column=0)

        self.checkbox = Checkbutton(self, text="Keep me logged in")#checkbox
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command = self._login_btn_clickked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clickked(self):
        #print("Clicked")
        username = self.entry_1.get()
        password = self.entry_2.get()

        #print(username, password)

        if username == "john" and password == "password":
            tm.showinfo("Login info", "Welcome John")
            window.Tk()
        else:
            tm.showerror("Login error", "Incorrect username")




        
root = Tk()
lf = LoginFrame(root)
Page = slopeFrame()
Page.createwindow()
root.mainloop()
