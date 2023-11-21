# #Zad1: napisz funkcje ktora obliczy sume cyfr liczby całkowitej
# def add(num1: int):
#     add = 0
#     while num1 > 0:
#         add += num1 % 10 #cyfra jednosci
#         num1 //= 10
#     return add

# try:
#     num1 = input('Enter a number: ')
#     if num1.isdigit():
#         print(f"Suma cyfr liczby {num1} wynosi: ", add(num1))
#     else:
#         print("Please enter only digits.")
# except ValueError:
#     print("Please provide olny digits.")

#Zad 2: napisz program obliczajacy wskaznik masy ciala BMI na podstawie wzrostu i wagi uzytkownika
# bmi = waga / (wzrost ** 2)
# 18.5 > niedowaga
# 18.5 - 24.9 prawidlowa waga
# 25-29.9 nadwaga
# >30 otylosc
def check_float(number) -> bool:
    try:
        float(number)
        return True
    except ValueError:
        return False

def oblicz_bmi(weight: float, height: int) -> str:
    bmi = weight / (height ** 2)
    return interpretuj_BMI(bmi)

def interpretuj_BMI(bmi: float) -> str:
    if 25 <= bmi and bmi < 30:
        return "Otylosc"
    elif bmi <= 18.5:
        return "Niedowaga"
    elif 18.5 < bmi and bmi < 25:
        return "Prawidlowa waga"
    else:
        return "Nadwaga"
try:
    weight = input("Enter your weight: ")
    height = input("Enter your height: ")