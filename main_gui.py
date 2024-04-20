from tkinter import *    
from tkinter.messagebox import *

window = Tk()
window.title ("LightsOff")
#window.iconbitmap("img/light.ico")
window.geometry("250x25")


boton = Button(window, text="Shutdown lights").pack()

window.mainloop()