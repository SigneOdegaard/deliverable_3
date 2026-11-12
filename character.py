# TASK 1
# Using the game-simulator_v1.py code 

# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

from items import Weapon

class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None = None) -> None:
        """
        Initialise the Character
        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
            weapon (Weapon | None): The optional weapon the character can wield (default = None)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon  # Optional weapon attribute, default is None


        # New method - Point 1:
    def take_damage(self, amount: int) -> None:
        """Reduces the character's own health points.."""
        self._hp -= amount
        self._hp = max(self._hp, 0)


        # New method - Point 2:
    def heal(self, amount: int) -> None:
        """Heals the character by a specified amount."""
        self._hp += amount     # Adds HP (hit points)
        self._hp = min(self._hp, self.hp_max)


        # New method - Point 3:
    def attack(self, target) -> None:
        """Attacks another character and deals damage."""
        if self.weapon is not None:
            damage_dealt = self.weapon.roll_damage()
        else:
            damage_dealt = self.damage

        target.take_damage(damage_dealt)




    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe
        edits."""
        return self._hp

    # New method - Point 4:
    @property
    def is_alive(self) -> bool:
        """Sjekker om karakteren fortsatt lever."""
        return self._hp > 0



# TASK 4:
# Warrior subclass

class Warrior(Character):
    """
    Represents a warrior character with defensive armor.

    Inherits attributes and methods from the Character class
    and reduces incoming damage based on its armor value.

    Attributes:
        armor (int): The amount of damage absorbed by the warrior's armor.
    """

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, armor: int = 5, weapon: Weapon | None = None):
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor

# Overriding: Method that subtracts the full amount of damage from HP
    def take_damage(self, amount: int) -> None:
        """Reduces incoming damage by the warrior's armor."""
        reduced_damage = max(amount - self.armor, 0)
        super().take_damage(reduced_damage)

    # amount - the damage the Warrior receives
    # self.armor - reduces the incoming damage before it is applied to the warrior's HP (reduces the amount of damage the warrior receives)
    # max(..., 0) - ensures that the damage can never be negative
    # super().take_damage(reduced_damage) - uses the take_damage() method from the Character class to subtract the reduced damage from HP


# Mage subclass
# Mana ()= a type of magical energy or power used in many fantasy games)
class Mage(Character):
    """
    Represents a mage character with mana.

    Inherits attributes and methods from the Character class
    and uses mana to perform powerful magical attacks.

    Attributes:
        mana (int): The mage's current mana.
        mana_max (int): The mage's maximum mana.
    """

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10,
             mana: int = 30, mana_max: int = 30, weapon=None):
        super().__init__(name, hp_max, damage, weapon)
        self.mana = mana
        self.mana_max = mana_max 

    # mana: int = 30 - gives the Mage 30 mana by default
    # mana_max: int = 30 - sets the maximum mana to 30
    # super().__init__(...) - inherits the standard attributes from the Character class
    # self.mana and self.mana_max store the mana values



    # Override the Character.attack() method
    def attack(self, target) -> None:
        if self.mana >= 10:
            self.mana -= 10
            magical_damage = self.damage * 2
            target.take_damage(magical_damage)
        else:
            super().attack(target)
            self.mana = min(self.mana + 5, self.mana_max)

 # When the Mage has at least 10 mana:
    # self.mana -= 10 - consumes 10 mana
    # self.damage * 2 - doubles the base damage
    # target.take_damage(magical_damage) - applies magical damage directly
    # --> Do not use super().attack() here because it could have used the weapon

# When the Mage has less than 10 mana:
    # super().attack(target) - uses the standard attack from the Character class (This also allows the Mage to use a weapon if they have one)
    # self.mana = min(self.mana + 5, self.mana_max) restores 5 mana without allowing the mana to exceed the maximum


