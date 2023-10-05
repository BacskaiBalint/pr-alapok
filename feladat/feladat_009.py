# feladat_009
"""
Kérjünk be két egész számot, szám1 és szám2
hasonlitsuk össze a két számot, és irassuk ki, hogy
a szám1 kisebb mint a szám2, vagy a szám2 kisebb mint a szám1, vagy a szám1 egyenlő
szám2-vel.
"""
szam1 = input("Írj be egy egész számot:")
szam1 = int(szam1)
szam2 = input("Írj be még egy egész számot:")
szam2 = int(szam2)
if szam1 > szam2:
    print(f"{szam1} nagyobb mint {szam2}")
elif szam1 < szam2:
    print(f"{szam1} kisebb mint {szam2}")
elif szam1 == szam2:
    print(f"{szam1} egyenlő {szam2}-vel")
    

    