from abc import ABC, abstractmethod
from copy import deepcopy

class CharacterCreator(ABC):
    @abstractmethod
    def create_character(self, name):
        pass


class WarriorCreator(CharacterCreator):
    def create_character(self, name):
        return Warrior(name)


class Character(ABC):
    @abstractmethod
    def clone(self):
        pass


class Warrior(Character):
    def __init__(self, name):
        self.name = name

    def clone(self):
        return deepcopy(self)


# Create a warrior using the creator
warrior_creator = WarriorCreator()
warrior_1 = warrior_creator.create_character("Max")

# Clone the warrior and modify the clone
warrior_2 = warrior_1.clone()
warrior_2.name = "Ryan"

print(warrior_1.name, warrior_2.name)
