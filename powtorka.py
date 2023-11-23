#Zadanie1: pobierz aktualną datę i czas
from datetime import datetime

print(datetime.now())

#Zadanie2: Wyświetl aktualny rok

print(datetime.now().year)
print(datetime.now().strftime("%Y"))

#Zadanie3: Wyświetl aktualny miesiąc jako nazwę, np: "Listopad"

print(datetime.now().strftime("%B"))

import locale
locale.setlocale(locale.LC_ALL, 'pl_PL')    #wyswietli po polsku
current_date = datetime.now()
print(current_date.strftime("%B"))

#Zadanie4: Dodaj 5 dni do aktualnej daty

from datetime import timedelta

date = datetime.now()
new_date = date + timedelta(days=5)
print(new_date)

#Zadanie5: Odejmij 2 tygodnie od aktualnej daty

new_date = date - timedelta(days=14)
print(new_date)

new_date = date - timedelta(weeks=2)
print(new_date)

#Zadanie6: Oblicz wiek osoby urodzonej w dniu "1990-05-28"

date_object = datetime(1990, 5, 28)

new_date = date - date_object
print(new_date)