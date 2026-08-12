from abc import ABC, abstractclassmethod

class Animal(ABC):
    @abstractclassmethod
    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        print("Raor !!")


lion = Lion()
lion.make_sound()