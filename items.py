# TASK 3

from dice import Dice

class Weapon:
    """
    Represents a weapon with a name and damage value based on  a dice roll.

    Attributes:
        name (str): The name of the weapon.
        damage_dice (Dice): The dice used to determine damage.
    """

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """Initialise the Weapon"""
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Rolls the damage dice to determine the damage dealt by the weapon."""
        return self.damage_dice.roll()
    

