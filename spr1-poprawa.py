# Napisz program w Pythonie, który będzie obsługiwał dane o działkach rolnych. Program powinien umożliwić:
# Przechowywanie informacji o wielkości każdej działki( długość i szerokość) oraz o nazwie właściciela (rolnika)
# Obliczanie powierzchni każdej działki
# Zapisywanie danych o działkach do pliku w formacie: nazwa_rolnika; dlugoscXszerokosc, dlugoscXszerokosc, ...
# Odczytywanie i wyświetlanie informacji o działkach z pliku, w tym łącznej powierzchni działek danego rolnika

filename = "dzialki.txt"

#oblicza powierzchnie dzialki
def oblicz_powierzchnie(dlugosc, szerokosc):
    return dlugosc * szerokosc

#zapisuje do pliku dzialke w formacie: nazwa_rolnika; dlugoscXszerokosc
def zapisz_do_pliku(dzialki, filename):
    with open(filename, 'w') as file:
        for dzialka in dzialki:
            file.write(f"{dzialka['nazwa_rolnika']}; {dzialka['dlugosc']}X{dzialka['szerokosc']}, ")

#odczytuje dane z pliku
def odczytaj_z_pliku(filename):
    with open(filename, 'r') as file:
        dane = file.read().split(', ')
        dzialki = []
        for element in dane:
            if element:
                nazwa, wymiary = element.split('; ')
                dlugosc, szerokosc = map(int, wymiary.split('X'))
                dzialki.append({'nazwa_rolnika': nazwa, 'dlugosc': dlugosc, 'szerokosc': szerokosc})
        return dzialki

#wyswietla informacje o dzialce
def wyswietl_informacje(dzialki):
    for dzialka in dzialki:
        print(f"Działka: {dzialka['nazwa_rolnika']}; {dzialka['dlugosc']}X{dzialka['szerokosc']}, "
              f"Powierzchnia: {oblicz_powierzchnie(dzialka['dlugosc'], dzialka['szerokosc'])}")

#wyswietla sume powierzchni dzialek
def laczna_powierzchnia_rolnika(dzialki, nazwa_rolnika):
    powierzchnia = sum(oblicz_powierzchnie(dzialka['dlugosc'], dzialka['szerokosc'])
                       for dzialka in dzialki if dzialka['nazwa_rolnika'] == nazwa_rolnika)
    print(f"Łączna powierzchnia działek rolnika {nazwa_rolnika}: {powierzchnia}")


# Przykład użycia:
dzialki = [
    {'nazwa_rolnika': 'Rolnik1', 'dlugosc': 20, 'szerokosc': 30},
    {'nazwa_rolnika': 'Rolnik2', 'dlugosc': 15, 'szerokosc': 25},
]

zapisz_do_pliku(dzialki, "dzialki.txt")
wczytane_dzialki = odczytaj_z_pliku("dzialki.txt")

wyswietl_informacje(wczytane_dzialki)

laczna_powierzchnia_rolnika(wczytane_dzialki, "Rolnik1")