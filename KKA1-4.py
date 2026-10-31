class Hero:

    # Constructor: Run when the hero is created
    def __init__(self, name, hp, attack_power):
        self.name = name # Hero Name
        self.__hp = hp # Health Point
        self.attack_power = attack_power # Attack Power
    
    # Info Display Hero
    def info(self):
        print(f"Hero: {self.name} | HP: {self.get_hp()} | Power: {self.attack_power}")

    # GETTER
    def get_hp(self):
        return self.__hp
    
    # SETTER
    def set_hp(self, new_val):
        if new_val < 0:
            self.__hp = 0 # HP cannot be negative
        elif new_val > 1000:
            print("Cheat detected! HP is only capped to 1000 only.")
            self.__hp = 1000
        else:
            self.__hp = new_val

    # Attack Method: This object (self) attacks another object (enemy)
    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name}!")
        enemy.attacked(self.attack_power)
    
    # Attacked Method: Receives damage
    def attacked(self, dmg):
        self.set_hp(dmg)
        print(f"{self.name} gets hit by {dmg} dmg! HP left: {self.get_hp()}")

# -- Main Program --
# Instantiate Objects
Layla = Hero("Layla", 100, 15)
Zilong = Hero("Zilong", 120, 20)

# Calling Methods
Layla.info()
Zilong.info()

print("\n\n--- Buff Hero ---")
Layla.__hp = 9999
print(Layla.__hp)
Layla.set_hp(50)
print(Layla.get_hp()) 

print(f"Brute force try: {Layla._Hero__hp}")