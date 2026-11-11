# Using the game-simulator_v1.py code 

# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

from items import Weapon

class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None= None) -> None:
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


        # New methid - Point 3:
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
    