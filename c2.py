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
#print(owoce.pop("banan"))
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

#klucz, wartosc = owoce.popitem("banan")

#slowniki

slownik1 = {'a': 1, 'b': 2}
slownik2 = {'b': 3, 'c': 4}

slownik1.update(slownik2)
#slownik1 = {'a':1, 'b':3, 'c':4}

slownik1 = {'a': 1, 'b':2}
slownik2 = slownik1.copy()
print(slownik2)



lista = [1,2,3]
print(lista)
print(lista[0])
lista.append(4)
print(lista)
lista.extend([5,6,7])
print(lista)
lista.insert(3,0)
print(lista)
lista.insert(4, "cos")
print(lista)
lista.insert(6, "cos")
print(lista)
lista.remove("cos")
lista.remove("cos")
print(lista)
lista.pop(4)
print(lista)
lista.reverse()
print(lista)
lista.sort()
print(lista)
#lista.count()
#print(lista)
