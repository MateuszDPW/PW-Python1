# #Zadanie 1:
# #Napisz funkcję powitanie, która nie przyjmuje żadnych argumentów i wypisuje "Witaj w świecie Pythona!".

# print("Witaj w świecie Pythona!")

# #Zadanie 2:
# #Zmodyfikuj funkcję powitanie tak, aby przyjmowała jeden argument imie i wypisywała personalizowanie powitanie.

# def powitanie (imie):
#     print(f"Witaj, {imie}, w świecie Pythona!")


# #Zadanie 3
# #Napisz funkcje max_min, która przyjmuje trzy argumenty i zwraca wartość maksymalną oraz minimalną.

# def max_min(a,b,c):
#     return max(a,b,c), min(a,b,c)

# print(max_min(1,2,3))

# #Zadanie 4
# #Stwórz funkcję dlugosc_ciagu, która przyjmuje string i zwraca liczbę znaków w tym stringu.

# def dlugosc_ciagu (zdanie):
#     return len(zdanie)

# print(dlugosc_ciagu("Python"))

# #Zadanie 5
# #Napisz funkcję silnia, która oblicza silnię danej liczby.

# def silnia(n):
#     if n==0:
#         return 1
#     else:
#         return n*silnia(n-1)

# print(silnia(5))

# #Zadanie 6
# #Napisz funkcję z adnotacją typów, która sumuje dwie liczby całkowite

# def adnotacja(a: int, b:int) ->int:
#     return a*b

# print(adnotacja(2,3))

# #Zadanie 7: wykonywanie prostej prośby GET

# import requests

# response = requests.get('https://www.google.com')

# print(response.status_code)

# #Zadanie 8: Walidacja adresu e-mail
#     #czy istnieje @
#     #walidacja pustych znaków
#     #user ma 6-30 znaków
#     #domena to pw.edu.pl

# def walidacja_email(email):

#     if email.count('@') !=1:
#         raise ValueError("To nie jest adres mailowy")
 
#     #podział adresu na username i domenę
#     parametr = email.split('@')

#     if parametr[1] != 'pw.edu.pl':

#         raise ValueError("Domena jest poza PW")
  

#     print(parametr[1])

#     print(email.count('@'))

#     try:
#         walidacja_email('01182344@pw.edu.pl')
#     except ValueError as e:
#         print(f"Komunikat błędu: {e}")


# #Zadanie 9
# #Napisz funkcję validate_password która sprawdza czy hasło jest wystarczająco silne. Załóżmy, że silne hasło musi mieć przynajmniej 8 znaków, w tym jedną cyfrę i jedną wielką literę

# def validate_password(password):
#     mam_cyfre = any(char.isdigit() for char in password)
#     mam_duza_litere = any(char.isupper() for char in password)
#     is_long = len(password)>=8
#     return mam_cyfre and mam_duza_litere and is_long

# haslo = input("Wprowadz haslo: ")

# if validate_password(haslo):
#     print('Mam silne haslo')
# else:
#    print('Mam slabe haslo')

# #Zadanie 10
# #napisz funkcje validate_username ktora sprawdza czy nazwa uzytkownika sklada sie wylaznie z liter i cyfr oraz czy ma od 3 do 16 znakow

# def validate_username(username):
#     return username.isalnum() and 3 <= len(username) <= 16

# nick = input("Podaj swój nickname: ")

# if validate_username(nick):
#     print("Sklada sie wylacznie z liter i cyfr i jest miedzy 3 a 16 znakow")
# else:
#     print("Coś jest nie tak")

# #Zadanie 11
# #napisz funkcje validate_ip ktora sprawdza czy podany ciag znakow jest poprawnym adresem IPv4. Adres IPv4 powiniem skladac sie z czterech sekcji z liczba 0-255 oddzielonych kropkami

# import ipaddress

# def validate_ip(ip):
#     try:
#         ip = ipaddress.ip_address(ip)
#         print("Adres IP '{ip}'  jest poprawny")
#     except ValueError:
#         print("Adres IP '{ip}'  jest niepoprawny")

# validate_ip("123.123.123.123")

# def validate_ip(ip_address):
#     parts = ip_address.split('.')
#     if len(parts) !=4:
#         return False
#     for part in parts:
#         if not part.isdigit() or not 0 <= int(part) <= 255:
#             return False
#     return True

# print(validate_ip('123.123.123.123'))
# print(validate_ip('777.123.123.123'))
# print(validate_ip('123.0.0.123'))

# #Zadanie 12
# #cos z numerem NIP
def validate_nip(nip):
    nip = '7742704378'
    weights = [6,5,7,2,3,4,5,6,7]
#sprawdzamy czy mamy 10 znakow i czy wszystkie sa cyframi
    if len(nip) != 10:
        return False
    if nip.isdigit():
        return False

    suma = 0
    for i in range(9):
        suma += int(nip[i]) * weights[i]

    if suma %11 != 10 and suma%11 != nip[9]:
        return False
    
    return True

if validate_nip('7742704378'):
    print("NIP jest ok")
else:
    print('Ferdek Kiepski')