import sqlite3
baglanti=sqlite3.connect("kütüphane.db")
cursor=baglanti.cursor()

def tablo_olustur():
	cursor.execute("CREATE TABLE IF NOT EXISTS Library (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)")
	baglanti.commit()
#tablo_olustur()
def veri_ekle():
	cursor.execute("Insert Into Library Values('Safahat','Mehmet Akif Ersoy','Anka',644)")
	baglanti.commit()
def veri_ekle2(İsim,Yazar,Yayınevi,Sayfa_Say):
	cursor.execute("Insert Into Library Values(?,?,?,?)",(İsim,Yazar,Yayınevi,Sayfa_Say))
	baglanti.commit()
#veri_ekle()
isim = input("Lütfen Kitap İsimi Giriniz= ")
yazar = input("Lütfen Yazar İsimi Giriniz= ")
yayınevi = input("Lütfen Yayınevi İsimi Giriniz= ")
sayfa_say = input("Lütfen Sayfa Sayısı Giriniz= ")
veri_ekle2(isim,yazar,yayınevi,sayfa_say)

baglanti.close()