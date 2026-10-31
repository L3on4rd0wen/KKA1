from abc import ABC, abstractmethod

# 1. Interface / Abstract Class
class GameUnit(ABC):
    @abstractmethod
    def attack(self, target):
        pass
    
    @abstractmethod
    def info(self):
        pass

# 2. Implement Concrete Classes
class Hero(GameUnit):
    def __init__(self, name):
        self.name = name

    def attack(self, target):
        print(f"Hero {self.nama} slash {target}!")

    def info(self):
        print(f"I'm a Hero: {self.name}")

class Monster(GameUnit):

    def __init__(self, jenis):
        self.jenis = jenis

    def attack(self, target):
        print(f"Monster {self.jenis} bites {target}!")

    def info(self):
        print(f"I'm a Monster: {self.jenis}")

# -- Try --
unit = GameUnit()

h = Hero("Alucard")
m = Monster("Wolf")
h.info()
m.info()