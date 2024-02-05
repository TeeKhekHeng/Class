class Animal:
    def __init__(self, type, sound):
        self.type = type
        self.sound = sound
    def make_sound(self):
        self.sound = "Make Sound"
    def animal_sounds(self):
        return f"{self.sound} for a {self.type}"

class Dog(Animal):
    def __init__(self, type, sound):
        super().__init__(type, sound)
    def make_sound(self):
        self.sound = "Woof!"
    def animal_sounds(self):
        return super().animal_sounds()

class Cat(Animal):
    def __init__(self, type, sound):
        super().__init__(type, sound)
    def make_sound(self):
        self.sound = "Meow!"
    def animal_sounds(self):
        return super().animal_sounds()

class Duck(Animal):
    def __init__(self, type, sound):
        super().__init__(type, sound)
    def make_sound(self):
        self.sound = "Quack!"
    def animal_sounds(self):
        return super().animal_sounds()

dogg = Dog("dog", "Woof!")
catt = Cat("cat", "Meow!")
duckk = Duck("duck", "Quack!")

print(dogg.animal_sounds())
print(catt.animal_sounds())
print(duckk.animal_sounds())