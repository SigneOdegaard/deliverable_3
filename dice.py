
# TASK 2

import random 


#  Creates the dice class
class Dice:
    """
    Represents a dice with a specified number of sides.

    Attributes:
        sides (int): The number of sides on the dice.
    """


    def __init__(self, sides: int = 6) -> None:

        # Adds a control:
            # The dice needs to have at least two sides (n >= 2)
        if sides < 2:
                    raise ValueError("A dice must have at least 2 sides")

        self.sides = sides


# Adds a roll() method to roll the dice
    def roll(self) -> int:
        """Rolls the dice and returns a random number."""
        return random.randint(1, self.sides)  

    # random.randint() - generates a random number
    # 1 - the lowest possible value 
    # 1. self.sides - the highest possible value



# Adds a __repr__ method that returns string representations like Dice(sides=6)
# --> Create a method that provides a string representation of the dice object:
    def __repr__(self) -> str:
        """Returns a string representation of the dice."""
        return f"Dice(sides={self.sides})"

    # __repr__ - determines how the object is represented as a string
    # -> str - the method returns a string



# Implement a __call__ method that allow you to roll the dice
# --> We want to use the dice object as if it were a function
    def __call__(self) -> int:
        """Allows the dice object to be called like a function."""
        return self.roll()

    # __call__ - allows us to call an object as if it were a function
    # -> int - returns an integer 








