from tkinter import *
from PIL import Image, ImageTk

pencere = Tk()
pencere.title("Fotoğraf İşlemleri")
pencere.geometry("800x600")


resim = ImageTk.PhotoImage(Image.open("img.jpg"))
Label(pencere,  image=resim).place(x=20, y=20)

pencere.mainloop()