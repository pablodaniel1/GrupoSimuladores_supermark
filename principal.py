import tkinter as tk
import tkinter.font as tkFont
from login import Login
from db import Db

  

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=516
        height=207
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_765=tk.Button(root)
        GButton_765["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_765["font"] = ft
        GButton_765["fg"] = "#000000"
        GButton_765["justify"] = "center"
        GButton_765["text"] = "Button"
        GButton_765.place(x=150,y=50,width=202,height=79)
        GButton_765["command"] = self.abrir_login

    def abrir_login(self):
        Login(self.root)

if __name__ == "__main__":
    Db.crear_tablas()
    Db.poblar_tablas()
    project = "SUPERMARKET" #"supermarket"
    root = tk.Tk()
    root.iconbitmap(default=f"{project}.ico")
    app = App(root, project.capitalize())
    root.mainloop()
