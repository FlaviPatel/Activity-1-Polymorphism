class Dog:
    def __init__(self, name):
        self.name = name

    def makesound(self):
        print(f"My name is {self.name} and I can bark")

class Cat:
    def __init__(self, name):
        self.name = name

    def makesound(self):
        print(f"My name is {self.name} and I can meow")

# Create the object
bunny = Dog("Bunny")
fuzzy = Cat('Fuzzy')

# Implement the Polymorphism
pets = (bunny, fuzzy)

for pet in pets:
    pet.makesound()