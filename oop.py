# Base class: Superhero
class Superhero:
    def __init__(self, name, alias, power_level):
        self.name = name
        self.__alias = alias   # Encapsulated attribute
        self.power_level = power_level

    def reveal_identity(self):
        return f"My real name is {self.__alias}."

    def use_power(self):
        return f"{self.name} uses a generic power."

    def get_power_level(self):
        return self.power_level

    def __str__(self):
        return f"{self.name} (Power Level: {self.power_level})"

# Derived class: FireHero
class FireHero(Superhero):
    def __init__(self, name, alias, power_level, flame_color):
        super().__init__(name, alias, power_level)
        self.flame_color = flame_color

    def use_power(self):
        return f"{self.name} engulfs the area in {self.flame_color} flames!"

# Derived class: SpeedHero
class SpeedHero(Superhero):
    def __init__(self, name, alias, power_level, top_speed):
        super().__init__(name, alias, power_level)
        self.top_speed = top_speed

    def use_power(self):
        return f"{self.name} dashes at {self.top_speed} km/h to stop the enemy!"


# Main program to create and use hero objects
if __name__ == "__main__":
    blaze = FireHero("Blaze", "Emily Sparks", 85, "blue")
    flashwing = SpeedHero("Flashwing", "Derek Bolt", 90, 1200)

    print(blaze)
    print(blaze.use_power())
    print(blaze.reveal_identity())

    print()

    print(flashwing)
    print(flashwing.use_power())
    print(flashwing.reveal_identity())