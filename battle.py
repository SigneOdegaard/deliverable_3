# TASK 5

from character import Character

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
            self.hero.attack(self.enemy)

            if self.enemy.is_alive:
                self.enemy.attack(self.hero)

    def simulate_battle(self) -> None:
        """Simulates the battle until one character is defeated."""
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()

        if self.hero.is_alive:
            print(f"{self.hero.name} wins!")
        else:
            print(f"{self.enemy.name} wins!")


