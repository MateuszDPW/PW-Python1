class Car:
  # atrybuty klasy
  kolor = "Czerwony"
  def __init__(self, make, model, year):
    #atrybuty instancji
    self.make = make
    self.model = model
    self.__year = year
  


  #zablokowanie zmiany roku samochodu
  def get__year(self):
    return self.__year
  def set__year(self, new__year):
    self.__year = new__year



car = Car("Toyota", "Camry", 2023)
print(car.kolor)
car.kolor = "Zielony"
print(car.kolor)

print(car.get__year())
car.set__year(2020)
print(car.get__year())




class Person:
  def __init__(self, name):
    self.name = name

person = Person("Jon")
person.wiek = 30    #atrybut dynamiczny
print(person.wiek)




class Circle:
  def __init___(self, radius):
    self.radius = radius
  
  def calculate(self):
    return 3.14 * self.radius**2
  
circle = Circle(10)
pole = circle.calculate()
print(pole)
circle.radius = 4
pole = circle.calculate()
print(pole)





class Kwadrat:
  width = 0
  height = 0

  def __init__(self, width, height):
    self.width = width
    self.height = height

  @classmethod
  def pole_kwadratu(cls, atrybuty):
    return cls(atrybuty, atrybuty)
  

  @staticmethod
  def obwod(a, b):
    return 2*(a+b)

def my_decorator(func):
  def wrapper():
    print("Tekst przed funkcja")
    func()
    print("Tekst po wykonaniu funkcji")
  return wrapper

@my_decorator
def czesc():
  print("Hello! world")
  
czesc()



pole = Kwadrat.pole_kwadratu(4)
print(pole.height)

print(Kwadrat.obwod(4,6))


