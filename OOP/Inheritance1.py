# Base class
class GameCharacter:
    def __init__(self, name, health):  # this is the constructor method
        self.name = name      # 'self' refers to the instance of the class
        self.health = health

    def show_info(self):
        print(f"Character: {self.name}, Health: {self.health}")

# Derived class (inherits from GameCharacter)


class Warrior(GameCharacter):
    def __init__(self, name, health, strength):
        super().__init__(name, health)  # Use 'super()' to call the base class constructor
        self.strength = strength

    def show_info(self):  # method overriding
        super().show_info()  # Call base class method
        print(f"Strength: {self.strength}")

# Another derived class


class Mage(GameCharacter):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana

    def show_info(self):
        super().show_info()
        print(f"Mana: {self.mana}")


# Create objects
# Python doesn't support method overloading in the same way Java or C++ does.
w = Warrior("Thor", 100, 80)
# Instead, each class defines one constructor, and child classes use super() to extend it.
# obj = Warrior() ❌ is incorrect, because the __init__ method in Warrior requires three arguments: So we cant use default constructor as usual
m = Mage("Merlin", 70, 120)

# Display character info
w.show_info()
print("---")
m.show_info()

''' Output - 
Character: Thor, Health: 100
Strength: 80
---
Character: Merlin, Health: 70
Mana: 120
'''
