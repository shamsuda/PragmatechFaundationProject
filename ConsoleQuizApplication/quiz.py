from ast import If


sual="""
 1. 4+5=?
  A)6
  B)7
  C)8
  D)9
 """

print(sual)

cavab=input("Cavabinizi Daxil Edin: ")

if cavab== "D":
    print("Tebrikler Siz Suala Duzgun Cavab Verdiniz.")
else:
    print("Cavabiniz Duzgun Deyil.")