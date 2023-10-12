# Bacskai Balint 10.D 1.csoport
# szamonkeres001.py
"""
Bekerek egy osztalyzatot 1-5 irassuk ki a megadott jegyet ertekkel es szovegesen
Ha nem megfelelo jegyet adtam akkor irassuk ki a jegy erteket es melle azt a szoveget,
hogy nem megfelelo jegy
"""
jegy = input("Kerek egy osztalyzatot 1-5 kozott: ")
jegy = int(jegy)
if jegy == 5:
    print(f"Az ertekelesed {jegy} jeles")
elif jegy == 4:
    print(f"Az ertekelesed {jegy} jo")
elif jegy == 3:
    print(f"Az ertekelesed {jegy} kozepes")
elif jegy == 2:
    print(f"Az ertekelesed {jegy} elegseges")
elif jegy == 1:
    print(f"Az ertekelesed {jegy} elegtelen")
else:
    print(f"Az ertekelesed {jegy} ami nem megfelelo")