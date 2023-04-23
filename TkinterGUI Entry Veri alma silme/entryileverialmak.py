import tkinter as tk

pencere = tk.Tk()
pencere.geometry("800x600")

text1 = tk.Entry(pencere, state="readonly", width=30) # yalnızca okunabilen bilgi
text1.place(x=20, y=20)

def veriGetir():
    if(textVeri.get() == ""):
        etiketVeriGoster["text"] = "Geçersiz Değer"
    else:
         etiketVeriGoster["text"] = textVeri.get()
         #text1["width"] = textVeri.get()
         #text1.place(y=textVeri.get())

def veriSil():
    if(textVeri.get() != ""):
        textVeri.delete(0, "end")
    else:
        etiketVeriGoster["text"] = "☺"

textVeri = tk.Entry(pencere, text="Veri Giriş")
textVeri.place(x=20, y=50)

buton = tk.Button(pencere, text="Bilgileri Al", command=veriGetir)
buton.place(x=20, y=120)
etiketVeriGoster = tk.Label(pencere, text="")
etiketVeriGoster.place(x=20, y=90)
butonSil = tk.Button(pencere, text="Bilgi Sil", command=veriSil)
butonSil.place(x=120, y=120)
pencere.mainloop()
