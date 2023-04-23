import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

pencere = Tk()
pencere.geometry("800x600")

def fotoEkle():
    fotoDialog = filedialog.askopenfilename(title="Fotoğraf Seçme", multiple=True, filetypes=(("png","*.png"),("jpg", "*.jpg"),("bmp", "*.bmp")))
    
    for i in fotoDialog:
        img = Image.open(i)  # foto okunur ve açılır
        img = img.resize((300,300)) # new width & height
        img = ImageTk.PhotoImage(img)  # Fotograf türünde olduğu belirtiliyor
        fotoEtiketi = Label(pencere)  # Fotonun içine gonderileceği etiket tanımlanıyor
        fotoEtiketi.place(x=100, y=100) # Etiket konumlandırma
        fotoEtiketi.image = img # fotograf etikete eklenir
        fotoEtiketi["image"] = img
        
        
buton = Button(pencere, text="Fotoğraf Ekle", command=fotoEkle)
buton.place(x=380, y=20)

pencere.mainloop()