# feladat_17
# adatbekérés while-ciklussal (szám bekérése a megadott intervallumban)

# while szam < 5 or 10 < szam:

szam = int(input('Adj meg egy számot 5 és 10 között '))
while not 5 <= szam <= 10:
    szam = int(input('Helytelen érték! Adj meg egy számot 5 és 10 között!'))

print('Rendben!')