print("Firilag Eeden Her Bir Sagirdin Testi Legv Olunacaq!")
print("Ugurlar")
sual="""
 1. Dunyanin en uzun çayı hansidir?
  A) Lena çayı
  B) Mississippi çayı
  C) Nil çayı
  D) Amazon çayı
 """

print(sual)
cavab=input("Cavabinizi Daxil Edin: ")
if cavab== "D":
    print("Tebrikler Siz Suala Duzgun Cavab Verdiniz.")
else:
    print("Cavabiniz Duzgun Deyil.")


sual="""
 2.Bir akvariumda 10 balıq var. 2 si boğuldu. 4ü üzür. 3 ü isə öldü. Akvariumda neçə balıq qalır??
  A) 5
  B) 0
  C) 10
  D) 4
 """

print(sual)
cavab=input("Cavabinizi Daxil Edin: ")
if cavab== "C":
    print("Tebrikler Siz Suala Duzgun Cavab Verdiniz.")
else:
    print("Cavabiniz Duzgun Deyil.") 
    
    
sual="""
 3.Bunlardan hansi materik deyil? 
  A) Avstraliya
  B) Avrasiya
  C) Afrika
  D) Hamisi
 """

print(sual)
cavab=input("Cavabinizi Daxil Edin: ")
if cavab== "D":
    print("Tebrikler Siz Suala Duzgun Cavab Verdiniz.")
else:
    print("Cavabiniz Duzgun Deyil.")
    
sual="""
 4.Nufusuna gore ilk hansi ölkedi?
  A) Çin
  B) ABD
  C) Hindistan
  D) Rusiya
 """

print(sual)
cavab=input("Cavabinizi Daxil Edin: ")
if cavab== "A":
    print("Tebrikler Siz Suala Duzgun Cavab Verdiniz.")
else:
    print("Cavabiniz Duzgun Deyil.")
        
duz_sayi =  int(input("Dogru Sayizi Qeyd Edin:"))
if duz_sayi   <=1:
    print("Cox Pis Netice")
if duz_sayi <=2 :
    print("Pis Netice") 
if duz_sayi  <=3 :
    print("Orta Netice")
if duz_sayi  <=4 :
    print("Ela Netice")