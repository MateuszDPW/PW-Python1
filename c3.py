#program wyswietlacy napis

print("Hello World")

#program proszacy o wpisanie czegos zeby sie wyswietlilo w zdaniu

imie = input("Podaj swoje imię ")
nazwisko = "Kowalski"
print("Witaj, ", imie)
print(f"Witaj, {imie}")
print("Witaj, {}!".format(imie))
print("Witaj, {1} {0}!".format(imie, nazwisko))

#Zadeklaruj dwie zmienne liczbowe i wykonaj podstawowe działania matematyczne
#wypisz wyniki na ekranie

a = 10
b = 4
suma = a + b
roznica =a - b
iloczyn = a * b
iloraz = a / b

print("Suma: ", suma )
print("Różnica: ", roznica )
print("Iloczyn: ", iloczyn )
print("Iloraz: ", iloraz )

#obliczanie sredniej
#popros o podanie trzech liczb calkowitych, oblicz ich arytmetyczna i podaj wynik

num1 = int(input("Podaj pierwszą liczbę: "))
num2 = int(input("Podaj drugą liczbę: "))
num3 = int(input("Podaj trzecią liczbę: "))

wynik = (num1 + num2 + num3)/3

print("Wynik działania arytmetycznego wynosi: ", wynik)

#zadeklaruj zmienną zawierającą dowolny tekst i użyj operatora indeksowania, aby wupisac pierwszą i ostatnią literę tego tekstu

text = "Python"
first = text[0]
last = text[-1]
print("Pierwsza litera: ", first, ", ostatnia litera: ", last)

#zmiana liter w tekscie
#zadeklaruj zmienna tekstem i zamien wszystkie litery na male litery. Nastepnie wypisz powstaly tekst

text = "PytHon jEst SUPer!"
print(text)
text = text.lower()
print(text)

#liczenie znaków w tekscie
#popros o podanie tekstu, oblicz i wypisz liczbe znakow w tym tekscie (spacje tez)

text = input("Wpisz jakieś zdanie: ")
text = len(text)
print("Liczba znaków w tym tekscie wynosi: ", text)

#zamiana w tekscie za pomoca replace
#zadeklaruj zmienna z tekstem, zamien wszystkie lotery "a" na "x". wypsiz zmodyfikowany tekst

text = "Przykladowy tekst z litera a"
print(text)
text = text.replace("a","x")
print(text)

#podzial tekstu na slowa
#zadeklaruj zmienna zawieajaca zdanie. Nastepnie powiel to zdanie na słowa i wypisz je jako liste

text = "To jest przykład dowolnego zdania do podziału."
text1 = text.split()
print(text1)

#uzycie strip

text = "     To jest przykład nadmiaru białych znaków.     "
text1 = text.strip()
print(text1)

#uzycie join

text = " ".join(text1)
print(text)

#uzycie capitalize

text = "przykladowe zdanie."
text = text.capitalize()
print(text)

#zliczenie ilosci danego znaku z pomoca count

count_a = text.count("a")
print(count_a)

#odwrocenie slowa

text = "python"
text = text[::-1]
print(text)

#odwrocenie slowa bez pierwszej litery

text = text[:-1]
print(text)

#odwrocenie slowa bez pierwszych dwoch liter

text = text[0:-1]
print(text)