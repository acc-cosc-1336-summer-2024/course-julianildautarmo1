import random  # Import internal Python files that allow for use of random number generator

class Die:  # Create class
    
    def __init__(self):  # Initialization step
        self.__roll_value = None

    def roll(self):  # Create dice roll operation and limit options to 1-6
        self.__roll_value = random.randint(1, 6)

    def get_roll(self):  # Return the roll when called
        return self.__roll_value
    
    def __str__(self):  # Output to user
        return f"The die landed on {self.__roll_value}."