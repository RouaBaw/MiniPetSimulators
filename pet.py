class Pet:
    def __init__(self, name, energy_level):
        self.name = name
        self.energy_level = energy_level

    def feed_pet(self):
        self.energy_level += 1
        print(f"{self.name} was fed. Energy level is now {self.energy_level}.")