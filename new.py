from tkinter import *
#from PIL import Image, ImageTk
from tkinter import messagebox
root = Tk()
root.title("my tk")
root.geometry("400x500")
root.config(background = "light blue")
#upload = Image.open("a.jpg")
#i1 = ImageTk.PhotoImage(upload)
#l1 = Label(root, image = i1, height = 100, width = 100)
#l1.pack()
l2 = Label(root, text = "welcome")
l2.pack()
def msg():
    messagebox.askyesnocancel("Greet", "Welcome to Tkinter Message Box!")
b1 = Button(root, text = "Welcome!", command = msg)
b1.pack()

root.mainloop()