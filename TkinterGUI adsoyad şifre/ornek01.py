import tkinter as tk
from tkinter import messagebox

def mesaj():
    msg = messagebox.showinfo(title="Bilgi Kutusu", message="Giriş Düğmesine Tıklandı\nTebrikler")

def cikis():
    msg = messagebox.askquestion(title="Çıkış İşlemi", message="Çıkmak İstiyor Musunuz?")
    if(msg == "yes"):
        # exit(0)
        pencere.destroy()
        
        
pencere = tk.Tk()  # pencere nesnesini oluşturuyoruz
pencere.title("Tkinter Dersine Hoş Geldiniz")  # pencere başlığı eklenir
pencere.iconbitmap("mainicon.ico")
pencere.geometry("800x600+400+100") # pencere boyut ayarlama

pencere.maxsize(1000,800) # olabilecek en yüksek boyut
pencere.minsize(500,300)  # olabilecek en düşük boyut
pencere.configure(bg="aqua")
pencere.resizable(False, False)

label = tk.Label(pencere, text="Burası İlk Etiket Bölümü", bg="red", font="Times 20 bold")
label.place(x=20, y=20)
metin = tk.Entry(pencere, border=2)
metin.place(x=350, y=20)

labelAdi = tk.Label(pencere, text="Ad Soyad", bg="maroon", fg="white")
labelAdi.place(x=20, y=60)
metinAdi = tk.Entry(pencere, border=2)
metinAdi.place(x=200, y=60)

labelAdi = tk.Label(pencere, text="Parola")
labelAdi.place(x=20, y=90)
metinAdi = tk.Entry(pencere, cursor="watch", show="*")
metinAdi.place(x=200, y=90)

btnGiris = tk.Button(pencere, text="Giriş", command=mesaj)
btnGiris.place(x=150, y=120, width=120, height=50)

btnCikis = tk.Button(pencere, text="Çıkış", command=cikis)
btnCikis.place(x=300, y=120, width=120, height=50)


canvas = tk.Canvas(pencere, bg="yellow")
canvas.place(x=400, y=500, width=100, height=100)

benimFontum = ("Comic Sans MS", "20", "italic bold underline")
labelFont= tk.Label(pencere, text="Yazı Karakteri Farklı", font=benimFontum, bg="aqua")
labelFont.place(x=120, y=200)


pencere.mainloop() # Pencerenin ekranda sürekli açık kalmasını sağlar