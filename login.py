import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
from users import user
from dashboard import DashBoard

class Login(tk.Toplevel):   
    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.title("Login")
        width=508
        height=258
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLineEdit_452=tk.Entry(self, name="txtUsuario")
        GLineEdit_452["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_452["font"] = ft
        GLineEdit_452["fg"] = "#333333"
        GLineEdit_452["justify"] = "center"
        GLineEdit_452["text"] = ""
        GLineEdit_452.place(x=210,y=50,width=154,height=50)

        GLineEdit_580=tk.Entry(self, name="txtContrasenia", show="*")
        GLineEdit_580["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_580["font"] = ft
        GLineEdit_580["fg"] = "#333333"
        GLineEdit_580["justify"] = "center"
        GLineEdit_580["text"] = ""
        GLineEdit_580.place(x=210,y=130,width=155,height=50)

        GLabel_647=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_647["font"] = ft
        GLabel_647["fg"] = "#333333"
        GLabel_647["justify"] = "center"
        GLabel_647["text"] = "Usuario"
        GLabel_647.place(x=120,y=60,width=70,height=25)

        GLabel_641=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_641["font"] = ft
        GLabel_641["fg"] = "#333333"
        GLabel_641["justify"] = "center"
        GLabel_641["text"] = "Contraseña"
        GLabel_641.place(x=120,y=140,width=70,height=25)

        GButton_897=tk.Button(self)
        GButton_897["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_897["font"] = ft
        GButton_897["fg"] = "#000000"
        GButton_897["justify"] = "center"
        GButton_897["text"] = "Crear cuenta"
        GButton_897.place(x=50,y=200,width=137,height=39)
        GButton_897["command"] = self.GButton_897_command

    def iniciar_sesion(self):
        try:
            txtUsuario = self.nametowidget("txtUsuario")
            usuario = txtUsuario.get()            

            txtContrasenia = self.nametowidget("txtContrasenia")
            contrasenia = txtContrasenia.get()

            if usuario != "":
                if user.validar(usuario, contrasenia):
                    Dashboard(self.master)
                    self.destroy()
                else:
                    tkMsgBox.showwarning(self.master.title(), "Usuario/Contraseña incorrecta")
            else:
                tkMsgBox.showwarning(self.master.title(), "Ingrese el Usuario para iniciar sesión")
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))

    def cerrar(self):
        self.destroy()

    def abrir_user(self):
        User(self.master)

        
