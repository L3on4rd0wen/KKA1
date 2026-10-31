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

# Mage Class child of The Hero Class
class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
    # Call the parent's (Hero) constructor
        super().__init__(name, hp, attack_power)
        self.mana = mana
    
    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")
    
    # Unique Mage Skill
    def skill_fireball(self, enemy):
        if self.mana >= 20:
            print(f"{self.name} casts Fireball to {enemy.name}!")
            self.mana -= 20
            enemy.attacked(self.attack_power * 2) # Double Damage
        else:
            print(f"{self.name} failed to cast! Not enough Mana.")

# -- Main Program --
# Instantiate Objects
Layla = Hero("Layla", 100, 15)
Zilong = Hero("Zilong", 120, 20)
Eudora = Mage("Eudora", 80, 30, 100)
Balmond = Hero("Balmond", 200, 10)

# Calling Methods
Layla.info()
Zilong.info()
Eudora.info()
Balmond.info()

print("\n--- Battle Begins ---")

print("\n\n--- Fight 1 ---")
Layla.attack(Zilong)
Zilong.attack(Layla)

print("\n\n--- Fight 2 ---")
Eudora.attack(Balmond)
Eudora.skill_fireball(Balmond)