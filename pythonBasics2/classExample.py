# Uses Pascal naming convention
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()
# point1.move()
#
# point2 = Point()
# point2.x = 1
# print(point2.x)

# point1 = Point(x=5, y=10)
# print(point1.x)
# point1.x = 10
# print(point1.x)

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'{self.name} is talking...')


# eric = Person('Eric')
# eric.talk()
#
# bob = Person('Bob')
# bob.talk()


# Inheritance
class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def bark(self):
        print('bark!')


class Cat(Mammal):
    def meow(self):
        print('meow!')


# dog1 = Dog()
# dog1.walk()
# dog1.bark()
#
# cat1 = Cat()
# cat1.walk()
# cat1.meow()


# # Modules
# import converter
# # This is to import select functions from module
# # Press ctrl+space after you type import to see what function are available
# from converter import kg_to_lbs
# # This statement can be called because of the select import
# # The call to the object prefix is not needed
# # without the select import you would have to type: converter.kg_to_lbs(100)
# kg_to_lbs(100)
#
# print(converter.kg_to_lbs(70))


# # More Modules
# from utils import find_max
#
# numbers = [1, 4, 10, 8, 4, 20, 2]
#
# print(find_max(numbers))


# Packages

