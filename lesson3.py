import sqlite3
baglanti=sqlite3.connect("kütüphane.db")
cursor=baglanti.cursor()

def tablo_olustur():
	cursor.execute("CREATE TABLE IF NOT EXISTS Library (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)")
	baglanti.commit()
tablo_olustur()
def veri_ekle():
	cursor.execute("Insert Into Library Values('Safahat','Mehmet Akif Ersoy','Anka',644)")
	baglanti.commit()
veri_ekle()
baglanti.close()