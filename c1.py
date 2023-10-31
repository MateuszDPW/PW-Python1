# #if else czy jest wieksze od 10

# liczba = int(input("podaj liczbe"))
# if liczba > 10:
#     print("liczba jest wieksza od 10")
# else:
#     print("liczba nie jest wieksza od 10")

# #elif
# #popros o podanie wieku i wydrukuj wiadomosc na podstawie wieku: "Młodzież", "Dziecko", "Dorosły"

# wiek = int(input("Podaj wiek"))

# if wiek >= 18:
#     print("Dorosły")
# elif wiek < 10:
#     print("Dziecko")
# else:
#     print("Młodzież")

# #Sprawdzenie wartosci prawdziwej/falszywej
# #zadeklaruj zmienna warunek o wartości True i napisz instrukcje warunkową która wypisze Prawda lub Fałsz na podstawie wartości tej zmiennej

# warunek = True

# if warunek:
#     print("prawda")
# else:
#     print("fałsz")

# #sprawdzenie czy liczba jest parzysta
# #popros o licz całk i sprawdz czy jest ona parzysta

# liczba = int(input("Podaj liczbe"))

# if liczba % 2 == 0:
#     print("Liczba jest parzysta")
# else:
#     print("Liczba jest nieparzysta")

# #operator logiczny AND
# #popros o podanie swojego wieku i informacji czy ma prawo jazdy. nastepnie sprawdz, czy użytkownik jest pełnoletni i ma prawo jazdy

# wiek = int(input("Podaj swój wiek"))
# prawoJazdy = input("Czy masz prawo jazdy (TAK/NIE)?").lower()

# if wiek >=18 and prawoJazdy == "tak":
#     print("Jesteś pełnoletni i masz prawo jazdy")
# else:
#     print("Nie jesteś pełnoletni lub nie masz prawa jazdy")

#     #sprawdzenie przynaleznosci do zakresu
#     #popros o podanie liczby i sprawdz czy nalezy ona do zakresu od 10 do 50

#     num = int(input("Podaj liczbe: "))

# #if 10<= liczba <= 50:
# #zakres = (10,51)
# #if num in zakres[0]:
# #if liczba >=zakres[0] and liczba <=zakres[1]:

#     if num in range(10, 51):
#         print("Liczba nalezy do zakresu")
#     else:
#         print("Liczba jest poza zakresem")

# #warunek z operatorami logicznymi
# #popros o podanie liczby i sprawdz czy jest ona podzielna przez 2 i 3 jednoczesnie

# num = int(input("Podaj liczbe: "))
# if liczba %2 == 0 and liczba %3 == 0:
#     print("liczba jest podzielna przez 2 i 3")
# else:
#     print("liczba nie jest podzielna przez 2 i 3")

# #warunek z operatorem in
# #popros o uzytkownika o podanie dnia tygodnia i sprawdz czy wprowadzona nazwa jest jednym z dni roboczych (poniedzialek-piatek)

# dniRobocze = ["poniedzialek", "wtorek", "sroda", "czwartek", "piatek"]

# dzienTygodnia = input("Podaj dzien tygodnia (bez polskich znakow): ").lower()

# if dzienTygodnia in dniRobocze:
#     print("jest to dzien roboczy")
# else:
#     print("jest to dzien weekendu")

# #napisz program ktory poprosi o slowo i sprawdzi czy slowo jest palindromem

# palindrom = input("Wpisz dowolne slowo lub zdanie: ")

# if palindrom == palindrom[::-1]:
#     print("To jest palindrom")
# else:
#     print("To nie palindrom")

#program sprawdzajacy czy podany rok jest rokiem przestepnym

rok = int(input("Podaj jakis rok: "))

if rok %4 == 0 and (rok %100 !=0 or rok %400 ==0):
    print("jest to rok przestepny")
else:
    print("nie jest to rok przestepny")