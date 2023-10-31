#stworz slownik gdzie kluczami beda nazwy owocow a wartosciami ich kolory

owoce = {
    "jablko":"czerwony",
    "banan":"zolty"
}   #klucz:wartosc

for kolor in owoce.values():
    print(kolor)


print(owoce)
print(owoce["banan"])
print(owoce.keys())
print(owoce.values())
print(owoce.items())
print(owoce.clear())
print(owoce.pop("banan"))
print(owoce.get("banan",0))
owoc = input("podaj nazwe owoca: ")
for owoc in owoce.items():
    if owoc == owoce.get(owoc,0) != 0:
        print("jest w koszyku")
    else:
        print("brak")

zbiorLiter= {}
litera = input("podaj litere: ")
if owoce.get(litera,0) != 0:
    owoce.pop(litera)
else:
    print("brak")
