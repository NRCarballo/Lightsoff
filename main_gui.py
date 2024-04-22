from tkinter import *    
from tkinter import messagebox


def cmd():
    messagebox.showinfo(message="Estamos trabajando en esto..")
    print("Estamos trabajando en esto..")

window = Tk()
window.title ("LightsOff")
#window.iconbitmap("img/light.ico")
window.geometry("250x25")
boton = Button(window, command=cmd,  text="Shutdown lights").pack()
window.mainloop()