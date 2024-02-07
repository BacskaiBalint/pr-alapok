'''
A SZÉLSŐÉRTÉK MEGHATÁROZÁSA esetében azt vizsgáljuk, hogy melyik a legkisebb,
illetve a legnagyobb érték az adatsorban (itt a listában).
'''
lista = [12, 5, 4, 8, 9, 11, 10, 15, 6]

min = lista[0]
max = lista[0]
for szam in lista:
    if szam < min:
        min = szam
    if szam > max:
        max = szam

print(f"A legkisebb szám a listában: {min}")
print(f"A legnagyobb szám a listában: {max}")

# ---------------------------------------------

# Alakítsd át a programot függvénnyé!

lista = [12, 5, 3, 8, 9, 11, 10, 16, 6]

def maximum(list):
    max1 = list[0]
    for szam in list:
        if szam > max1:
            max1 = szam
    return max1

print(f"A lista legnagyobb eleme: {maximum(lista)}")

#-----------------------------------------------

# minimum függvény
lista = [12, 5, 3, 8, 9, 11, 10, 16, 6]

def minimum(list):
    min1 = list[0]
    for szam in list:
        if szam < min1:
            min1 = szam
    return min1

print(f"A lista legkisebb eleme: {minimum(lista)}")

# ---------------------------------------------
# A lista legnagyobb és legkisebb eleme közötti különbség!
lista = [12, 5, 3, 8, 9, 11, 10, 16, 6]
print(f"A lista különbség: {maximum(lista) - minimum(lista)}")

lista3 = [12, 5, 2, 8, 9, 11, 10, 16, 6]
print(f"A lista_max és a lista3_min különbség: {maximum(lista) - minimum(lista3)}")

#osszeg függvény
lista5 = [12, 5, 2, 8, 9, 11, 10, 16, 6]
def osszeg(list):
    szumma = 0
    for szam in list:
        szumma = szumma + szam
    return szumma

print(f"A lista5 lista elemeinek összege: {osszeg(lista5)}")