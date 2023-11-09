import requests


#url = f"https://api.github.com/users/{user}/repos"


# waluta_z
# waluta_na
# kwota
def przelicz(kwota: float, waluta_z: str, waluta_na: str) -> float:
    url = f"https://v6.exchangerate-api.com/v6/2f5845f3ea692b4077c36475/latest/{waluta_z}"
    response = requests.get(url)
    lista_walut = response.json()['conversion_rates']
    wynik = kwota * lista_walut[waluta_na]

    return wynik

print(przelicz(100, 'USD', 'PLN'))