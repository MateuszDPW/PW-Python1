#Zadanie: Pobierz aktualną datę i czas
#pip install DateTime
from datetime import datetime
from datetime import date

now = datetime.now()

print(now)

print(now.year)
print(now.strftime("%Y"))

#wyswietl aktualny miesiąc jako nazwę, np "Listopad"

print(now.strftime("%B"))

#wyświetl aktualny dzien tygodnia

print(now.strftime("%A"))

#Konwertuj napis 2023 11 15 na obiekt daty
date_object = datetime.strptime("2023-Nov-15", "%Y-%b-%d")

print(date_object)

#dodaj 5 dni do aktualnej daty
from datetime import timedelta

date_object = datetime.strptime("2023-11-15", "%Y-%m-%d")
new_date = date_object + timedelta(days=5)

print(new_date)

#odejmij 2 tygodnie od aktualnej daty
print(now - timedelta(weeks=2))
#print(now + timedelta(weeks=-2))   #dziala
#print(now - timedelta(weeks=-2))   #dziala

#wyswietl roznice w dniach miedzy 1 stycznia 2023 a dzisiaj

past_date = datetime(2023, 1, 1)

day = now - past_date
print(day.days)

#sprawdz czy rok 2024 jest rokiem przestepnym
import calendar

new_year = calendar.isleap(2024)
print(new_year)

#wyswietl numer biezacego tygodnia roku
print(now.strftime("%U"))

#zmien format daty z "2023-11-15 00:00:00" na format RFC 2822

rfc_date = datetime.strptime("2023-11-15 00:00:00", "%Y-%m-%d %H:%M:%S").strftime("%a, %d %b %Y %H:%M:%S +0000")
print(rfc_date)