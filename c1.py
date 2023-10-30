#podaj liczbe i sprawdz czy jest większa od 10

number = int(input("Podaj liczbe: "))

if(number > 10):
    print("Liczba jest większa od 10")
else:
    print("Podana liczba jest mniejsza lub równa 10")

# popros o wiek, sprawdz czy jest to dziecko, mlodziez lub dorosly

age = int(input("Podaj swój wiek: "))

if(age <10):
    print("Jesteś dzieckiem")
elif(age <18):
    print("Jesteś młodzieżą")
else:
    print("Jesteś dorosły")

#sprawdzenie warunku true/false

warunek = False

if warunek:
    print("Warunek prawdziwy")
else:
    print("Warunek fałszywy")

#liczba parzysta

num = int(input("Wpisz liczbę"))

if(num %2 == 0):
    print("Liczba jest parzysta")
else:
    print("Liczba jest nieparzysta")

#and, sprawdzenie 2 warunkow

age = int(input("Podaj wiek: "))
prawo_jazdy = int(input("Czy masz prawo jazdy?(1/0)"))

if(age >= 18 and prawo_jazdy.lower == 1):
    print("Jesteś pełnoletni i masz prawo jazdy")
else:
    print("Jesteś niepełnoletni lub nie masz prawa jazdy")
