#if else czy jest wieksze od 10

liczba = int(input("podaj liczbe"))
if liczba > 10:
    print("liczba jest wieksza od 10")
else:
    print("liczba nie jest wieksza od 10")

#elif
#popros o podanie wieku i wydrukuj wiadomosc na podstawie wieku: "Młodzież", "Dziecko", "Dorosły"

wiek = int(input("Podaj wiek"))

if wiek >= 18:
    print("Dorosły")
elif wiek < 10:
    print("Dziecko")
else:
    print("Młodzież")

#Sprawdzenie wartosci prawdziwej/falszywej
#zadeklaruj zmienna warunek o wartości True i napisz instrukcje warunkową która wypisze Prawda lub Fałsz na podstawie wartości tej zmiennej

warunek = True

if warunek:
    print("prawda")
else:
    print("fałsz")

#sprawdzenie czy liczba jest parzysta
#popros o licz całk i sprawdz czy jest ona parzysta

liczba = int(input("Podaj liczbe"))

if liczba % 2 == 0:
    print("Liczba jest parzysta")
else:
    print("Liczba jest nieparzysta")

#operator logiczny AND
#popros o podanie swojego wieku i informacji czy ma prawo jazdy. nastepnie sprawdz, czy użytkownik jest pełnoletni i ma prawo jazdy

wiek = int(input("Podaj swój wiek"))
prawoJazdy = input("Czy masz prawo jazdy (TAK/NIE)?").lower()

if wiek >=18 and prawoJazdy == "tak":
    print("Jesteś pełnoletni i masz prawo jazdy")
else:
    print("Nie jesteś pełnoletni lub nie masz prawa jazdy")

    #sprawdzenie przynaleznosci do zakresu
    #popros o podanie liczby i sprawdz czy nalezy ona do zakresu od 10 do 50

    num = int(input("Podaj liczbe: "))

#if 10<= liczba <= 50:
#zakres = (10,51)
#if num in zakres[0]:
#if liczba >=zakres[0] and liczba <=zakres[1]:

    if num in range(10, 51):
        print("Liczba nalezy do zakresu")
    else:
        print("Liczba jest poza zakresem")

