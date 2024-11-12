from copy import deepcopy

class Warrior:
    def __init__(self, name):
        self.name = name

    def clone(self):
        return deepcopy(self)
    
warrior_1 = Warrior("Max")

warrior2 = warrior_1.clone()
warrior2.name = "Ryan"

print(warrior_1.name, warrior2.name)
