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
print(owoce["banan"])