import sqlite3
from tkinter import *

sayfa=Tk()
sayfa.title("DB Input")
sayfa.geometry("800x400")

baglanti=sqlite3.connect("tkinter.db")
cursor=baglanti.cursor()

def tablo_olustur():
	cursor.execute("CREATE TABLE IF NOT EXISTS Library (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)")
	baglanti.commit()
#tablo_olustur()
def veri_ekle3():
	isim=isimGirisi.get()
	yazar=yazarGirisi.get()
	yayınevi=yayıneviGirisi.get()
	sayfa_sayisi=sayfaGirisi.get()
	cursor.execute("Insert Into Library Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayisi))
	baglanti.commit()
#veri_ekle3()

isim=Label(sayfa,text="isim giriniz:",font=("Arial",10))
isim.grid(row=0,column=0)
isim=Label(sayfa,text="yazar isimi giriniz:",font=("Arial",10))
isim.grid(row=1,column=0)
isim=Label(sayfa,text="yayın giriniz:",font=("Arial",10))
isim.grid(row=2,column=0)
isim=Label(sayfa,text="sayfa sayısı giriniz:",font=("Arial",10))
isim.grid(row=3,column=0)

isimGirisi=Entry(sayfa,width=50,font=("Arial",10))
isimGirisi.grid(row=0,column=1)
isimGirisi.insert(0,"")

yazarGirisi=Entry(sayfa,width=50,font=("Arial",10))
yazarGirisi.grid(row=1,column=1)
yazarGirisi.insert(0,"")

yayıneviGirisi=Entry(sayfa,width=50,font=("Arial",10))
yayıneviGirisi.grid(row=2,column=1)
yayıneviGirisi.insert(0,"")

sayfaGirisi=Entry(sayfa,width=50,font=("Arial",10))
sayfaGirisi.grid(row=3,column=1)
sayfaGirisi.insert(0,"")

buton=Button(sayfa,text="Tablo Olustur",command=tablo_olustur,font=("Arial",10))
buton.grid(row=4,column=1)
buton=Button(sayfa,text="Verileri VeriTabanına Yaz",command=veri_ekle3,font=("Arial",10))
buton.grid(row=5,column=1)
sayfa.mainloop()