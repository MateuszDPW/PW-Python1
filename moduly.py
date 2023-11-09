# # import math
# # print(math.sqrt(10))
# # from math import sqrt
# # print(sqrt(10))

# #generowanie losowej liczby 1-100
# import random
# print(random.randint(1,100))

# #wybor losowego elementu z listy
# fruits = ["apple", "banana", "orange"]
# print(random.choice(fruits))

# #mieszanie listy
# numbers=[1,2,3,4,5]
# random.shuffle(numbers)
# print(numbers)

# #zwrocenie czasu
# import time
# print(time.time())

# #zwrocenie biezacej daty i godziny
import datetime
# now = datetime.datetime.now()
# print(now)

# #napisz program ktory sprawdza czy dany format daty jest prawidlowy
# # 'dd-mm-yyyy'

todays_date = datetime.date.today()

print(todays_date)

#1 stycznia 1970 - UTC
print(datetime.date.fromtimestamp(10))
print(datetime.date.fromtimestamp(10).year)

a = datetime.time(11,34,56)
print(a.minute)
a = datetime.time(11,34,56).hour
print(a)

now = datetime.datetime.now()
s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print(s1)

# #napisz kod ktory wypisze liste wszystkich plikow w biezacym katalogu
# import os
# for file in os.listdir():
#     print(file)


# file_path = "request.py"
# if os.path.exists(file_path):
#     print("file already exists")

# print(os.path.isfile(file_path))

# print(os.listdir("test"))

# os.rename(file_path, file_path+"nowy_plik.txt")

# os.mkdir("nowy_katalog")
# os.rmdir("nowy_katalog")

# with open("nowy_plik.txt", "w") as f:
#     f.write("To jest nowy plik.")


