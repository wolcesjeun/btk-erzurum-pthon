import sqlite3
baglanti =sqlite3.connect("kütüphane.db")
cursor= baglanti.cursor()
baglanti.close()