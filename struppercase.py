class fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def intro(self):
        print("Hello, I am", self.name,  self.color)
apple = fruit("Apple","Red")
apple.intro()