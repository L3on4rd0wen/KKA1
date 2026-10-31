class Hero:

    # Constructor: Run when the hero is created
    def __init__(self, name, hp, attack_power):
        self.name = name # Hero Name
        self.hp = hp # Health Point
        self.attack_power = attack_power # Attack Power
    # Info Display Hero
    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")

# -- Main Program --
# Instantiate Objects
Hero1 = Hero("Layla", 100, 15)
Hero2 = Hero("Zilong", 120, 20)

# Calling Methods
Hero1.info()
Hero2.info()

Hero1.hp = 500
print(Hero1.hp)
Hero1.info()