# TASK 5

from character import Character
from character import Warrior
from character import Mage

class Battle:
    """
    Represents a battle between two characters.

    Attributes:
        hero (Character): The first character in the battle.
        enemy (Character): The second character in the battle.
    """

    def __init__(self, hero: Character, enemy: Character) -> None:
        """Initialise the Battle"""
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """Simulates 1 round of battle between the hero and the enemy."""

        if self.hero.is_alive and self.enemy.is_alive:
            # Hero attacks
            enemy_hp_before = self.enemy.hp

            self.hero.attack(self.enemy)

            damage_dealt = enemy_hp_before - self.enemy.hp

            print(f"{self.hero.name} attacks {self.enemy.name}!")
            print(f"Damage dealt: {damage_dealt}")
            print(f"{self.enemy.name} has {self.enemy.hp} HP remaining.\n")

            # Enemy attacks if still alive
            if self.enemy.is_alive:

                hero_hp_before = self.hero.hp

                self.enemy.attack(self.hero)

                damage_dealt = hero_hp_before - self.hero.hp

                print(f"{self.enemy.name} attacks {self.hero.name}!")
                print(f"Damage dealt: {damage_dealt}")
                print(f"{self.hero.name} has {self.hero.hp} HP remaining.\n")

    def simulate_battle(self) -> None:
        """Simulates the battle until one character is defeated."""

        round_number = 0

        print(f"Fighters! enter the arena!")
        self.hero.introduce()
        if isinstance(self.hero, Warrior):
            print(f"{self.hero.name} is a mighty Warrior and is equipped with armor!")
        if isinstance(self.hero, Mage):
            print(f"{self.hero.name} is a powerful Mage and is equipped with magical mana!")

        self.enemy.introduce()
        if isinstance(self.enemy, Warrior):
            print(f"{self.enemy.name} is a mighty Warrior and is equipped with armor!")
        if isinstance(self.enemy, Mage):
            print(f"{self.enemy.name} is a powerful Mage and is equipped with magical mana!")

        print(f"Battle between {self.hero.name} and {self.enemy.name} begins!")

        while self.hero.is_alive and self.enemy.is_alive:
            round_number += 1

            print(f"--- Round {round_number} ---")

            self.play_round()
            
        if self.hero.is_alive:
            print(f"{self.hero.name} wins!")
        else:
            print(f"{self.enemy.name} wins!")


