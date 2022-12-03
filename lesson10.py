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
#veri_ekle()
def veri_ekle2(isim,yazar,yayınevi,sayfa_sayisi):
	cursor.execute("Insert Into Library Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayisi))
	baglanti.commit()
#veri_ekle2("Araba Sevdası","Recaizade Mahmud Ekrem","ALFA Basım",365)
def veri_ekle3():
	isim=input("Kitap ismi:")
	yazar=input("Yazarı:")
	yayınevi=input("Yayınevi:")
	sayfa_sayisi=input("Sayfa sayısı:")
	cursor.execute("Insert Into Library Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayisi))
	baglanti.commit()
#veri_ekle3()
def verileri_al():
	cursor.execute("Select * from Library")
	liste=cursor.fetchall()
	#print(liste)
	print("Mevcut Kütüphanedeki Kitap Bilgileri")
	for i in liste:
		print(i)

#verileri_al()

def verileri_al2():
	cursor.execute("Select İsim, Yazar from Library")
	liste= cursor.fetchall()
	for i in liste:
		print(i)
#verileri_al2()

def verileri_al3(yayınevi):
	cursor.execute("select * from Library where Yayınevi=?",(yayınevi,))
	liste= cursor.fetchall()
	for i in liste:
		print(i)
#verileri_al3("Anka")
def verileri_al4(yazar):
	cursor.execute("select Yayınevi, Sayfa_Sayısı from Library where yazar=?",(yazar,))
	liste= cursor.fetchall()
	for i in liste:
		print("Kitabın yayınevi: {} ve sayfa sayısı:{}".format(i[0],i[1]))

#verileri_al4("Mehmet Akif Ersoy")
def verileri_guncelle(eski_yayınevi,yeni_yayınevi):
	cursor.execute("UPDATE Library SET Yayınevi=? WHERE Yayınevi=?",(yeni_yayınevi,eski_yayınevi,))
	baglanti.commit
#verileri_guncelle("alfa","ALFA BASIM")
def verileri_sil(yazar):
	cursor.execute("delete from library where Yazar=?",(yazar,))
verileri_al()
verileri_sil("mahmut")
baglanti.close()