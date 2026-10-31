class Hero:

    # Constructor: Run when the hero is created
    def __init__(self, name, hp, attack_power):
        self.name = name # Hero Name
        self.hp = hp # Health Point
        self.attack_power = attack_power # Attack Power
    # Info Display Hero
    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")

    # Attack Method: This object (self) attacks another object (enemy)
    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name}!")
        enemy.attacked(self.attack_power)
    
    # Attacked Method: Receives damage
    def attacked(self, dmg):
        self.hp -= dmg
        print(f"{self.name} gets hit by {dmg} dmg! HP left: {self.hp}")

# -- Main Program --
# Instantiate Objects
Hero1 = Hero("Layla", 100, 15)
Hero2 = Hero("Zilong", 120, 20)

# Calling Methods
Hero1.info()
Hero2.info()

print("\n--- Battle Begins ---")
Hero1.attack(Hero2)
Hero2.attack(Hero1)
