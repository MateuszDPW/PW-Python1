####1####

# class ParentClass:
#     def speak(self):
#         print("Jestem rodzicem")

# class ChildClass(ParentClass):
#     def speak(self):
#         super().speak()
#         print("Jestem dzieckiem")

# child = ChildClass()
# child.speak()

####2####

# def area(shape):
#     return shape.calculate_area()

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         return 3.14 * (self.radius ** 2)

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     def calculate_area(self):
#         return self.width * self.height
    
# circle = Circle(5)
# rectangle = Rectangle(4,3)
# print(f"Pole koła to {area(circle)}")
# print("Pole koła", area(circle))
# print(f"Pole prostokąta to {area(rectangle)}")
# print("Pole prostokąta", area(rectangle))

####3####

# class Animal:
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return "Woof! Bark!"
# class Cat(Animal):
#     def speak(self):
#         return "Meow! Meow!"

# def make_animal_speak(animal):
#     return animal.speak()
    
# dog = Dog()
# cat = Cat()

# print(make_animal_speak(dog))
# print(make_animal_speak(cat))

####4####
#klasy abstrakcyjne#

# def area(shape):
#     return shape.calculate_area()

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         return 3.14 * (self.radius ** 2)

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     def calculate_area(self):
#         return self.width * self.height
    
# circle = Circle(5)
# rectangle = Rectangle(4,3)
# print("Pole koła", circle.calculate_area())
# print("Pole prostokąta", rectangle.calculate_area())

####5####

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f"{self.name}, {self.age} lat"

person = Person("Alicja", 33)
print(str(person))



