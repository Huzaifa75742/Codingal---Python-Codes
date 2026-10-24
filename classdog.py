class dog:
    animal = "Dog"

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def display(self):
        print("Breed:", self.breed)
        print("Color:", self.color)
        print("Animal:", self.animal)
        print()

dog1 = dog("Labrador", "Black")
dog2 = dog("Beagle", "Brown")

dog1.display
dog2.display()