# make sub-program to simulate  Coffee Machine taking an order
# Create (take_order)
# Helen's version
#20th of October 2026

from enum import Enum


class CoffeeType(Enum):
    BLACK = "Black Coffee"
    ESPRESSO = "Espresso Coffee"
    LATTE = "Cafe Latte"
    CHOC = "Hot Chocolate"

class CoffeeSize(Enum):
    S = "Small"
    M = "Medium"
    L = "Large"

class CoffeeCream(Enum):
    YES = "With Cream"
    NO = "Without Cream"


class Coffee:
    def __init__(self, name, time, coffee_type, size, cream):
        self.__name = name
        self.__time = time
        self.__coffee_type = coffee_type
        self.__size = size
        self.__cream = cream

    def get_name(self):
        return self.__name

    def get_time(self):
        return self.__time.strftime("%d-%m-%Y %H:%M")
       # return self.__time

    def get_coffee_type(self):
        return self.__coffee_type

    def get_size(self):
        return self.__size

    def get_cream(self):
        return self.__cream


