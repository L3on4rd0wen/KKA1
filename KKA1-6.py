# Parent Class
class Hero:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print("Hero attacks with bare hands.")

# Child Class 1
class Mage(Hero):
    def attack(self):
        print(f"{self.name} (Mage) casts a Fireball! Boom!")

# Child Class 2
class Archer(Hero):
    def attack(self):
        print(f"{self.name} (Archer) shoots an arrow from afar! Pew!")

# Child Class 3
class Fighter(Hero):
    def attack(self):
        print(f"{self.name} (Fighter) slashes with a sword! Slash!")

class Healer(Hero):
    def attack(self):
        print(f"{self.name} (Healer) heals with prayer! *Holy Intensifies*")

# -- Applying Polymorphism --
# We have a mixed list of heroes
army = [
    Mage("Eudora"),
    Archer("Miya"),
    Fighter("Zilong"),
    Mage("Gord"),
    Healer("Ralsei")
]

print("--- WAR HAS BEGUN ---")
# A single loop command, but with different responses (Polymorphism)
for hero in army:
    hero.attack()