import sqlite3
baglanti =sqlite3.connect("kütüphane.db")
cursor= baglanti.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Library (isim TEXT, kategori TEXT, yayınevi TEXT, Sayfa_sayisi INT)")
    baglanti.commit()#her cursor işleminden sonra gönderme yapmak için commit yaparız zaman damgasıyla gönderir
tablo_olustur()
baglanti.close()