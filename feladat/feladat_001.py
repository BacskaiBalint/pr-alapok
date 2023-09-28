# feladat_001
"""
Kérjük be a billentyűzetről a nevünket, és írassuk ki a képernyőnkre!
A billentyűzetről mindig a szöveget (string-et) olvasunk be!
type(változó)
"""
'''
nev = input("Kérek egy nevet: ")
print(f"A megadott név a következő: {nev}")
'''


vnev = input("Kérek egy vezetéknevet: ")
knev = input("Kérek egy keresztnevet: ")
print(f"A megadott név a következő: {vnev} {knev}")




print(f"A vnev változó típusa: {type(vnev)}")
print(f"A knev változó típusa: {type(knev)}")